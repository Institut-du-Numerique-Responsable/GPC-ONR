# Méthodologie de la GPC-ONR

Comment remplir la Grille de Priorisation des Cibles des Objectifs du Numérique Responsable, et comment sont calculés les niveaux de priorité.

## Principe

La GPC-ONR ne mesure pas une conformité. Elle croise deux jugements portés collectivement sur chacune des 32 cibles des ONR :

1. **l'importance** de la cible pour l'organisation ;
2. **la performance actuelle** de l'organisation sur cette cible.

Le classeur croise les deux notes et en déduit un **niveau de priorité d'intervention**. Vous vous en servez autant pour structurer la discussion que pour bâtir le plan d'action.

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

Notez surtout qui répond et à quelle date : c'est ce qui rend deux passages comparables.

### 2. Évaluer chaque cible

Onglets `ONR 1` à `ONR 5`, une ligne par cible. Colonnes à remplir :

| Colonne | Contenu | Type |
|---|---|---|
| Enjeux | Opportunités et menaces liées à la cible | Texte |
| Importance de la cible | Note de 0 à 3 | **Saisie** |
| Performance actuelle | Note de 1 à 4 | **Saisie** |
| Documentation de la performance | Ce qui est déjà en place, tel que les participants le connaissent | Texte |
| Compétences | Disponibilité des compétences internes ou externes | Note |
| Forces et faiblesses | Analyse interne | Texte |
| Niveau de priorité | Résultat | *Calculé* |
| Stratégies d'action | Pistes concrètes pour atteindre la cible | Texte |

Les colonnes texte forment le volet SWOT : les enjeux couvrent l'externe (opportunités, menaces), les forces et faiblesses l'interne.

### 3. Échelles de notation

**Importance de la cible** : à quel point la cible compte pour l'organisation :

| Note | Signification |
|---|---|
| 3 | Très importante |
| 2 | Importante |
| 1 | Peu importante |
| 0 | Non pertinente pour l'organisation |

**Performance actuelle** : où en est l'organisation sur cette cible :

| Note | Signification |
|---|---|
| 4 | Cible atteinte ou quasi atteinte |
| 3 | Progrès notables |
| 2 | Progrès limités |
| 1 | Aucun progrès |

Une cible non évaluée (importance ou performance manquante) reste sans priorité : la synthèse la compte en « non complétée », jamais en priorité basse. Vous distinguez ainsi ce que vous n'avez pas encore documenté de ce qui ne demande aucune action.

### 4. Lire la matrice de priorisation

Le classeur calcule une clé `importance × 10 + performance`, puis affecte un niveau d'intervention :

| Importance \ Performance | 1 : aucun progrès | 2 : progrès limités | 3 : progrès notables | 4 : cible atteinte |
|---|---|---|---|---|
| **3 : très importante** | Intervention urgente | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation |
| **2 : importante** | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation | Intervention non prioritaire |
| **1 : peu importante** | Intervention à long terme | Intervention à long terme | Intervention non prioritaire | Intervention non prioritaire |
| **0 : non pertinente** | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente |

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

- **`Résultats détaillés`**, répartition des cibles par niveau d'intervention, axe par axe.
- **`Résultats synthèse`**, vue consolidée des 32 cibles sur les 5 thèmes (Environnement, Accessibilité, Éthique, Résilience, Valeurs), avec le nombre de cibles non complétées, urgentes, prioritaires, à moyen terme et à long terme. Six graphiques accompagnent le tableau, à droite des données : un diagramme en barres pour l'ensemble des 32 cibles, puis un camembert par ONR, qui montre comment les cibles de l'axe se répartissent entre les sept niveaux d'intervention.

Les cibles classées « urgente » et « prioritaire » forment votre plan d'action de premier rang, et leurs colonnes « Stratégies d'action » en donnent le contenu.

## Conditions de validité

L'atelier ne demande aucune preuve documentaire. Les notes reposent sur ce que savent les personnes interrogées, et la maturité se lit dans la progression entre deux passages.

- **Deux façons de jouer.** Seul, pour un premier repérage rapide, ou en intelligence collective avec les métiers, l'IT, les achats et la direction. Les deux se complètent : le passage solo prépare la séance de groupe.
- **L'itération.** Une grille remplie une fois donne une photo. Rejouez l'exercice à intervalle régulier avec le même groupe : c'est l'écart entre deux éditions qui mesure la maturité, pas la valeur absolue d'une note.
- **Le groupe interrogé.** Renseignez dans l'onglet `Contexte` qui a répondu. Un score donné par l'IT seule et un score donné par un panel transverse ne se lisent pas de la même manière.

La colonne « Documentation de la performance » sert à écrire ce que les participants savent des mesures déjà en place. Elle explique la note aux personnes qui reliront la grille plus tard, y compris à vous-même au passage suivant.

## Voir aussi

- [Référentiel des 32 cibles ONR](referentiel-onr.md)
- [Exemple commenté](exemple-commente.md)
- [Questions fréquentes](faq.md)
