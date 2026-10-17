# Méthodologie de la GPC-ONR

Comment remplir la Grille de Priorisation des Cibles des Objectifs du Numérique Responsable, et comment sont calculés les niveaux de priorité.

## Principe

La GPC-ONR ne mesure pas une conformité. Elle croise deux jugements portés collectivement sur chacune des 32 cibles des ONR :

1. **l'importance** de la cible pour l'organisation ;
2. **le niveau actuel** atteint par l'organisation sur cette cible (sa performance actuelle).

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

Onglets `ONR 1` à `ONR 5`, une ligne par cible. Vous saisissez dans les cellules jaunes ; une bulle d'aide rappelle l'échelle quand vous sélectionnez une cellule de note. Faites défiler vers la droite pour atteindre la colonne des actions.

![Onglet ONR 1 de l'exemple rempli : notes en jaune, niveaux de priorité colorés et actions proposées](assets/capture-onr1.webp){ loading=lazy }

Colonnes à remplir :

| Colonne | Contenu | Type |
|---|---|---|
| Avantages possibles et risques | Ce que la cible peut apporter, et ce qui peut mal tourner | Texte |
| Importance | Note de 0 à 3 | **Saisie** |
| Niveau actuel | Note de 1 à 4 (performance actuelle) | **Saisie** |
| Ce qui est déjà fait et ce qui justifie la note | Mesures en place, telles que les participants les connaissent | Texte |
| Compétences nécessaires | Équipe à mobiliser, de 1 à 4 (voir l'échelle ci-dessous) | **Saisie** |
| Points forts et points faibles | Analyse interne | Texte |
| Niveau de priorité | Résultat | *Calculé* |
| Actions proposées pour atteindre la cible | Pistes concrètes, attribuables | Texte |

Les colonnes texte forment le volet SWOT : les avantages possibles et les risques couvrent l'externe (opportunités, menaces), les points forts et points faibles l'interne.

### 3. Échelles de notation

**Importance** : à quel point la cible compte pour l'organisation.

| Note | Signification |
|---|---|
| 3 | Très importante |
| 2 | Importante |
| 1 | Peu importante |
| 0 | Non applicable : la cible ne concerne pas l'organisation. Le niveau actuel peut alors rester vide. |

**Niveau actuel** : où en est l'organisation sur cette cible.

| Note | Signification |
|---|---|
| 4 | Atteinte |
| 3 | En voie d'être atteinte |
| 2 | Atteinte en partie |
| 1 | Pas du tout atteinte |

**Compétences nécessaires** : qui doit agir pour faire avancer la cible.

| Note | Équipe à mobiliser |
|---|---|
| 1 | L'équipe numérique responsable (NR) ou RSE seule |
| 2 | L'équipe NR / RSE avec la direction informatique (DSI) |
| 3 | L'équipe NR / RSE avec une équipe hors DSI (achats, RH, communication…) |
| 4 | Une intervention extérieure |

Cette note ne change pas le niveau de priorité. Elle sert à répartir le travail : l'onglet de synthèse compte, pour les cibles urgentes et prioritaires, combien relèvent de chaque équipe.

Une cible non évaluée (importance ou niveau actuel manquant) reste sans priorité : la synthèse la compte en « non complétée », jamais en priorité basse. Vous distinguez ainsi ce que vous n'avez pas encore documenté de ce qui ne demande aucune action.

### 4. Lire la matrice de priorisation

Le classeur calcule une clé `importance × 10 + performance`, puis affecte un niveau d'intervention :

| Importance \ Niveau actuel | 1 : pas du tout atteinte | 2 : atteinte en partie | 3 : en voie d'être atteinte | 4 : atteinte |
|---|---|---|---|---|
| **3 : très importante** | Intervention urgente | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation |
| **2 : importante** | Intervention prioritaire | Intervention à moyen terme | Intervention de consolidation | Intervention non prioritaire |
| **1 : peu importante** | Intervention à long terme | Intervention à long terme | Intervention non prioritaire | Intervention non prioritaire |
| **0 : non applicable** | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente | Intervention non pertinente |

Les sept niveaux, du plus au moins pressant :

| Valeur | Niveau | Lecture |
|---|---|---|
| 6 | Intervention urgente | Cible très importante et pas du tout atteinte |
| 5 | Intervention prioritaire | Écart fort entre l'enjeu et l'état réel |
| 4 | Intervention à moyen terme | Dynamique engagée, à poursuivre |
| 3 | Intervention à long terme | Enjeu réel mais différable |
| 2 | Intervention de consolidation | Acquis à sécuriser dans la durée |
| 1 | Intervention non prioritaire | Ni enjeu fort ni retard |
| 0 | Intervention non pertinente | Cible hors périmètre de l'organisation |

Version machine de cette matrice : [`data/matrice-priorisation.json`](../data/matrice-priorisation.json).

### 5. Exploiter les résultats

L'onglet **`Résultats synthèse`** se lit de haut en bas :

1. **Indicateurs clés** : cibles à évaluer et évaluées, part évaluée, nombre de cibles urgentes ou prioritaires, part des cibles atteintes, part des priorités qui ont une action proposée.
2. **Comparaison des cinq ONR** : les mêmes indicateurs axe par axe, pour voir où l'évaluation avance et où se concentrent les urgences.
3. **Où concentrer les efforts ?** : deux graphiques, la part des cibles évaluées et le nombre de cibles urgentes et prioritaires par ONR.
4. **Comprendre les notes et les besoins** : la répartition des cibles par importance et niveau actuel, et les équipes à mobiliser pour les priorités.
5. **Informations à compléter** : les cibles sans note, les notes hors échelle, les notes sans justification, les priorités sans compétences ou sans action proposée. Commencez par là avant de présenter les résultats.
6. **Cibles à traiter en premier** : les dix premières priorités, avec un extrait de l'action proposée.

![Haut de l'onglet Résultats synthèse de l'exemple : indicateurs clés, comparaison des cinq ONR et graphiques](assets/capture-synthese.webp){ loading=lazy width=627 }

L'onglet **`Résultats détaillés`** reprend les 32 cibles sur une seule page, avec toutes les colonnes : c'est la liste complète au-delà des dix premières priorités.

Les taux portent sur les cibles applicables évaluées. Une action proposée ne signifie pas qu'elle a été réalisée.

Les cibles classées « urgente » et « prioritaire » forment votre plan d'action de premier rang, et leurs colonnes « Actions proposées pour atteindre la cible » en donnent le contenu.

## Conditions de validité

L'atelier ne demande aucune preuve documentaire. Les notes reposent sur ce que savent les personnes interrogées, et la maturité se lit dans la progression entre deux passages.

- **Deux façons de jouer.** Seul, pour un premier repérage rapide, ou en intelligence collective avec les métiers, l'IT, les achats et la direction. Les deux se complètent : le passage solo prépare la séance de groupe.
- **L'itération.** Une grille remplie une fois donne une photo. Rejouez l'exercice à intervalle régulier avec le même groupe : c'est l'écart entre deux éditions qui mesure la maturité, pas la valeur absolue d'une note.
- **Le groupe interrogé.** Renseignez dans l'onglet `Contexte` qui a répondu. Un score donné par l'IT seule et un score donné par un panel transverse ne se lisent pas de la même manière.

La colonne « Ce qui est déjà fait et ce qui justifie la note » sert à écrire ce que les participants savent des mesures déjà en place. Elle explique la note aux personnes qui reliront la grille plus tard, y compris à vous-même au passage suivant.

## Organiser un atelier

Prévoyez une demi-journée pour un premier passage collectif sur les 32 cibles, à 5 à 8 personnes.

| Temps | Étape | Conseil |
|---|---|---|
| Avant | Remplir l'onglet `Contexte` ; faire un passage solo | Le passage solo repère les cibles qui feront débat |
| 15 min | Présenter l'outil et les échelles | Montrez la [vidéo de démonstration](presentation.html) |
| 2 h 30 | Noter les 32 cibles, axe par axe | Notez d'abord l'importance de toutes les cibles d'un axe, puis leur niveau actuel ; écrivez la justification au fil de l'eau |
| 30 min | Lire l'onglet de synthèse | Traitez d'abord le bloc « Informations à compléter » |
| 15 min | Attribuer les actions des cibles urgentes | Une personne responsable et une échéance par action |

En cas de désaccord sur une note, écrivez les deux points de vue dans la justification : ils nourriront le passage suivant.

## Voir aussi

- [Référentiel des 32 cibles ONR](referentiel-onr.md)
- [Exemple commenté](exemple-commente.md)
- [Questions fréquentes](faq.md)
