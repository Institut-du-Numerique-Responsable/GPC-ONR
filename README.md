# GPC-ONR : Grille de Priorisation des Cibles des Objectifs du Numérique Responsable

[![Licence des scripts : EUPL-1.2](https://img.shields.io/badge/Scripts-EUPL--1.2-blue.svg)](LICENSE)
[![Licence des contenus : CC BY 4.0](https://img.shields.io/badge/Contenus-CC%20BY%204.0-blue.svg)](LICENSES/CC-BY-4.0.txt)
[![Format](https://img.shields.io/badge/Format-XLSX%20%7C%20JSON%20%7C%20CSV-green.svg)](data/)
[![Institut du Numérique Responsable](https://img.shields.io/badge/Éditeur-INR-orange.svg)](https://institutnr.org/)
[![Cibles](https://img.shields.io/badge/Cibles%20ONR-32-lightgrey.svg)](docs/referentiel-onr.md)
[![Documentation](https://img.shields.io/badge/Documentation-en%20ligne-blue.svg)](https://institut-du-numerique-responsable.github.io/GPC-ONR/)
[![Dernière version](https://img.shields.io/github/v/release/Institut-du-Numerique-Responsable/GPC-ONR?label=Version)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/releases/latest)
[![Validation des données](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/actions/workflows/validate.yml/badge.svg)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/actions/workflows/validate.yml)

**Un outil libre d'auto-évaluation et de priorisation participative pour les organisations engagées dans une démarche de numérique responsable.**

La GPC-ONR aide une organisation à répondre à une question simple et rarement traitée de front : parmi les 32 cibles des Objectifs du Numérique Responsable, **par lesquelles commencer ?** Elle croise, cible par cible, l'importance de l'enjeu pour l'organisation et sa performance actuelle, et en déduit un ordre d'intervention.

C'est un support de décision collective. Aucun score de conformité, aucun label.

**Documentation en ligne : <https://institut-du-numerique-responsable.github.io/GPC-ONR/>** · **[Découvrir l'outil en une minute (vidéo)](https://institut-du-numerique-responsable.github.io/GPC-ONR/presentation.html)**

[![Onglet ONR 1 de l'exemple rempli : notes, niveaux de priorité colorés et actions proposées](docs/assets/capture-onr1.webp)](https://institut-du-numerique-responsable.github.io/GPC-ONR/presentation.html)

## Télécharger le classeur

> **[⬇ Télécharger la grille vierge (Excel)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/releases/latest/download/INR_GPC_ONR_Template.xlsx)**
>
> **[⬇ Télécharger l'exemple rempli (Excel)](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/releases/latest/download/INR_GPC_ONR_Exemple.xlsx)**

> **Nouveau : deux versions alternatives**, proposées par LaNum Pays Basque pour les publics qu'elle accompagne dans le projet européen NÉONUM : [⬇ collectivités territoriales](secteurs/collectivites/GPC-ONR_collectivites_Template.xlsx) · [⬇ enseignement supérieur et recherche](secteurs/enseignement-superieur/GPC-ONR_enseignement-superieur_Template.xlsx). [En savoir plus](#versions-sectorielles)

Rien d'autre à installer. Le fichier s'ouvre avec Excel, LibreOffice Calc, Numbers ou Google Sheets, et ne contient aucune macro. Si vous ne venez que pour la grille, vous pouvez vous arrêter ici : la suite de cette page s'adresse à celles et ceux qui veulent réutiliser les données ou contribuer.


## Sommaire

- [Télécharger le classeur](#télécharger-le-classeur)
- [Versions sectorielles](#versions-sectorielles)
- [Ce que fait l'outil](#ce-que-fait-loutil)
- [Démarrage rapide](#démarrage-rapide)
- [Les 5 axes et 32 cibles](#les-5-axes-et-32-cibles)
- [Comment la priorité est calculée](#comment-la-priorité-est-calculée)
- [Contenu du dépôt](#contenu-du-dépôt)
- [Données ouvertes](#données-ouvertes)
- [Documentation](#documentation)
- [Contribuer](#contribuer)
- [Contributeurs](#contributeurs)
- [Citer ce travail](#citer-ce-travail)
- [Licence et crédits](#licence-et-crédits)

## Versions sectorielles

<p>
  <img src="docs/assets/logo-inr.webp" alt="Institut du Numérique Responsable" height="44" align="middle">
  <img src="docs/assets/logo-lanum.svg" alt="LaNum Pays Basque" height="44" align="middle">
  <img src="docs/assets/logo-neonum.webp" alt="NÉONUM" height="64" align="middle">
</p>

**LaNum Pays Basque** propose ces deux versions alternatives de la grille. Dans le cadre du projet européen **NÉONUM**, elle accompagne des collectivités territoriales et des établissements d'enseignement supérieur et de recherche, qui ne se reconnaissent pas toujours dans un outil pensé pour l'entreprise. Pour faciliter l'adoption de la GPC-ONR dans ces contextes, LaNum a reformulé les 32 cibles dans leur langage, ajouté des cibles propres à chaque secteur et relié chaque cible aux ODD. L'INR publie ces versions à côté de la grille commune.

| Version | Pour qui | Cibles propres au secteur | Classeur | Documentation |
|---|---|---|---|---|
| **Collectivités territoriales** | Communes, intercommunalités, départements, régions, syndicats et opérateurs publics de services numériques | Stratégie numérique responsable (loi REEN), territoire intelligent, illectronisme et médiation numérique, accessibilité des contenus et de l'accueil, données publiques ouvertes, encadrement de l'IA, mutualisation et continuité en cas de crise, civic tech et participation citoyenne | [⬇ Excel](secteurs/collectivites/GPC-ONR_collectivites_Template.xlsx) | [Page](docs/secteurs/collectivites.md) |
| **Enseignement supérieur et recherche** | Universités, écoles, organismes et laboratoires de recherche, CROUS | Sobriété du calcul et du stockage de recherche, égalité d'accès des étudiants, science ouverte, plan de transition et label DD&RS, formation à la transition écologique | [⬇ Excel](secteurs/enseignement-superieur/GPC-ONR_enseignement-superieur_Template.xlsx) | [Page](docs/secteurs/enseignement-superieur.md) |

Ce qui change par rapport à la grille commune :

- **Les 32 cibles gardent leur code et leur sens.** Leur formulation et leurs exemples parlent le langage du secteur : habitants, agents et élus d'un côté ; étudiants, enseignants et chercheurs de l'autre. Les résultats restent comparables avec la grille commune.
- **Des cibles propres au secteur** s'ajoutent (8 pour les collectivités, 5 pour l'enseignement supérieur), dans la feuille « Cibles métier » du classeur. Elles ont leur propre calcul de priorité, mais n'apparaissent pas dans les feuilles de résultats.
- **Chaque cible est reliée aux Objectifs de développement durable (ODD).** Beaucoup de collectivités et d'établissements travaillent déjà avec les ODD : la grille s'appuie sur ce qu'ils connaissent. Voir [Couverture des ODD](docs/couverture-odd.md).

Ces versions sont des **versions de travail**, à relire avec des personnes de chaque secteur. Vos retours sont les bienvenus en [issue](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/issues). Pour modifier une version ou en créer une autre, voir [secteurs/README.md](secteurs/README.md).

## Ce que fait l'outil

| Usage | Description |
|---|---|
| **État des lieux** | Recenser ce qui est déjà en place, tel que le connaissent les personnes interrogées |
| **Support de discussion** | Faire dialoguer métiers, IT, achats et direction sur une base commune |
| **Priorisation** | Classer les cibles en 7 niveaux d'intervention, de l'urgent au non pertinent |
| **Analyse SWOT** | Documenter enjeux externes (opportunités, menaces) et internes (forces, faiblesses) |
| **Plan d'action** | Formuler, pour chaque cible, des stratégies concrètes attribuables |

## Démarrage rapide

1. Ouvrez le classeur téléchargé ci-dessus avec Excel, LibreOffice Calc ou tout tableur compatible `.xlsx`. Aucune macro n'est utilisée : rien à activer.
2. Renseignez l'onglet **`Contexte`** : organisation, participants, date. C'est ce qui rendra vos passages successifs comparables.
3. Parcourez les onglets **`ONR 1`** à **`ONR 5`**. Pour chaque cible, notez l'**importance** (0–3) et la **performance actuelle** (1–4), puis décrivez les avantages et les risques, ce qui est déjà fait, les points forts et faibles, et les actions proposées.
4. Lisez les onglets **`Résultats détaillés`** et **`Résultats synthèse`** : les cibles urgentes et prioritaires forment votre plan de premier rang.

> [!TIP]
> Jouez la grille seul pour un premier repérage, puis en groupe. La maturité se lit dans l'écart entre deux passages, pas dans la valeur absolue d'une note. Consultez **`INR_GPC_ONR Exemple.xlsx`** pour voir le niveau de détail attendu.

## Les 5 axes et 32 cibles

| Axe | Engagement | Thème | Cibles |
|---|---|---|---|
| **ONR 1 : Sobriété** | Utiliser les outils numériques pour consommer moins de ressources et réduire leurs effets sur l’environnement | Environnement | 8 |
| **ONR 2 : Inclusion** | Développer des services numériques durables que toutes et tous peuvent utiliser | Accessibilité | 5 |
| **ONR 3 : RSE** | Utiliser le numérique de façon éthique et responsable | Éthique | 8 |
| **ONR 4 : Résilience et stratégie** | Utiliser le numérique responsable pour aider l’organisation à faire face aux difficultés et à s’adapter | Résilience | 4 |
| **ONR 5 : Management** | Donner du sens au travail et préserver les personnes et les ressources nécessaires à nos activités | Valeurs | 7 |

Le détail des 32 cibles est disponible en texte intégral : **[docs/referentiel-onr.md](docs/referentiel-onr.md)**. Les cibles y sont formulées en langage clair, avec un résumé **En bref** et, en annexe, les libellés d'origine de la charte.

Ces objectifs sont issus de la charte de l'[Institut du Numérique Responsable](https://institutnr.org/), qui formalise les engagements pris par une organisation (entreprise, association, TPE/PME, acteur public) sur les impacts environnementaux, sociaux et éthiques du numérique.

## Comment la priorité est calculée

Deux notes suffisent. L'**importance de la cible** pour l'organisation (0 à 3) et sa **performance actuelle** (1 à 4). Leur croisement donne le niveau d'intervention :

| Importance \ Niveau actuel | 1 : pas du tout atteinte | 2 : atteinte en partie | 3 : en voie d'être atteinte | 4 : atteinte |
|---|---|---|---|---|
| **3 : très importante** | 🔴 Urgente | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation |
| **2 : importante** | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation | ⚪ Non prioritaire |
| **1 : peu importante** | 🔵 Long terme | 🔵 Long terme | ⚪ Non prioritaire | ⚪ Non prioritaire |
| **0 : non applicable** | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente |

Une cible laissée vide compte comme **non complétée**, jamais comme non prioritaire. Vous saurez ainsi ce qu'il reste à documenter.

Méthode complète, échelles détaillées et conditions de validité : **[docs/methodologie.md](docs/methodologie.md)**.

## Contenu du dépôt

```
GPC-ONR/
├── INR_GPC_ONR Template.xlsx            Classeur vierge à utiliser
├── INR_GPC_ONR Exemple.xlsx             Classeur pré-rempli, illustratif
├── docs/                                Source du site public
│   ├── index.md                         Accueil
│   ├── referentiel-onr.md               Les 32 cibles en langage clair, libellés de la charte en annexe
│   ├── methodologie.md                  Déroulé, échelles, matrice de priorisation
│   ├── exemple-commente.md              Lecture commentée du classeur d'exemple
│   ├── faq.md                           Questions fréquentes
│   ├── couverture-odd.md                Rapprochement cibles-ODD et indicateurs de couverture
│   └── secteurs/                        Pages des versions sectorielles (générées)
│   └── contributeurs.md                 Crédits
├── data/
│   ├── onr-referentiel.json             Axes, cibles et explications, structurés
│   ├── onr-referentiel.csv              Même contenu, tabulaire
│   ├── matrice-priorisation.json        Les 16 combinaisons et leur niveau
│   ├── onr-odd.csv                      Liens cibles-ODD (principal, contributif) et justifications
│   └── gpc-onr-exemple.json             Contenu textuel du classeur d'exemple
├── secteurs/                            Versions sectorielles avec LaNum (voir secteurs/README.md)
│   ├── logos/                           Logos des co-éditeurs insérés dans les classeurs
│   ├── collectivites/                   referentiel.json (source), CSV et classeur générés
│   └── enseignement-superieur/          referentiel.json (source), CSV et classeur générés
├── scripts/
│   ├── validate_data.py                 Contrôle de cohérence des données
│   ├── couverture_odd.py                Indicateurs de couverture des ODD
│   └── build_secteurs.py                Génère CSV, classeurs et pages des versions sectorielles
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
├── LICENSE                              Licence des scripts (EUPL-1.2)
└── LICENSES/                            Textes des licences (EUPL-1.2, CC BY 4.0, MIT historique)
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
| [Référentiel ONR](docs/referentiel-onr.md) | Les 5 axes et l'intégralité des 32 cibles |
| [Méthodologie](docs/methodologie.md) | Comment remplir la grille et lire les résultats |
| [Exemple commenté](docs/exemple-commente.md) | Cas fictif détaillé, cible par cible |
| [FAQ](docs/faq.md) | Périmètre, durée, public, différence template/exemple |
| [Couverture des ODD](docs/couverture-odd.md) | Liens entre cibles et ODD, indicateurs de couverture |
| [Collectivités territoriales](docs/secteurs/collectivites.md) | Version sectorielle : cibles reformulées et cibles métier |
| [Enseignement supérieur et recherche](docs/secteurs/enseignement-superieur.md) | Version sectorielle : cibles reformulées et cibles métier |
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

> Institut du Numérique Responsable, *GPC-ONR : Grille de priorisation des cibles des Objectifs du Numérique Responsable*, 2026. Licences EUPL-1.2 et CC BY 4.0. <https://github.com/Institut-du-Numerique-Responsable/GPC-ONR>

## Licence et crédits

Publié par l'**[Institut du Numérique Responsable](https://institutnr.org/)** sous deux licences ouvertes européennes :

| Éléments | Licence | Ce qu'elle vous permet |
|---|---|---|
| Classeurs `.xlsx`, données de `data/`, documentation, vidéo et captures | [CC BY 4.0](LICENSES/CC-BY-4.0.txt), licence de réutilisation de la Commission européenne | Utiliser, adapter et partager, y compris dans un cadre commercial, en citant l'INR comme source |
| Scripts (`scripts/`), workflows, page `presentation.html` | [EUPL-1.2](LICENSE), licence publique de l'Union européenne | Utiliser, modifier et redistribuer, y compris dans un cadre commercial ; les versions modifiées que vous distribuez restent sous EUPL-1.2 ou une licence compatible |

L'EUPL-1.2 existe dans les 24 langues officielles de l'Union, toutes de même valeur : [version française](https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12). Les versions publiées jusqu'à la 1.3.0 restent disponibles sous licence MIT ([texte](LICENSES/MIT-historique.txt)).

L'INR est une association qui fédère organisations publiques et privées autour de la réduction des impacts environnementaux, sociaux et économiques du numérique.

### Contributeurs

| Contributeur | Rôle |
|---|---|
| **Vincent Courboulay** | Institut du Numérique Responsable |
| **Benjamin Duthil** | Institut du Numérique Responsable |
| **Nathalie Sauzeau** | Institut du Numérique Responsable |
| **Guillaume Gallon** | Institut du Numérique Responsable |

Versions alternatives pour les collectivités territoriales et pour l'enseignement supérieur et la recherche : proposées par **LaNum Pays Basque** dans le cadre du projet européen **NÉONUM**, et co-éditées avec l'INR.

<p>
  <img src="docs/assets/logo-inr.webp" alt="Institut du Numérique Responsable" height="44" align="middle">
  <img src="docs/assets/logo-lanum.svg" alt="LaNum Pays Basque" height="44" align="middle">
  <img src="docs/assets/logo-neonum.webp" alt="NÉONUM" height="64" align="middle">
</p>

Liste détaillée : [CONTRIBUTORS.md](CONTRIBUTORS.md). Métadonnées citables : [`CITATION.cff`](CITATION.cff).

---

<sub>Mots-clés : numérique responsable · Green IT · sobriété numérique · éco-conception · priorisation · auto-évaluation · maturité · RSE numérique · accessibilité · GR491 · RGESN · ODD · INR</sub>
