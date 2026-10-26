# Versions sectorielles

Versions de la GPC-ONR adaptées à un secteur, co-éditées par l'Institut du Numérique Responsable (INR) et LaNum Pays Basque, dans le cadre du projet NÉONUM.

| Secteur | Classeur | Page |
|---|---|---|
| Collectivités territoriales | [GPC-ONR_collectivites_Template.xlsx](collectivites/GPC-ONR_collectivites_Template.xlsx) | [docs/secteurs/collectivites.md](../docs/secteurs/collectivites.md) |
| Enseignement supérieur et recherche | [GPC-ONR_enseignement-superieur_Template.xlsx](enseignement-superieur/GPC-ONR_enseignement-superieur_Template.xlsx) | [docs/secteurs/enseignement-superieur.md](../docs/secteurs/enseignement-superieur.md) |

Les classeurs de la grille commune (`INR_GPC_ONR Template.xlsx`, `INR_GPC_ONR Exemple.xlsx`) restent à la racine du dépôt. Des liens et des QR codes publiés pointent vers eux : ne pas les déplacer.

## Organisation

```
secteurs/
├── logos/                     Logos des co-éditeurs insérés dans les classeurs (PNG)
└── <secteur>/
    ├── referentiel.json       SOURCE : seul fichier à modifier à la main
    ├── onr-referentiel.csv    généré : 32 cibles reformulées + cibles métier
    ├── onr-odd.csv            généré : liens ODD communs + liens des cibles métier
    └── GPC-ONR_<secteur>_Template.xlsx   généré à partir du classeur INR
```

Les pages `docs/secteurs/<secteur>.md` sont générées elles aussi.

## Modifier un secteur

1. Modifier `secteurs/<secteur>/referentiel.json`.
2. Lancer `python3 scripts/build_secteurs.py`.
3. Commiter la source et les fichiers générés ensemble. Le CI refuse une demande de fusion dont les fichiers générés sont obsolètes.

## Format de `referentiel.json`

- `variante` : identifiant, nom, titre, public visé et cadre réglementaire du secteur.
- `cibles` : les 32 cibles de la grille commune, avec les mêmes codes. Chacune porte un `libelle` (reformulation), un `libelle_charte` (forme « En … ») et une `explication` (en bref). Le sens reste celui de la cible commune, pour que les résultats restent comparables.
- `cibles_metier` : 5 cibles propres au secteur, une par axe. Les codes commencent par une lettre (`C.1`, `E.1`…).
- `odd_metier` : liens ODD des cibles métier, au format `[cible, odd, cible_odd, "principal" | "contributif", justification]`. Chaque cible métier a un seul lien principal.

Les cibles communes reprennent les liens ODD de `data/onr-odd.csv`.

## Ajouter un secteur

Créer `secteurs/<nouveau-secteur>/referentiel.json` sur le modèle d'un secteur existant, puis lancer le script. Ajouter ensuite la page dans la navigation de `mkdocs.yml` et une ligne dans le tableau ci-dessus.

## Limite connue

Dans le classeur, les cibles métier sont dans la feuille « Cibles métier », avec leur propre calcul de priorité. Elles ne sont pas reprises dans les feuilles `Résultats détaillés` et `Résultats synthèse`.
