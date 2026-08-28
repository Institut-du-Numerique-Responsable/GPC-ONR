# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/). Ce projet suit le [versionnement sémantique](https://semver.org/lang/fr/).

## [1.2.0] - 2026-08-28

### Reformulé (décision INR)

- `4.2` « En participant à une démarche collaborative de conception et d'évaluation des services numériques en adéquation avec les réels besoins » devient **« En évaluant nos services numériques dans la durée, et en partageant les résultats de ces évaluations »**. La formulation initiale faisait doublon avec la cible 2.4, qui porte la conception avec les utilisateurs. L'ONR 4 retrouve son sujet : mesurer, comparer, rendre compte.

## [1.1.0] - 2026-08-28

### Ajouté

- **Quatre cibles sur l'intelligence artificielle**, tirées de la charte IA de l'INR et ajoutées aux axes existants sans en retirer aucune. Le référentiel passe de 28 à 32 cibles, réparties 8/5/8/4/7.
    - `1.8` En mesurant ce que consomme l'IA, de son entraînement à son usage, et en le réduisant
    - `2.5` En vérifiant que l'IA ne discrimine personne et que ses services restent utilisables par tous
    - `3.8` En disant quand c'est une IA qui répond, en expliquant comment elle décide, et en gardant un humain aux commandes sur les sujets sensibles
    - `5.7` En décidant des usages de l'IA avec les équipes, en les formant à ses limites, et en préservant le sens de leur travail
- **Un camembert par ONR** dans l'onglet `Résultats synthèse`, à côté du diagramme d'ensemble : une part par niveau d'intervention, avec les couleurs de la matrice de priorisation.
- **Téléchargement en premier** : le README ouvre sur les deux liens de téléchargement, et la page d'accueil du site sur deux boutons. Une visiteuse qui vient chercher le classeur n'a plus à traverser la documentation ni à cloner le dépôt.
- **Cadre de contribution** : `CODEOWNERS` (relecture obligatoire des données, des classeurs et du référentiel), `dependabot.yml`, contrôle mensuel des liens, `.gitattributes`, `.gitignore`, `.editorconfig`, et protection de la branche `main`.

### Reformulé (décision INR)

- `1.2` « En permettant la durée de vie des équipements, même au-delà de leur amortissement comptable et en valorisant les gains et le ROI pour chacune des parties prenantes » devient **« En allongeant la durée d'usage des équipements, même au-delà de leur amortissement comptable »**. La formulation initiale était grammaticalement incorrecte et la mention des parties prenantes superflue.
- `1.3` devient **« En éco-concevant les services numériques, et en choisissant des technologies qui contribuent aux Objectifs de développement durable (ODD) »**. La formulation initiale ne désignait aucune action concrète.
- `2.2` devient **« En rendant nos services numériques accessibles à toutes et tous, et en mesurant leur conformité au RGAA »**. L'accompagnement des acteurs du territoire relevait de la mission d'une collectivité, pas de toutes les organisations.
- `2.4` devient **« En concevant les services avec celles et ceux qui les utiliseront, pour livrer ce dont ils ont besoin et rien de plus »**. La mention de conformité faisait doublon avec 2.2.

### Corrigé

- **Nombre de cibles par ONR** : dans `Résultats détaillés`, les cellules « Nombre de cibles » des ONR 1, 4 et 5 étaient saisies en dur avec 6, 3 et 7 au lieu de 7, 4 et 6. Le total annonçait 27 cibles au lieu de 28 et la colonne « cibles analysées » tombait à -1. Elles comptent désormais les lignes de cibles de leur axe, ce qui garde le classeur juste si une cible est ajoutée ou retirée.
- **Priorité de la cible 2.4** : la cellule ne portait aucune formule, la priorité calculée restait vide.
- **Codes des cibles de l'ONR 3** : dans `Résultats détaillés`, ils étaient figés en valeurs au lieu de suivre l'onglet de l'axe.
- **Onglet `Liste ONR`** : régénéré depuis le référentiel, il énumérait encore les 28 cibles d'origine.
- **Conditions de validité** : la documentation posait à tort la preuve écrite comme condition d'une évaluation sérieuse. L'atelier ne demande aucune évaluation documentaire. Il se joue seul puis s'itère, ou se joue en intelligence collective, et la maturité se lit dans la progression entre deux passages avec le même groupe.
- **Modèle d'issue « correction »** : une description contenant un deux-points rendait le fichier illisible par YAML, et GitHub aurait rejeté le modèle.

### Rédaction

- Documentation relue pour supprimer les tournures artificielles : tirets cadratins, oppositions binaires, formules à effet, voix passive. Les échelles et les titres d'axes utilisent le deux-points.

## [1.0.0] - 2026-08-28

Première version publiée du dépôt : classeurs, données ouvertes, documentation et site public.

### Ajouté

- **Reformulation « En clair »** des 28 cibles ONR, en langage courant, pour rendre la grille utilisable sans connaissance préalable du numérique responsable. Publiée en parallèle des libellés officiels, dans `data/onr-referentiel.json` (champ `explication`), `data/onr-referentiel.csv` (colonne `cible_explication`) et `docs/referentiel-onr.md` (colonne **En clair**).
- **Site public** construit avec MkDocs Material et publié sur GitHub Pages : <https://institut-du-numerique-responsable.github.io/GPC-ONR/>
- **Page contributeurs** (`CONTRIBUTORS.md` et page publique), avec Vincent Courboulay, Benjamin Duthil, Nathalie Sauzeau et Guillaume Gallon, également déclarés dans `CITATION.cff`.
- **Validation automatique des données** (`scripts/validate_data.py`) : 28 cibles réparties 7/4/7/4/6, cohérence JSON et CSV, 16 combinaisons de la matrice, alignement des libellés avec le classeur, non-régression des fautes corrigées. Exécutée à chaque push et pull request.
- **Modèles d'issues** (correction de contenu, méthode, retour d'usage), modèle de pull request, `CODE_OF_CONDUCT.md` et `SECURITY.md`.
- `CHANGELOG.md`.

### Modifié

- **Fautes corrigées** dans les classeurs, les données et la documentation : `vis-àvis`, `utilisatuer`, `garrantissant`, `accompagnat`, `cbile`, `partie prenantes`, accords fautifs des commentaires d'aide, `Technologie` au singulier, espaces avant ponctuation. 136 occurrences au total.
- **Classeurs renommés** sans préfixe de date : `INR_GPC_ONR Template.xlsx` et `INR_GPC_ONR Exemple.xlsx`.
- `README.md` restructuré : liens vers le site public, section contributeurs, exemples de données ouvertes mis à jour.
- `llms.txt` mis à jour pour refléter les nouveaux fichiers et le site public.

### Non modifié

Les libellés officiels des 28 cibles issus de la charte des Objectifs du Numérique Responsable restent inchangés sur le fond. Seules les fautes d'orthographe et de grammaire ont été corrigées. Toute reformulation de fond relève d'une décision de l'INR.
