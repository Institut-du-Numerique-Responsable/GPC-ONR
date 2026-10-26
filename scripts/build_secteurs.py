#!/usr/bin/env python3
"""Construit les versions sectorielles de la GPC-ONR.

Pour chaque dossier secteurs/<id>/ qui contient un referentiel.json :
  - onr-referentiel.csv : les 32 cibles reformulées, puis les cibles métier ;
  - onr-odd.csv : liens ODD du référentiel commun, complétés par ceux des cibles métier ;
  - GPC-ONR_<id>_Template.xlsx : classeur dérivé du modèle INR. Les 32 cibles sont
    reformulées, une feuille « Cibles métier » est ajoutée après « ONR 5 », et les
    logos et crédits des co-éditeurs sont ajoutés. Formules et graphiques sont conservés ;
  - docs/secteurs/<id>.md : page de documentation.

Le classeur est modifié au niveau XML, sans bibliothèque tierce, pour ne rien perdre
du modèle (graphiques, commentaires, validations, mises en forme conditionnelles).

Usage : python3 scripts/build_secteurs.py
Le résultat est déterministe : relancer le script sans rien changer ne modifie aucun fichier.
"""
import csv
import html
import io
import json
import re
import struct
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from couverture_odd import NB_CIBLES_ODD, NOMS_ODD, charger_liens, pct, structurels  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "INR_GPC_ONR Template.xlsx"
LOGOS = [  # (fichier dans secteurs/logos, nom affiché)
    ("logo-lanum.png", "LaNum Pays Basque"),
    ("logo-neonum.png", "NÉONUM"),
]
DEPOT = "https://github.com/Institut-du-Numerique-Responsable/GPC-ONR"
COEDITEURS = "l'Institut du Numérique Responsable (INR) et LaNum Pays Basque"
CADRE = "dans le cadre du projet NÉONUM"
FEUILLE_SOURCE_METIER = "ONR 2"  # 5 cibles, comme chaque jeu de cibles métier
NOM_FEUILLE_METIER = "Cibles métier"

NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
REL_IMAGE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
REL_SHEET = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
EMU_PAR_PX = 9525

erreurs = []


# --- outils XML ---------------------------------------------------------------

def motif_texte(texte):
    """Expression régulière qui retrouve un texte dans du XML, quelle que soit
    la forme de l'apostrophe (droite, typographique, entité)."""
    morceaux = []
    for car in texte:
        if car in "'’":
            morceaux.append("(?:'|’|&#x27;|&#39;|&apos;)")
        else:
            morceaux.append(re.escape(html.escape(car, quote=False)))
    return re.compile("".join(morceaux))


def remplacer_texte(xml, ancien, nouveau):
    return motif_texte(ancien).subn(lambda _: html.escape(nouveau, quote=False), xml)


def taille_png(donnees):
    largeur, hauteur = struct.unpack(">II", donnees[16:24])
    return largeur, hauteur


def positions_colonnes(feuille_xml):
    """Abscisse (EMU) du bord gauche de chaque colonne, à partir des largeurs déclarées."""
    defaut = re.search(r'defaultColWidth="([\d.]+)"', feuille_xml)
    defaut = float(defaut.group(1)) if defaut else 8.43
    largeurs = {}
    for mn, mx, w in re.findall(r'<(?:x:)?col min="(\d+)" max="(\d+)" width="([\d.]+)"', feuille_xml):
        for c in range(int(mn), min(int(mx), 200) + 1):
            largeurs[c] = float(w)
    positions, x = [], 0
    for c in range(1, 201):
        positions.append(x)
        x += int(largeurs.get(c, defaut) * 7 + 5) * EMU_PAR_PX
    return positions


