#!/usr/bin/env python3
"""Vérifie la cohérence des données ouvertes du dépôt GPC-ONR.

Contrôles :
  1. 32 cibles, réparties 8/5/8/4/7 sur les 5 axes ;
  2. JSON et CSV identiques (codes, libellés, explications) ;
  3. chaque cible possède un libellé et une explication non vides ;
  4. matrice de priorisation : 16 combinaisons importance x performance ;
  5. libellés du JSON présents à l'identique dans le classeur Template.xlsx ;
  6. absence des fautes déjà corrigées.

Sortie : code 0 si tout est conforme, 1 sinon.
"""
import csv
import json
import re
import sys
import zipfile
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CIBLES_PAR_AXE = {1: 8, 2: 5, 3: 8, 4: 4, 5: 7}
FAUTES = ["vis-àvis", "utilisatuer", "garrantissant", "accompagnat ", "cbile", "partie prenantes"]

erreurs = []


def verifier(condition, message):
    if not condition:
        erreurs.append(message)


referentiel = json.loads((ROOT / "data/onr-referentiel.json").read_text(encoding="utf8"))
cibles = {c["code"]: c for a in referentiel["axes"] for c in a["cibles"]}

# 1. structure
verifier(len(cibles) == 32, f"32 cibles attendues, {len(cibles)} trouvées")
for axe in referentiel["axes"]:
    attendu = CIBLES_PAR_AXE[axe["numero"]]
    verifier(
        len(axe["cibles"]) == attendu,
        f"axe {axe['numero']} : {attendu} cibles attendues, {len(axe['cibles'])} trouvées",
    )

# 2 et 3. JSON vs CSV, champs non vides
with (ROOT / "data/onr-referentiel.csv").open(encoding="utf8") as f:
    lignes = list(csv.DictReader(f))
verifier(len(lignes) == len(cibles), f"CSV : {len(lignes)} lignes pour {len(cibles)} cibles")
for ligne in lignes:
    code = ligne["cible_code"]
    if code not in cibles:
        erreurs.append(f"CSV : cible {code} absente du JSON")
        continue
    verifier(
        ligne["cible_libelle"] == cibles[code]["libelle"],
        f"cible {code} : libellé JSON et CSV différents",
    )
    verifier(
        ligne["cible_explication"] == cibles[code]["explication"],
        f"cible {code} : explication JSON et CSV différentes",
    )
for code, cible in cibles.items():
    verifier(cible.get("libelle", "").strip(), f"cible {code} : libellé vide")
    verifier(cible.get("explication", "").strip(), f"cible {code} : explication vide")

# 4. matrice
matrice = json.loads((ROOT / "data/matrice-priorisation.json").read_text(encoding="utf8"))
combinaisons = matrice.get("combinaisons", [])
verifier(len(combinaisons) == 16, f"16 combinaisons attendues, {len(combinaisons)} trouvées")
attendues = {(i, p) for i in range(4) for p in range(1, 5)}
verifier(
    {(c["importance"], c["performance"]) for c in combinaisons} == attendues,
    "matrice : combinaisons importance x performance incomplètes",
)

# 5. classeur de référence
template = next(ROOT.glob("*Template.xlsx"), None)
verifier(template is not None, "classeur Template.xlsx introuvable")
if template:
    classeur = zipfile.ZipFile(template)
    xml = classeur.read("xl/sharedStrings.xml").decode("utf8")
    chaines = {
        unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", bloc, re.S)))
        for bloc in re.findall(r"<si>(.*?)</si>", xml, re.S)
    }
    # les cibles ajoutées après coup sont écrites en texte direct dans la cellule
    for nom in classeur.namelist():
        if nom.startswith("xl/worksheets/sheet"):
            feuille = classeur.read(nom).decode("utf8")
            chaines.update(
                unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", bloc, re.S)))
                for bloc in re.findall(r"<is>(.*?)</is>", feuille, re.S)
            )
    normaliser = lambda s: re.sub(r"\s+", " ", s.replace("’", "'")).strip()
    chaines_normalisees = {normaliser(s) for s in chaines}
    for code, cible in cibles.items():
        verifier(
            normaliser(cible["libelle"]) in chaines_normalisees,
            f"cible {code} : libellé absent du classeur Template.xlsx",
        )

# 6. fautes corrigées
for chemin in list(ROOT.glob("docs/*.md")) + list(ROOT.glob("data/*")) + [ROOT / "README.md"]:
    contenu = chemin.read_text(encoding="utf8", errors="ignore")
    for faute in FAUTES:
        verifier(faute not in contenu, f"{chemin.name} : faute réintroduite « {faute} »")

if erreurs:
    print(f"{len(erreurs)} erreur(s) :")
    for e in erreurs:
        print(f"  - {e}")
    sys.exit(1)

print(f"Données conformes : {len(cibles)} cibles, {len(combinaisons)} combinaisons, classeur aligné.")
