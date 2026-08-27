# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/). Ce projet suit le [versionnement sémantique](https://semver.org/lang/fr/).

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