def ancre_image(positions, x, row, row_off, cx, cy, rid, id_forme, nom):
    col = max(i for i, p in enumerate(positions) if p <= x)
    return (
        f'<xdr:oneCellAnchor><xdr:from><xdr:col>{col}</xdr:col><xdr:colOff>{x - positions[col]}</xdr:colOff>'
        f'<xdr:row>{row}</xdr:row><xdr:rowOff>{row_off}</xdr:rowOff></xdr:from>'
        f'<xdr:ext cx="{cx}" cy="{cy}"/><xdr:pic><xdr:nvPicPr><xdr:cNvPr id="{id_forme}" name="{html.escape(nom)}" '
        f'descr="Logo {html.escape(nom)}"/><xdr:cNvPicPr><a:picLocks xmlns:a="{NS_A}" noChangeAspect="1"/>'
        f'</xdr:cNvPicPr></xdr:nvPicPr><xdr:blipFill><a:blip xmlns:a="{NS_A}" xmlns:r="{NS_R}" r:embed="{rid}"/>'
        f'<a:stretch xmlns:a="{NS_A}"><a:fillRect/></a:stretch></xdr:blipFill><xdr:spPr>'
        f'<a:prstGeom xmlns:a="{NS_A}" prst="rect"/></xdr:spPr></xdr:pic><xdr:clientData/></xdr:oneCellAnchor>'
    )


def chemin_cible(base, cible):
    """Résout la cible d'une relation OPC relativement au dossier de la partie source."""
    if cible.startswith("/"):
        return cible[1:]
    parties = base.split("/")[:-1]
    for p in cible.split("/"):
        if p == "..":
            parties.pop()
        elif p != ".":
            parties.append(p)
    return "/".join(parties)


def chemin_rels(partie):
    dossier, nom = partie.rsplit("/", 1)
    return f"{dossier}/_rels/{nom}.rels"


def relations(parts, partie):
    xml = parts.get(chemin_rels(partie), "")
    return [
        (dict(re.findall(r'(\w+)="([^"]*)"', m)))
        for m in re.findall(r"<Relationship ([^>]*)/?>", xml)
    ]


def ajouter_relation(parts, partie, rid, type_, cible):
    nom = chemin_rels(partie)
    xml = parts.get(nom) or (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"></Relationships>'
    )
    parts[nom] = xml.replace(
        "</Relationships>", f'<Relationship Id="{rid}" Type="{type_}" Target="{cible}"/></Relationships>'
    )


# --- classeur -----------------------------------------------------------------

def feuilles(parts):
    """[(nom, rId, chemin de la partie)] dans l'ordre du classeur."""
    rels = {r["Id"]: chemin_cible("xl/workbook.xml", r["Target"]) for r in relations(parts, "xl/workbook.xml")}
    return [
        (html.unescape(n), rid, rels[rid])
        for n, rid in re.findall(r'<sheet name="([^"]+)"[^>]*r:id="(rId\w+)"', parts["xl/workbook.xml"])
    ]


