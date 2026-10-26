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
# Bandeau INR + LaNum + NÉONUM composé une fois (secteurs/logos) : il remplace le logo INR
# à la même ancre. Une image unique ne peut pas se chevaucher, quel que soit le tableur
# (Excel, LibreOffice et OnlyOffice ne calculent pas les largeurs de colonnes pareil).
BANDEAU = "bandeau-coedition.png"
DEPOT = "https://github.com/Institut-du-Numerique-Responsable/GPC-ONR"
COEDITEURS = "l'Institut du Numérique Responsable (INR) et LaNum Pays Basque"
CADRE = "pour les publics qu'elle accompagne dans le projet européen NÉONUM"
NOM_FEUILLE_METIER = "Cibles métier"

NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_IMAGE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
REL_SHEET = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"

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


def positions_colonnes(feuille_xml):
    """Abscisse approximative (EMU) du bord gauche de chaque colonne. Sert seulement à caler le
    bandeau : une erreur d'estimation le décale un peu, elle ne peut pas créer de chevauchement."""
    defaut = re.search(r'defaultColWidth="([\d.]+)"', feuille_xml)
    defaut = float(defaut.group(1)) if defaut else 8.43
    largeurs = {}
    for mn, mx, w in re.findall(r'<(?:x:)?col min="(\d+)" max="(\d+)" width="([\d.]+)"', feuille_xml):
        for c in range(int(mn), min(int(mx), 200) + 1):
            largeurs[c] = float(w)
    positions, x = [], 0
    for c in range(1, 201):
        positions.append(x)
        x += int(largeurs.get(c, defaut) * 7 + 5) * 9525
    return positions


