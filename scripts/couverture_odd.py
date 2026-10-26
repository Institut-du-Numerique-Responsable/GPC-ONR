#!/usr/bin/env python3
"""Calcule les indicateurs de couverture des ODD par la grille GPC-ONR.

Indicateurs structurels (rapprochement cibles-ODD seul) :
  S1. couverture des 17 ODD (tous liens, puis liens principaux seuls) ;
  S2. nombre de cibles ODD distinctes touchées (sur 169) ;
  S3. intensité par ODD (lien principal = 2, contributif = 1) ;
  S4. concentration : part des 3 ODD les plus liés, indice de Herfindahl ;
  S5. répartition par pilier (5P de l'Agenda 2030) ;
  S6. ODD orphelins.

Indicateurs d'évaluation (grille remplie, JSON au format data/gpc-onr-exemple.json) :
  E1. pertinence de chaque ODD pour l'organisation ;
  E2. performance de l'organisation sur chaque ODD ;
  E3. couverture effective : ODD pertinents dont la performance atteint 2/3 ;
  E4. tension : cibles liées classées « urgente » ou « prioritaire ».

Usage :
  python3 scripts/couverture_odd.py [--odd liens.csv] [grille.json]
Sans --odd, le rapprochement du référentiel commun (data/onr-odd.csv) est utilisé.
Sans grille, la grille d'exemple est utilisée ; « --odd x.csv - » n'évalue aucune grille.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POIDS = {"principal": 2, "contributif": 1}
NB_CIBLES_ODD = 169
PILIERS = {
    "Population": [1, 2, 3, 4, 5],
    "Planète": [6, 12, 13, 14, 15],
    "Prospérité": [7, 8, 9, 10, 11],
    "Paix": [16],
    "Partenariats": [17],
}
NOMS_ODD = {
    1: "Pas de pauvreté",
    2: "Faim « zéro »",
    3: "Bonne santé et bien-être",
    4: "Éducation de qualité",
    5: "Égalité entre les sexes",
    6: "Eau propre et assainissement",
    7: "Énergie propre et d'un coût abordable",
    8: "Travail décent et croissance économique",
    9: "Industrie, innovation et infrastructure",
    10: "Inégalités réduites",
    11: "Villes et communautés durables",
    12: "Consommation et production responsables",
    13: "Lutte contre les changements climatiques",
    14: "Vie aquatique",
    15: "Vie terrestre",
    16: "Paix, justice et institutions efficaces",
    17: "Partenariats pour la réalisation des objectifs",
}


def pct(x):
    return f"{100 * x:.0f} %"


def charger_liens(chemin):
    with Path(chemin).open(encoding="utf8") as f:
        return [dict(l, odd=int(l["odd"]), poids=POIDS[l["lien"]]) for l in csv.DictReader(f)]


def structurels(liens):
    intensite = defaultdict(int)
    nb_principal = defaultdict(int)
    nb_contributif = defaultdict(int)
    for l in liens:
        intensite[l["odd"]] += l["poids"]
        (nb_principal if l["lien"] == "principal" else nb_contributif)[l["odd"]] += 1
    total = sum(intensite.values())
    return {
        "intensite": intensite,
        "nb_principal": nb_principal,
        "nb_contributif": nb_contributif,
        "total": total,
        "odd_couverts": sorted(intensite),
        "odd_principaux": sorted(nb_principal),
        "cibles_odd": {l["cible_odd"] for l in liens},
        "top3": sum(sorted(intensite.values(), reverse=True)[:3]) / total,
        "herfindahl": sum((v / total) ** 2 for v in intensite.values()),
        "orphelins": [o for o in range(1, 18) if o not in intensite],
        "piliers": {p: sum(intensite[o] for o in odds) for p, odds in PILIERS.items()},
    }


def afficher_structurels(s):
    print("## Indicateurs structurels\n")
    print(f"- S1. ODD couverts : {len(s['odd_couverts'])}/17 ({pct(len(s['odd_couverts']) / 17)}) ; "
          f"par un lien principal : {len(s['odd_principaux'])}/17 ({pct(len(s['odd_principaux']) / 17)})")
    print(f"- S2. Cibles ODD touchées : {len(s['cibles_odd'])}/{NB_CIBLES_ODD} "
          f"({pct(len(s['cibles_odd']) / NB_CIBLES_ODD)})")
    print(f"- S4. Part des 3 ODD les plus liés : {pct(s['top3'])} ; indice de Herfindahl : {s['herfindahl']:.3f}")
    print(f"- S6. ODD orphelins : {', '.join(f'ODD {o}' for o in s['orphelins']) or 'aucun'}\n")

    print("| ODD | Libellé | Principal | Contributif | S3. Intensité |")
    print("|---|---|---|---|---|")
    for o in range(1, 18):
        print(f"| {o} | {NOMS_ODD[o]} | {s['nb_principal'][o]} | {s['nb_contributif'][o]} | {s['intensite'][o]} |")

    print("\n| S5. Pilier | ODD | Intensité | Part |")
    print("|---|---|---|---|")
    for pilier, odds in PILIERS.items():
        v = s["piliers"][pilier]
        print(f"| {pilier} | {', '.join(map(str, odds))} | {v} | {pct(v / s['total'])} |")


def evaluer(liens, chemin):
    grille = json.loads(Path(chemin).read_text(encoding="utf8"))
    notes = {c["code"]: c for a in grille["axes"] for c in a["cibles"]}
    matrice = json.loads((ROOT / "data/matrice-priorisation.json").read_text(encoding="utf8"))
    niveau = {(c["importance"], c["performance"]): c["valeur"] for c in matrice["combinaisons"]}

    pertinence_num = defaultdict(float)
    pertinence_den = defaultdict(float)
    perf_num = defaultdict(float)
    tension = defaultdict(set)
    for l in liens:
        c = notes.get(l["cible_code"])
        if c is None or c.get("importance") is None or c.get("performance") is None:
            continue
        imp, perf = int(c["importance"]), int(c["performance"])
        o, w = l["odd"], l["poids"]
        pertinence_num[o] += w * imp
        pertinence_den[o] += w * 3
        perf_num[o] += w * imp * (perf - 1) / 3
        if niveau.get((imp, perf), 0) >= 5:
            tension[o].add(l["cible_code"])

    print(f"\n## Indicateurs d'évaluation ({Path(chemin).name})\n")
    print("| ODD | E1. Pertinence | E2. Performance | E4. Cibles en tension |")
    print("|---|---|---|---|")
    pertinents, atteints = [], []
    for o in range(1, 18):
        if not pertinence_den[o]:
            print(f"| {o} | n.c. | n.c. | |")
            continue
        p = pertinence_num[o] / pertinence_den[o]
        if pertinence_num[o]:
            perf = perf_num[o] / pertinence_num[o]
            pertinents.append(o)
            if perf >= 2 / 3:
                atteints.append(o)
            perf_txt = pct(perf)
        else:
            perf_txt = "n.a."
        print(f"| {o} | {pct(p)} | {perf_txt} | {', '.join(sorted(tension[o]))} |")

    print(f"\n- E3. Couverture effective : {len(atteints)}/{len(pertinents)} ODD pertinents "
          f"ont une performance d'au moins 2/3"
          + (f" ({', '.join(f'ODD {o}' for o in atteints)})" if atteints else ""))


if __name__ == "__main__":
    args = sys.argv[1:]
    odd = ROOT / "data/onr-odd.csv"
    if args[:1] == ["--odd"]:
        odd, args = Path(args[1]), args[2:]
    liens = charger_liens(odd)
    afficher_structurels(structurels(liens))
    grille = args[0] if args else ROOT / "data/gpc-onr-exemple.json"
    if grille != "-":
        evaluer(liens, grille)
