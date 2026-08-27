# Méthodologie de la GPC-ONR

Comment remplir la Grille de Priorisation des Cibles des Objectifs du Numérique Responsable, et comment sont calculés les niveaux de priorité.

## Principe

La GPC-ONR ne mesure pas une conformité. Elle croise deux jugements portés collectivement sur chacune des 28 cibles des ONR :

1. **l'importance** de la cible pour l'organisation ;
2. **la performance actuelle** de l'organisation sur cette cible.

Le croisement des deux produit automatiquement un **niveau de priorité d'intervention**. L'outil sert donc autant à structurer la discussion entre parties prenantes qu'à produire un plan d'action.

## Déroulé en 5 étapes

### 1. Renseigner le contexte

Onglet `Contexte`. Champs à documenter avant toute évaluation :

| Champ | Objet |
|---|---|
| Organisation | Entité pour laquelle la priorisation est effectuée |
| Niveau d'avancement | Maturité actuelle dans la mise en œuvre des ONR |
| Documents politiques et stratégiques | Documents existants ou en préparation facilitant l'identification des cibles prioritaires |
| Sources d'information | Sources pertinentes sur la situation vis-à-vis des cibles |
| Service responsable | Service porteur de la priorisation |
| Analystes | Noms et titres des personnes participant à l'analyse |
| Responsable | Personne responsable de l'analyse et du suivi |
| Date | Date de l'analyse |

Ce cadrage détermine la légitimité des scores : sans référence documentaire, l'évaluation reste déclarative.

### 2. Évaluer chaque cible

Onglets `ONR 1` à `ONR 5`, une ligne par cible. Colonnes à remplir :

| Colonne | Contenu | Type |
|---|---|---|
| Enjeux | Opportunités et menaces liées à la cible | Texte |
| Importance de la cible | Note de 0 à 3 | **Saisie** |
| Performance actuelle | Note de 1 à 4 | **Saisie** |
| Documentation de la performance | Mesures déjà en place, preuves | Texte |
| Compétences | Disponibilité des compétences internes ou externes | Note |
| Forces et faiblesses | Analyse interne | Texte |
| Niveau de priorité | Résultat | *Calculé* |
| Stratégies d'action | Pistes concrètes pour atteindre la cible | Texte |

Les colonnes texte (enjeux, forces/faiblesses) constituent le volet SWOT : les enjeux couvrent l'externe (opportunités, menaces), les forces et faiblesses couvrent l'interne.

### 3. Échelles de notation

**Importance de la cible** — à quel point la cible compte pour l'organisation :

| Note | Signification |
|---|---|
| 3 | Très importante |
| 2 | Importante |
| 1 | Peu importante |
| 0 | Non pertinente pour l'organisation |

**Performance actuelle** — où en est l'organisation sur cette cible :

| Note | Signification |
|---|---|
| 4 | Cible atteinte ou quasi atteinte |
| 3 | Progrès notables |
| 2 | Progrès limités |
| 1 | Aucun progrès |

Une cible non évaluée (importance ou performance manquante) reste sans priorité : elle apparaît en « non complétée » dans la synthèse, et non en priorité basse. La distinction est importante : ne pas savoir n'est pas la même chose que ne pas avoir besoin d'agir.

### 4. Lire la matrice de priorisation

Le classeur calcule une clé `importance × 10 + performance`, puis affecte un niveau d'intervention :

| Importance \ Performance | 1 — aucun progrès | 2 — progrès limités | 3 — progrès notables | 4 — cible atteinte |
|---|---|---|---|---|
| **3 — très importante** | Intervention urgente | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation |
| **2 — importante** | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation | Intervention non prioritaire |
| **1 — peu importante** | Intervention à long terme | Intervention à long terme | Intervention non prioritaire | Intervention non prioritaire |
| **0 — non pertinente** | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente |

Les sept niveaux, du plus au moins pressant :

| Valeur | Niveau | Lecture |
|---|---|---|
| 6 | Intervention urgente | Cible décisive, aucun progrès : point de rupture |
| 5 | Intervention prioritaire | Écart fort entre l'enjeu et l'état réel |
| 4 | Intervention à moyen terme | Dynamique engagée, à poursuivre |
| 3 | Intervention à long terme | Enjeu réel mais différable |
| 2 | Intervention de consolidation | Acquis à sécuriser dans la durée |
| 1 | Intervention non prioritaire | Ni enjeu fort ni retard |
| 0 | Intervention non pertinente | Cible hors périmètre de l'organisation |

Version machine de cette matrice : [`data/matrice-priorisation.json`](../data/matrice-priorisation.json).

### 5. Exploiter les résultats

- **`Résultats détaillés`** — répartition des cibles par niveau d'intervention, axe par axe.
- **`Résultats synthèse`** — vue consolidée des 28 cibles sur les 5 thèmes (Environnement, Accessibilité, Éthique, Résilience, Valeurs), avec le nombre de cibles non complétées, urgentes, prioritaires, à moyen terme et à long terme.

Les cibles classées « urgente » et « prioritaire » constituent le plan d'action de premier rang ; leurs colonnes « Stratégies d'action » en fournissent le contenu.

## Conditions de validité

L'outil produit un classement, pas une vérité. Trois conditions rendent le résultat exploitable :

- **La collégialité.** Un score posé par une seule personne reflète un point de vue de service. La grille est conçue pour être remplie en atelier, avec les métiers, l'IT, les achats et la direction.
- **La traçabilité.** La colonne « Documentation de la performance » n'est pas facultative : elle est ce qui distingue une évaluation d'une impression.
- **La répétition.** Une grille remplie une fois donne un état des lieux. Deux grilles à un an d'intervalle donnent une trajectoire.

## Voir aussi

- [Référentiel des 28 cibles ONR](referentiel-onr.md)
- [Exemple commenté](exemple-commente.md)
- [Questions fréquentes](faq.md)