def ajuster_hauteurs(feuille_xml, car_par_ligne=40, pt_par_ligne=11.5):
    """Agrandit les lignes de cibles dont le libellé (colonne C) dépasse la hauteur prévue."""
    def ligne(m):
        row = m.group(0)
        texte = re.search(r'<x:c r="C\d+"[^>]*t="inlineStr"><x:is><x:t[^>]*>([^<]*)</x:t>', row)
        ht = re.search(r' ht="([\d.]+)"', row)
        if not texte or not ht:
            return row
        besoin = -(-len(html.unescape(texte.group(1))) // car_par_ligne) * pt_par_ligne + 8
        if besoin <= float(ht.group(1)):
            return row
        return row.replace(ht.group(0), f' ht="{besoin:g}"', 1)
    return re.sub(r'<x:row r="\d+"[^>]*>.*?</x:row>', ligne, feuille_xml, flags=re.S)


def poser_bandeau(parts, fichier, largeur, hauteur):
    """Remplace le logo INR par le bandeau des co-éditeurs, à la même ancre et à la même hauteur."""
    for _, _, feuille in feuilles(parts):
        for rel in relations(parts, feuille):
            if not rel["Type"].endswith("/drawing"):
                continue
            dessin = chemin_cible(feuille, rel["Target"])
            ids_inr = {r["Id"] for r in relations(parts, dessin) if "inr" in r["Target"].lower()}
            xml = parts[dessin]
            for ancre in re.findall(r"<xdr:oneCellAnchor>.*?</xdr:oneCellAnchor>", xml, re.S):
                if not any(f'r:embed="{i}"' in ancre for i in ids_inr):
                    continue
                cx, cy = (int(v) for v in re.search(r'<xdr:ext cx="(\d+)" cy="(\d+)"', ancre).groups())
                bx = cy * largeur // hauteur
                nouvelle = re.sub(r'<xdr:ext cx="\d+"', f'<xdr:ext cx="{bx}"', ancre)
                col, col_off = (int(v) for v in re.findall(r"<xdr:(?:col|colOff)>(\d+)<", ancre)[:2])
                if col > 2:
                    # logo INR calé à droite : le bandeau se termine là où il se terminait
                    positions = positions_colonnes(parts[feuille])
                    x = max(0, positions[col] + col_off + cx - bx)
                    c = max(i for i, p in enumerate(positions) if p <= x)
                    nouvelle = re.sub(r"<xdr:col>\d+</xdr:col><xdr:colOff>\d+</xdr:colOff>",
                                      f"<xdr:col>{c}</xdr:col><xdr:colOff>{x - positions[c]}</xdr:colOff>",
                                      nouvelle, count=1)
                nouvelle = re.sub(r'r:embed="[^"]+"', 'r:embed="bandeauCoedition"', nouvelle)
                nouvelle = re.sub(r'(<xdr:cNvPr id="\d+" name=")[^"]*"',
                                  r'\1Logos INR, LaNum Pays Basque et NÉONUM"', nouvelle)
                xml = xml.replace(ancre, nouvelle)
                ajouter_relation(parts, dessin, "bandeauCoedition", REL_IMAGE, f"/xl/media/{fichier}")
            parts[dessin] = xml


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
            f"Version « {variante['nom']} » proposée par LaNum Pays Basque {CADRE}, "
            "et co-éditée avec l'INR, d'après la GPC-ONR. "
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
    # Feuille source : l'onglet ONR qui a juste assez de lignes ; les lignes en trop sont masquées.
    axe = min((a for a in base["axes"] if len(a["cibles"]) >= len(cibles_metier)),
              key=lambda a: len(a["cibles"]), default=None)
    if axe is None:
        erreurs.append(f"feuille métier : {len(cibles_metier)} cibles, aucun onglet ONR assez long")
        return
    _, _, src = next(f for f in feuilles(parts) if f[0] == f"ONR {axe['numero']}")
    nouvelle = libre(parts, "xl/worksheets/sheet{}.xml")
    copier_partie(parts, src, nouvelle)
    xml = parts[nouvelle]

    # en-tête et cibles
    entete = f"Cibles propres au secteur · {variante['nom']}"
    xml, n = re.subn(r'(<x:c r="B2"[^>]*>)<x:v>[^<]*</x:v>', lambda m: m.group(1) + f"<x:v>{html.escape(entete)}</x:v>", xml)
    if not n:
        erreurs.append("feuille métier : en-tête B2 introuvable")
    for i, ancienne in enumerate(axe["cibles"]):
        metier = cibles_metier[i] if i < len(cibles_metier) else {"code": "", "libelle": ""}
        motif = rf'<x:c r="B(\d+)"[^>]*><x:is><x:t[^>]*>{re.escape(ancienne["code"])}</x:t>'
        ligne = re.search(motif, xml)
        xml, n1 = re.subn(rf'(<x:c r="B\d+"[^>]*><x:is><x:t[^>]*>){re.escape(ancienne["code"])}(</x:t>)',
                          lambda m: m.group(1) + metier["code"] + m.group(2), xml)
        xml, n2 = remplacer_texte(xml, cibles[ancienne["code"]]["libelle"], metier["libelle"])
        if not (ligne and n1 and n2):
            erreurs.append(f"feuille métier : cible {ancienne['code']} introuvable")
        elif not metier["code"]:
            xml = re.sub(rf'<x:row r="{ligne.group(1)}"', f'<x:row r="{ligne.group(1)}" hidden="1"', xml, count=1)
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
    # zone d'impression et titres repris de l'onglet source
    rang_src = noms.index(f"ONR {axe['numero']}")
    copies = [
        re.sub(r'localSheetId="\d+"', f'localSheetId="{rang}"', d).replace(
            f"'ONR {axe['numero']}'!", f"'{NOM_FEUILLE_METIER}'!")
        for d in re.findall(rf'<definedName name="_xlnm\.[^"]+" localSheetId="{rang_src}"[^>]*>[^<]*</definedName>', wb)
    ]
    wb = wb.replace("</definedNames>", "".join(copies) + "</definedNames>")
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

    # 2. feuille des cibles métier (copie d'un onglet ONR, avant la pose du bandeau)
    ajouter_feuille_metier(parts, variante, cibles_metier, cibles, base)
    for nom, _, feuille in feuilles(parts):
        if nom.startswith("ONR ") or nom == NOM_FEUILLE_METIER:
            parts[feuille] = ajuster_hauteurs(parts[feuille])

    # 3. logos et crédits
    donnees = (ROOT / "secteurs/logos" / BANDEAU).read_bytes()
    parts[f"xl/media/{BANDEAU}"] = donnees
    poser_bandeau(parts, BANDEAU, *taille_png(donnees))
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
        f"Version proposée par LaNum Pays Basque {CADRE}, et co-éditée avec l'INR, d'après la GPC-ONR. "
        "Elle fait partie des [versions alternatives](index.md) de la grille.",
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
        f"- **{len(cibles_metier)} cibles métier** (codes `{cibles_metier[0]['code'][0]}.x`), réparties sur les cinq axes, couvrent "
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
        if not metier or any(c["axe"] not in (1, 2, 3, 4, 5) for c in metier):
            erreurs.append(f"{variante['id']} : cibles métier absentes ou axe hors 1-5")

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