def ajouter_logos(parts, logos):
    """Place les logos des co-éditeurs à droite du logo INR, sur chaque feuille qui en porte un."""
    for _, _, feuille in feuilles(parts):
        for rel in relations(parts, feuille):
            if not rel["Type"].endswith("/drawing"):
                continue
            dessin = chemin_cible(feuille, rel["Target"])
            xml = parts[dessin]
            ids_inr = {r["Id"] for r in relations(parts, dessin) if "inr" in r["Target"].lower()}
            ancre = next(
                (a for a in re.findall(r"<xdr:oneCellAnchor>.*?</xdr:oneCellAnchor>", xml, re.S)
                 if any(f'r:embed="{i}"' in a for i in ids_inr)),
                None,
            )
            if ancre is None:
                continue
            col, col_off, row, row_off = (int(v) for v in re.findall(
                r"<xdr:(?:col|colOff|row|rowOff)>(\d+)<", ancre)[:4])
            cx, cy = (int(v) for v in re.search(r'<xdr:ext cx="(\d+)" cy="(\d+)"', ancre).groups())
            positions = positions_colonnes(parts[feuille])
            # Logo INR en haut à gauche (Accueil) : les co-éditeurs suivent à sa droite.
            # Logo INR calé à droite de la feuille : ils se placent à sa gauche, pour ne pas
            # déborder de la zone imprimable.
            x_inr = positions[col] + col_off
            a_droite = col <= 2
            largeurs = [cy * largeur // hauteur for _, _, largeur, hauteur in logos]
            x = x_inr + cx if a_droite else x_inr - sum(largeurs) - len(logos) * (cy // 3)
            nouvelles = []
            for i, ((fichier, nom, _, _), largeur_emu) in enumerate(zip(logos, largeurs)):
                rid = f"logoCoediteur{i + 1}"
                ajouter_relation(parts, dessin, rid, REL_IMAGE, f"/xl/media/{fichier}")
                if a_droite:
                    x += cy // 3
                nouvelles.append(ancre_image(positions, x, row, row_off, largeur_emu, cy, rid, 900 + i, nom))
                x += largeur_emu + (0 if a_droite else cy // 3)
            parts[dessin] = xml.replace("</xdr:wsDr>", "".join(nouvelles) + "</xdr:wsDr>")


def paragraphe_comme(modele, texte):
    """Nouveau paragraphe DrawingML au format du paragraphe modèle (premier run)."""
    ppr = re.search(r"<a:pPr[^>]*/>|<a:pPr[^>]*>.*?</a:pPr>", modele, re.S)
    rpr = re.search(r"<a:r>(<a:rPr[^>]*/>|<a:rPr[^>]*>.*?</a:rPr>)", modele, re.S)
    return (
        "<a:p>" + (ppr.group(0) if ppr else "")
        + "<a:r>" + (rpr.group(1) if rpr else "") + f"<a:t>{html.escape(texte, quote=False)}</a:t></a:r></a:p>"
    )


def personnaliser_accueil(parts, variante):
    feuille = next(p for n, _, p in feuilles(parts) if n == "Accueil")
    for rel in relations(parts, feuille):
        dessin = chemin_cible(feuille, rel["Target"])
        if not rel["Type"].endswith("/drawing") or "Crédits" not in parts[dessin]:
            continue
        xml = parts[dessin]
        paragraphes = re.findall(r"<a:p>.*?</a:p>", xml, re.S)
        texte = lambda p: "".join(re.findall(r"<a:t>([^<]*)</a:t>", p))
        sous_titre = next(p for p in paragraphes if texte(p).startswith("OUTIL D"))
        titre = next(p for p in paragraphes if texte(p) == "(GPC-ONR)")
        credits = next(p for p in paragraphes if texte(p).startswith("Cette fiche est inspirée"))
        xml = xml.replace(titre, titre + paragraphe_comme(sous_titre, "VERSION " + variante["nom"].upper()), 1)
        xml = xml.replace(credits, credits + paragraphe_comme(credits, (
            f"Version « {variante['nom']} » co-éditée par {COEDITEURS}, {CADRE}, "
            "d'après la GPC-ONR de l'INR. "
            "Les cibles métier (feuille « Cibles métier ») ne sont pas reprises dans les feuilles de résultats."
        )), 1)
        parts[dessin] = xml
        return
    erreurs.append("Accueil : zone de texte des crédits introuvable")


def copier_partie(parts, source, cible):
    parts[cible] = parts[source]
    types = parts["[Content_Types].xml"]
    m = re.search(rf'<Override PartName="/{re.escape(source)}" ContentType="([^"]+)"/>', types)
    if m:
        parts["[Content_Types].xml"] = types.replace(
            "</Types>", f'<Override PartName="/{cible}" ContentType="{m.group(1)}"/></Types>')


def libre(parts, modele):
    """Premier nom de partie libre de la forme modele.format(n)."""
    n = 1
    while modele.format(n) in parts:
        n += 1
    return modele.format(n)


def ajouter_feuille_metier(parts, variante, cibles_metier, cibles, base):
    nom_src, _, src = next(f for f in feuilles(parts) if f[0] == FEUILLE_SOURCE_METIER)
    nouvelle = libre(parts, "xl/worksheets/sheet{}.xml")
    copier_partie(parts, src, nouvelle)
    xml = parts[nouvelle]

    # en-tête et cibles
    entete = f"Cibles propres au secteur · {variante['nom']}"
    xml, n = re.subn(r'(<x:c r="B2"[^>]*>)<x:v>[^<]*</x:v>', lambda m: m.group(1) + f"<x:v>{html.escape(entete)}</x:v>", xml)
    if not n:
        erreurs.append("feuille métier : en-tête B2 introuvable")
    axe2 = [c for a in base["axes"] if a["numero"] == 2 for c in a["cibles"]]
    for ancienne, metier in zip(axe2, cibles_metier):
        xml, n1 = re.subn(rf'(<x:c r="B\d+"[^>]*><x:is><x:t[^>]*>){re.escape(ancienne["code"])}(</x:t>)',
                          lambda m: m.group(1) + metier["code"] + m.group(2), xml)
        xml, n2 = remplacer_texte(xml, cibles[ancienne["code"]]["libelle"], metier["libelle"])
        if not (n1 and n2):
            erreurs.append(f"feuille métier : cible {ancienne['code']} introuvable")
    parts[nouvelle] = xml

    # relations : commentaires, VML, réglages d'impression et logos sont dupliqués
    for rel in relations(parts, src):
        cible = chemin_cible(src, rel["Target"])
        modele = re.sub(r"\d*(\.\w+)$", r"{}\1", cible)
        copie = libre(parts, modele)
        copier_partie(parts, cible, copie)
        for sous in relations(parts, cible):
            ajouter_relation(parts, copie, sous["Id"], sous["Type"], sous["Target"])
        ajouter_relation(parts, nouvelle, rel["Id"], rel["Type"], "/" + copie)

    # classeur : nouvelle feuille insérée après « ONR 5 »
    wb = parts["xl/workbook.xml"]
    rid = "rIdCiblesMetier"
    ajouter_relation(parts, "xl/workbook.xml", rid, REL_SHEET, "/" + nouvelle)
    sheet_id = max(int(i) for i in re.findall(r'sheetId="(\d+)"', wb)) + 1
    noms = [f[0] for f in feuilles(parts)]
    rang = noms.index("ONR 5") + 1
    wb = re.sub(r'localSheetId="(\d+)"',
                lambda m: f'localSheetId="{int(m.group(1)) + (int(m.group(1)) >= rang)}"', wb)
    ancre = re.search(r'<sheet name="ONR 5"[^>]*/>', wb).group(0)
    wb = wb.replace(ancre, ancre + f'<sheet name="{NOM_FEUILLE_METIER}" sheetId="{sheet_id}" r:id="{rid}"/>')
    parts["xl/workbook.xml"] = wb

    # propriétés : liste des titres de feuilles
    app = parts.get("docProps/app.xml", "")
    if "<vt:lpstr>ONR 5</vt:lpstr>" in app:
        app = app.replace("<vt:lpstr>ONR 5</vt:lpstr>", f"<vt:lpstr>ONR 5</vt:lpstr><vt:lpstr>{NOM_FEUILLE_METIER}</vt:lpstr>")
        app = re.sub(r'(<TitlesOfParts><vt:vector size=")(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1), app)
        app = re.sub(r"(<vt:lpstr>Feuilles de calcul</vt:lpstr></vt:variant><vt:variant><vt:i4>)(\d+)",
                     lambda m: m.group(1) + str(int(m.group(2)) + 1), app)
        parts["docProps/app.xml"] = app


def construire_classeur(variante, cibles, cibles_metier, base, sortie):
    with zipfile.ZipFile(TEMPLATE) as z:
        ordre = z.namelist()
        # parties texte décodées, parties binaires (images, réglages d'impression) laissées en octets
        parts = {n: z.read(n) for n in ordre}
    for n, d in parts.items():
        if n.endswith((".xml", ".rels", ".vml")):
            parts[n] = d.decode("utf8")

    # 1. reformulation des 32 cibles (cellules en texte direct et chaînes partagées)
    for code, c in cibles.items():
        trouve = 0
        for nom in parts:
            if nom.startswith("xl/worksheets/sheet"):
                parts[nom], n = remplacer_texte(parts[nom], base["cibles"][code]["libelle"], c["libelle"])
                trouve += n
        parts["xl/sharedStrings.xml"], _ = remplacer_texte(
            parts["xl/sharedStrings.xml"], base["cibles"][code]["libelle_charte"], c["libelle_charte"])
        if not trouve:
            erreurs.append(f"classeur : cible {code} introuvable")

    # 2. feuille des cibles métier (copie de « ONR 2 », avant l'ajout des logos)
    ajouter_feuille_metier(parts, variante, cibles_metier, cibles, base)

    # 3. logos et crédits
    logos = []
    for fichier, nom in LOGOS:
        donnees = (ROOT / "secteurs/logos" / fichier).read_bytes()
        parts[f"xl/media/{fichier}"] = donnees
        logos.append((fichier, nom, *taille_png(donnees)))
    ajouter_logos(parts, logos)
    personnaliser_accueil(parts, variante)

    # 4. propriétés du document
    parts["docProps/core.xml"] = re.sub(
        r"<dc:title>[^<]*</dc:title>", f"<dc:title>{html.escape(variante['titre'])}</dc:title>",
        parts["docProps/core.xml"])

    # date fixe : le classeur ne change que si son contenu change
    nouveaux = sorted(n for n in parts if n not in ordre)
    with zipfile.ZipFile(sortie, "w", zipfile.ZIP_DEFLATED) as z:
        for nom in ordre + nouveaux:
            info = zipfile.ZipInfo(nom, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, parts[nom].encode("utf8") if isinstance(parts[nom], str) else parts[nom])


# --- données et documentation ------------------------------------------------

def ecrire_csv(chemin, entetes, lignes):
    with chemin.open("w", encoding="utf8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(entetes)
        w.writerows(lignes)


def construire_doc(variante, axes, cibles, cibles_metier, liens, chemin_xlsx):
    s = structurels(liens)
    par_cible = {}
    for l in liens:
        par_cible.setdefault(l["cible_code"], []).append(l)
    odd = lambda code: (
        "**" + next(l["cible_odd"] for l in par_cible[code] if l["lien"] == "principal") + "**"
        + "".join(", " + l["cible_odd"] for l in par_cible[code] if l["lien"] == "contributif")
    )
    lignes = [
        f"# {variante['nom']}",
        "",
        f"Version de la GPC-ONR adaptée aux {variante['public'][0].lower() + variante['public'][1:]}.",
        "",
        '<div class="coedition" markdown>',
        '![Institut du Numérique Responsable](../assets/logo-inr.webp){ height=44 style="vertical-align:middle" }',
        '![LaNum Pays Basque](../assets/logo-lanum.svg){ height=44 style="vertical-align:middle" }',
        '![NÉONUM](../assets/logo-neonum.webp){ height=64 style="vertical-align:middle" }',
        "</div>",
        "",
        f"Version co-éditée par {COEDITEURS}, {CADRE}, d'après la GPC-ONR de l'INR. "
        "Elle fait partie des [versions sectorielles](index.md) de la grille.",
        "",
        "!!! note \"Version de travail\"",
        "    Les reformulations et les cibles métier sont des propositions à relire avec des personnes du secteur "
        "avant toute diffusion.",
        "",
        "## Télécharger",
        "",
        f"- [Classeur à remplir]"
        f"({DEPOT}/raw/main/secteurs/{variante['id']}/{chemin_xlsx.name})",
        f"- Données ouvertes : `secteurs/{variante['id']}/onr-referentiel.csv` et "
        f"`secteurs/{variante['id']}/onr-odd.csv`",
        "",
        f"**Cadre de référence** : {variante['cadre']}.",
        "",
        "## Ce qui change",
        "",
        "- Les **32 cibles** gardent leur code et leur sens. Seuls leur formulation et leurs exemples sont adaptés "
        "au secteur. Les résultats restent comparables avec la grille commune.",
        f"- **{len(cibles_metier)} cibles métier** (codes `{cibles_metier[0]['code'][0]}.x`), une par axe, couvrent "
        "des enjeux propres au secteur. Le classeur les regroupe dans la feuille « Cibles métier ». "
        "Elles ont leur propre calcul de priorité mais ne figurent pas dans les feuilles de résultats.",
        "",
        "## Les cibles",
        "",
    ]
    for axe in axes:
        lignes += [f"### Axe {axe['numero']} · {axe['nom']}", "", "| Cible | Formulation | En bref | ODD |", "|---|---|---|---|"]
        for code, c in cibles.items():
            if code.startswith(f"{axe['numero']}."):
                lignes.append(f"| `{code}` | {c['libelle']} | {c['explication']} | {odd(code)} |")
        for c in cibles_metier:
            if c["axe"] == axe["numero"]:
                lignes.append(f"| `{c['code']}` **métier** | {c['libelle']} | {c['explication']} | {odd(c['code'])} |")
        lignes.append("")
    lignes += [
        "## Couverture des ODD",
        "",
        "Les liens des 32 cibles reprennent ceux de la grille commune (voir [Couverture des ODD](../couverture-odd.md)). "
        "Les cibles métier ajoutent les leurs.",
        "",
        "| Indicateur | Valeur |",
        "|---|---|",
        f"| S1. ODD couverts | {len(s['odd_couverts'])}/17 ({pct(len(s['odd_couverts']) / 17)}), "
        f"dont {len(s['odd_principaux'])}/17 par un lien principal |",
        f"| S2. Cibles ODD touchées | {len(s['cibles_odd'])}/{NB_CIBLES_ODD} ({pct(len(s['cibles_odd']) / NB_CIBLES_ODD)}) |",
        f"| S4. Part des 3 ODD les plus liés | {pct(s['top3'])} |",
        "| S5. Piliers | " + ", ".join(f"{p} {pct(v / s['total'])}" for p, v in s["piliers"].items()) + " |",
        f"| S6. ODD orphelins | {', '.join(f'ODD {o} ({NOMS_ODD[o]})' for o in s['orphelins']) or 'aucun'} |",
        "",
        "Pour calculer les indicateurs d'évaluation sur votre grille :",
        "",
        "```bash",
        f"python3 scripts/couverture_odd.py --odd secteurs/{variante['id']}/onr-odd.csv ma-grille.json",
        "```",
        "",
    ]
    return "\n".join(lignes)


def main():
    base_json = json.loads((ROOT / "data/onr-referentiel.json").read_text(encoding="utf8"))
    axes = base_json["axes"]
    base = {"axes": axes, "cibles": {c["code"]: c for a in axes for c in a["cibles"]}}
    liens_communs = list(csv.DictReader((ROOT / "data/onr-odd.csv").open(encoding="utf8")))

    for source in sorted((ROOT / "secteurs").glob("*/referentiel.json")):
        dossier = source.parent
        v = json.loads(source.read_text(encoding="utf8"))
        variante, cibles, metier = v["variante"], v["cibles"], v["cibles_metier"]

        manquantes = set(base["cibles"]) ^ set(cibles)
        if manquantes:
            erreurs.append(f"{variante['id']} : cibles manquantes ou en trop {sorted(manquantes)}")
            continue
        for code, c in list(cibles.items()) + [(c["code"], c) for c in metier]:
            for champ in ("libelle", "libelle_charte", "explication"):
                if not c.get(champ, "").strip():
                    erreurs.append(f"{variante['id']} : cible {code}, champ {champ} vide")
        if [c["axe"] for c in metier] != [1, 2, 3, 4, 5]:
            erreurs.append(f"{variante['id']} : une cible métier par axe attendue")

        cibles = {code: cibles[code] for code in base["cibles"]}  # ordre du référentiel
        ecrire_csv(dossier / "onr-referentiel.csv",
                   ["axe_numero", "axe_nom", "cible_code", "metier", "cible_libelle", "cible_libelle_charte",
                    "cible_explication", "cible_code_commun"],
                   [[a["numero"], a["nom"], code, "non", c["libelle"], c["libelle_charte"], c["explication"], code]
                    for a in axes for code, c in cibles.items() if code.startswith(f"{a['numero']}.")]
                   + [[c["axe"], axes[c["axe"] - 1]["nom"], c["code"], "oui", c["libelle"], c["libelle_charte"],
                       c["explication"], ""] for c in metier])

        liens = [[l["cible_code"], l["odd"], l["cible_odd"], l["lien"], l["justification"]] for l in liens_communs]
        liens += v["odd_metier"]
        for code in [c["code"] for c in metier]:
            if sum(1 for l in v["odd_metier"] if l[0] == code and l[3] == "principal") != 1:
                erreurs.append(f"{variante['id']} : cible {code}, un seul lien ODD principal attendu")
        ecrire_csv(dossier / "onr-odd.csv", ["cible_code", "odd", "cible_odd", "lien", "justification"], liens)

        sortie = dossier / f"GPC-ONR_{variante['id']}_Template.xlsx"
        construire_classeur(variante, cibles, metier, base, sortie)
        (ROOT / "docs/secteurs" / f"{variante['id']}.md").write_text(
            construire_doc(variante, axes, cibles, metier, charger_liens(dossier / "onr-odd.csv"), sortie),
            encoding="utf8")
        print(f"{variante['id']} : {len(cibles)} cibles + {len(metier)} cibles métier, {sortie.name}")

    if erreurs:
        print(f"{len(erreurs)} erreur(s) :")
        for e in erreurs:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
