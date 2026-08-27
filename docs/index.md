# GPC-ONR

**Grille de Priorisation des Cibles des Objectifs du Numérique Responsable.** Un outil libre d'auto-évaluation et de priorisation participative, publié par l'[Institut du Numérique Responsable](https://institutnr.org).

La GPC-ONR répond à une question simple et rarement traitée de front : parmi les 28 cibles des Objectifs du Numérique Responsable, **par lesquelles commencer ?** Elle croise, cible par cible, l'importance de l'enjeu pour l'organisation et sa performance actuelle, puis en déduit un ordre d'intervention.

!!! info "Ni audit, ni certification"
    L'outil ne délivre aucun score de conformité et aucun label. Il produit un classement des cibles en sept niveaux d'intervention, pour servir de support à une décision collective.

## Démarrer

1. Téléchargez le **[classeur vierge](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/raw/main/INR_GPC_ONR%20Template.xlsx)** et ouvrez-le avec LibreOffice Calc, Excel ou tout tableur compatible `.xlsx`. Aucune macro : rien à activer.
2. Renseignez l'onglet **Contexte** : organisation, sources d'information, analystes, date. Ce cadrage conditionne la valeur du reste.
3. Parcourez les onglets **ONR 1** à **ONR 5**. Pour chaque cible, notez l'**importance** (0 à 3) et la **performance actuelle** (1 à 4), puis documentez enjeux, forces, faiblesses et stratégies d'action.
4. Lisez les onglets de résultats : les cibles urgentes et prioritaires forment votre plan de premier rang.

!!! tip "Remplissez la grille en atelier, pas en solo"
    Un score posé par un seul service reflète le point de vue de ce service. Le **[classeur d'exemple](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/raw/main/INR_GPC_ONR%20Exemple.xlsx)** montre le niveau de détail attendu.

## Comment la priorité est calculée

Deux notes suffisent. Leur croisement donne le niveau d'intervention :

| Importance \ Performance | 1 — aucun progrès | 2 — progrès limités | 3 — progrès notables | 4 — cible atteinte |
|---|---|---|---|---|
| **3 — très importante** | 🔴 Urgente | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation |
| **2 — importante** | 🟠 Prioritaire | 🟡 Moyen terme | 🟢 Consolidation | ⚪ Non prioritaire |
| **1 — peu importante** | 🔵 Long terme | 🔵 Long terme | ⚪ Non prioritaire | ⚪ Non prioritaire |
| **0 — non pertinente** | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente | ⚫ Non pertinente |

Une cible laissée vide n'est pas classée : elle est comptée comme **non complétée**, pas comme non prioritaire. Ne pas savoir n'est pas la même chose que ne pas avoir besoin d'agir.

## Les 5 axes

| Axe | Engagement | Thème | Cibles |
|---|---|---|---|
| **ONR 1 — Sobriété** | Optimiser les outils numériques pour limiter leurs impacts et consommation | Environnement | 7 |
| **ONR 2 — Inclusion** | Développer des services numériques accessibles à toutes et tous, inclusifs et durables | Accessibilité | 4 |
| **ONR 3 — RSE** | S'engager pour des pratiques numériques éthiques et responsables | Éthique | 7 |
| **ONR 4 — Résilience et stratégie** | Aller vers un numérique responsable, indispensable à la résilience des organisations | Résilience | 4 |
| **ONR 5 — Management** | Faire les choses avec sens, en respectant et préservant les ressources qui produisent | Valeurs | 6 |

Chaque cible est présentée avec une reformulation **En clair**, en langage courant : voir **[les 28 cibles](referentiel-onr.md)**.

## Données ouvertes

Le contenu des classeurs est aussi publié en JSON et CSV, réutilisable sans tableur.

```bash
# Lister les cibles de l'axe Sobriété, en langage clair
jq -r '.axes[] | select(.numero==1) | .cibles[] | "\(.code)  \(.explication)"' data/onr-referentiel.json
```

| Fichier | Contenu |
|---|---|
| [`onr-referentiel.json`](../data/onr-referentiel.json) | Les 5 axes et 28 cibles, structurés |
| [`onr-referentiel.csv`](../data/onr-referentiel.csv) | Même contenu, tabulaire |
| [`matrice-priorisation.json`](../data/matrice-priorisation.json) | Les 16 combinaisons et leur niveau |
| [`gpc-onr-exemple.json`](../data/gpc-onr-exemple.json) | Contenu textuel du classeur d'exemple |

## Contribuer

Corrections de libellés, améliorations de la méthode, traductions et retours d'usage sont les bienvenus. Voir le **[guide de contribution](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/blob/main/CONTRIBUTING.md)** et les **[contributeurs](contributeurs.md)**.
