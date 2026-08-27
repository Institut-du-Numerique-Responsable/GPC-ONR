# GPC-ONR : Grille de Priorisation des Cibles des Objectifs du Numérique Responsable

[![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)
[![Format](https://img.shields.io/badge/Format-XLSX%20%7C%20JSON%20%7C%20CSV-green.svg)](data/)
[![Institut du Numérique Responsable](https://img.shields.io/badge/Éditeur-INR-orange.svg)](https://institutnr.org/)
[![Cibles](https://img.shields.io/badge/Cibles%20ONR-28-lightgrey.svg)](docs/referentiel-onr.md)
[![Documentation](https://img.shields.io/badge/Documentation-en%20ligne-blue.svg)](https://institut-du-numerique-responsable.github.io/GPC-ONR/)
[![Dernière version](https://img.shields.io/github/v/release/Institut-du-Numerique-Responsable/GPC-ONR?label=Version)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/releases/latest)
[![Validation des données](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/actions/workflows/validate.yml/badge.svg)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/actions/workflows/validate.yml)

**Un outil libre d'auto-évaluation et de priorisation participative pour les organisations engagées dans une démarche de numérique responsable.**

La GPC-ONR aide une organisation à répondre à une question simple et rarement traitée de front : parmi les 28 cibles des Objectifs du Numérique Responsable, **par lesquelles commencer ?** Elle croise, cible par cible, l'importance de l'enjeu pour l'organisation et sa performance actuelle, et en déduit un ordre d'intervention.

C'est un support de décision collective. Aucun score de conformité, aucun label.

**Documentation en ligne : <https://institut-du-numerique-responsable.github.io/GPC-ONR/>**

## Sommaire

- [Ce que fait l'outil](#ce-que-fait-loutil)
- [Démarrage rapide](#démarrage-rapide)
- [Les 5 axes et 28 cibles](#les-5-axes-et-28-cibles)
- [Comment la priorité est calculée](#comment-la-priorité-est-calculée)
- [Contenu du dépôt](#contenu-du-dépôt)
- [Données ouvertes](#données-ouvertes)
- [Documentation](#documentation)
- [Contribuer](#contribuer)
- [Contributeurs](#contributeurs)
- [Citer ce travail](#citer-ce-travail)
- [Licence et crédits](#licence-et-crédits)

## Ce que fait l'outil

| Usage | Description |
|---|---|
| **État des lieux** | Recenser ce qui est déjà fait, avec les preuves documentaires à l'appui |
| **Support de discussion** | Faire dialoguer métiers, IT, achats et direction sur une base commune |
| **Priorisation** | Classer les cibles en 7 niveaux d'intervention, de l'urgent au non pertinent |
| **Analyse SWOT** | Documenter enjeux externes (opportunités, menaces) et internes (forces, faiblesses) |
| **Plan d'action** | Formuler, pour chaque cible, des stratégies concrètes attribuables |

## Démarrage rapide

```bash
git clone https://github.com/Institut-du-Numerique-Responsable/GPC-ONR.git
cd GPC-ONR
```

1. Ouvrez **`INR_GPC_ONR Template.xlsx`** avec LibreOffice Calc, Excel ou tout tableur compatible `.xlsx`. Aucune macro n'est utilisée : rien à activer.
2. Renseignez l'onglet **`Contexte`** (organisation, sources, analystes, date). Ce cadrage conditionne la valeur du reste.
3. Parcourez les onglets **`ONR 1`** à **`ONR 5`**. Pour chaque cible, notez l'**importance** (0–3) et la **performance actuelle** (1–4), puis documentez enjeux, forces/faiblesses et stratégies d'action.
4. Lisez les onglets **`Résultats détaillés`** et **`Résultats synthèse`** : les cibles urgentes et prioritaires forment votre plan de premier rang.

> [!TIP]
> Remplissez la grille en atelier. Un score posé par un seul service reflète le point de vue de ce service. Consultez **`INR_GPC_ONR Exemple.xlsx`** pour voir le niveau de détail attendu.

## Les 5 axes et 28 cibles

| Axe | Engagement | Thème | Cibles |
|---|---|---|---|
| **ONR 1 : Sobriété** | Optimiser les outils numériques pour limiter leurs impacts et consommation | Environnement | 7 |
| **ONR 2 : Inclusion** | Développer des services numériques accessibles à toutes et tous, inclusifs et durables | Accessibilité | 4 |
| **ONR 3 : RSE** | S'engager pour des pratiques numériques éthiques et responsables | Éthique | 7 |
| **ONR 4 : Résilience et stratégie** | Aller vers un numérique responsable, indispensable à la résilience des organisations | Résilience | 4 |
| **ONR 5 : Management** | Faire les choses avec sens, en respectant et préservant les ressources qui produisent | Valeurs | 6 |

Le détail des 28 cibles est disponible en texte intégral : **[docs/referentiel-onr.md](docs/referentiel-onr.md)**. Chaque cible y est accompagnée d'une reformulation **En clair**, en langage courant, pour être comprise sans connaissance préalable du sujet.

Ces objectifs sont issus de la charte de l'[Institut du Numérique Responsable](https://institutnr.org/), qui formalise les engagements pris par une organisation (entreprise, association, TPE/PME, acteur public) sur les impacts environnementaux, sociaux et éthiques du numérique.

## Comment la priorité est calculée

Deux notes suffisent. L'**importance de la cible** pour l'organisation (0 à 3) et sa **performance actuelle** (1 à 4). Leur croisement donne le niveau d'intervention :

| Importance \ Performance | 1 : aucun progrès | 2 : progrès limités | 3 : progrès notables | 4 : cible atteinte |
|---|---|---|---|---|
| **3 : très importante** | 🔴 Urgente | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation |
| **2 : importante** | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation | ⚪ Non prioritaire |
| **1 : peu importante** | 🔵 Long terme | 🔵 Long terme | ⚪ Non prioritaire | ⚪ Non prioritaire |
| **0 : non pertinente** | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente |

Une cible laissée vide compte comme **non complétée**, jamais comme non prioritaire. Vous saurez ainsi ce qu'il reste à documenter.

Méthode complète, échelles détaillées et conditions de validité : **[docs/methodologie.md](docs/methodologie.md)**.

## Contenu du dépôt

```
GPC-ONR/
├── INR_GPC_ONR Template.xlsx            Classeur vierge à utiliser
├── INR_GPC_ONR Exemple.xlsx             Classeur pré-rempli, illustratif
├── docs/                                Source du site public
│   ├── index.md                         Accueil
│   ├── referentiel-onr.md               Les 28 cibles, avec reformulation « En clair »
│   ├── methodologie.md                  Déroulé, échelles, matrice de priorisation
│   ├── exemple-commente.md              Lecture commentée du classeur d'exemple
│   ├── faq.md                           Questions fréquentes
│   └── contributeurs.md                 Crédits
├── data/
│   ├── onr-referentiel.json             Axes, cibles et explications, structurés
│   ├── onr-referentiel.csv              Même contenu, tabulaire
│   ├── matrice-priorisation.json        Les 16 combinaisons et leur niveau
│   └── gpc-onr-exemple.json             Contenu textuel du classeur d'exemple
├── scripts/
│   └── validate_data.py                 Contrôle de cohérence des données
├── .github/
│   ├── workflows/pages.yml              Construction et publication du site
│   ├── workflows/validate.yml           Validation des données à chaque PR
│   ├── ISSUE_TEMPLATE/                  Correction, méthode, retour d'usage
│   └── PULL_REQUEST_TEMPLATE.md         Vérifications attendues
├── .github/dependabot.yml               Mise à jour mensuelle des actions et dépendances
├── .github/CODEOWNERS                   Relecteurs obligatoires du référentiel
├── mkdocs.yml                           Configuration du site
├── llms.txt                             Point d'entrée pour les assistants IA
├── CITATION.cff                         Métadonnées de citation (CFF 1.2.0)
├── CHANGELOG.md                         Journal des modifications
├── CONTRIBUTORS.md                      Contributeurs
├── CONTRIBUTING.md                      Guide de contribution et DCO
├── CODE_OF_CONDUCT.md                   Code de conduite
├── SECURITY.md                          Politique de sécurité
└── LICENSE                              Licence MIT
```

## Données ouvertes

Le contenu des classeurs est aussi publié en formats ouverts et interrogeables, pour être réutilisé sans tableur : intégration dans un autre outil, croisement avec un référentiel tiers, consultation par un assistant IA.

```bash
# Lister les cibles de l'axe Sobriété, en langage clair
jq -r '.axes[] | select(.numero==1) | .cibles[] | "\(.code)  \(.explication)"' data/onr-referentiel.json

# Retrouver le niveau d'intervention pour importance=3, performance=1
jq -r '.combinaisons[] | select(.importance==3 and .performance==1) | .niveau' data/matrice-priorisation.json
```

Ces fichiers sont dérivés des classeurs `.xlsx`, qui restent la source de référence.

## Documentation

| Document | Contenu |
|---|---|
| [Référentiel ONR](docs/referentiel-onr.md) | Les 5 axes et l'intégralité des 28 cibles |
| [Méthodologie](docs/methodologie.md) | Comment remplir la grille et lire les résultats |
| [Exemple commenté](docs/exemple-commente.md) | Cas fictif détaillé, cible par cible |
| [FAQ](docs/faq.md) | Périmètre, durée, public, différence template/exemple |
| [Contributeurs](CONTRIBUTORS.md) | Crédits et conditions d'ajout |
| [Journal des modifications](CHANGELOG.md) | Historique des versions |

## Contribuer

Les contributions sont bienvenues : correction de libellés, reformulation en langage clair, amélioration de la méthode, traduction, retours d'usage. Trois modèles d'issues sont proposés : correction de contenu, méthode, retour d'usage. Avant d'ouvrir une pull request, vérifiez la cohérence des données :

```bash
python scripts/validate_data.py
```
 Le processus et le Certificat d'Origine du Développeur (DCO) sont décrits dans **[CONTRIBUTING.md](CONTRIBUTING.md)**. Les commits doivent être signés :

```bash
git commit -s -m "Description de ma contribution"
```

Les modifications de `main` passent par une pull request : une relecture approuvée, la validation des données au vert, et l'accord d'un relecteur du référentiel pour les fichiers de `data/`, les classeurs et `docs/referentiel-onr.md`.

## Citer ce travail

Les métadonnées sont dans [`CITATION.cff`](CITATION.cff), au format Citation File Format 1.2.0, lisible par GitHub, Zenodo et les gestionnaires de références.

> Institut du Numérique Responsable, *GPC-ONR : Grille de priorisation des cibles des Objectifs du Numérique Responsable*, 2026. Licence MIT. <https://github.com/Institut-du-Numerique-Responsable/GPC-ONR>

## Licence et crédits

Publié sous [licence MIT](LICENSE) par l'**[Institut du Numérique Responsable](https://institutnr.org/)**.

L'INR est une association qui fédère organisations publiques et privées autour de la réduction des impacts environnementaux, sociaux et économiques du numérique.

### Contributeurs

| Contributeur | Rôle |
|---|---|
| **Vincent Courboulay** | Institut du Numérique Responsable |
| **Benjamin Duthil** | Institut du Numérique Responsable |
| **Nathalie Sauzeau** | Institut du Numérique Responsable |
| **Guillaume Gallon** | Institut du Numérique Responsable |

Liste détaillée : [CONTRIBUTORS.md](CONTRIBUTORS.md). Métadonnées citables : [`CITATION.cff`](CITATION.cff).

---

<sub>Mots-clés : numérique responsable · Green IT · sobriété numérique · éco-conception · priorisation · auto-évaluation · maturité · RSE numérique · accessibilité · GR491 · RGESN · ODD · INR</sub>
