# Questions fréquentes

## Qu'est-ce que la GPC-ONR ?

La GPC-ONR est une grille de priorisation des cibles des Objectifs du Numérique Responsable. C'est un classeur tableur qui aide une organisation à évaluer collectivement, cible par cible, l'écart entre ce qui compte pour elle et ce qu'elle fait réellement, puis à en déduire un ordre d'action. L'Institut du Numérique Responsable la publie sous licence CC BY 4.0 pour les classeurs, les données et la documentation, et sous EUPL-1.2 pour les scripts.

## Que sont les Objectifs du Numérique Responsable (ONR) ?

Les ONR sont les engagements de la charte de l'Institut du Numérique Responsable, structurés en 5 axes et 32 cibles : Sobriété, Inclusion, RSE, Résilience et stratégie, Management. La liste complète figure dans le [référentiel](referentiel-onr.md).

## À qui s'adresse l'outil ?

Aux organisations de toute taille engagées ou candidates à une démarche de numérique responsable : entreprises, TPE/PME, associations, collectivités et acteurs publics. Il n'exige ni compétence technique particulière, ni travail documentaire préalable.

## Combien de temps faut-il pour remplir la grille ?

Comptez deux à trois heures seul pour un premier passage sur les 32 cibles, une demi-journée à une journée en groupe selon le nombre de participants. Vous pouvez traiter les axes séparément, en plusieurs séances. La [méthodologie](methodologie.md#organiser-un-atelier) propose un déroulé d'atelier.

## Faut-il remplir les 32 cibles ?

Non. Le classeur compte une cible non évaluée en « non complétée » et ne la classe pas. Une cible hors du périmètre de l'organisation se note avec une importance de 0, ce qui la classe en « intervention non pertinente ». Les deux cas sont distincts et se lisent différemment dans la synthèse.

## Comment le niveau de priorité est-il calculé ?

Par croisement de l'importance de la cible (0 à 3) et de son niveau actuel (1 à 4), selon une matrice fixe qui produit sept niveaux, de l'intervention urgente à l'intervention non pertinente. Le détail est dans la [méthodologie](methodologie.md), et la matrice au format machine dans [`data/matrice-priorisation.json`](../data/matrice-priorisation.json).

## Quelle différence entre le Template et l'Exemple ?

Le **Template** est le classeur vierge à utiliser. L'**Exemple** est une copie pré-remplie par une organisation fictive, fournie pour illustrer le niveau de détail attendu ; il est commenté dans [exemple-commente.md](exemple-commente.md).

## Faut-il Microsoft Excel ?

Non. Le classeur s'ouvre avec LibreOffice Calc, ONLYOFFICE, Google Sheets, Numbers ou Excel. Il ne contient pas de macro : seulement des formules et de la mise en forme conditionnelle. Le tableur recalcule les priorités à l'ouverture du fichier.

## Comment comparer deux passages ?

Enregistrez une copie du classeur à chaque passage, avec la date dans le nom du fichier, et renseignez l'onglet `Contexte` : participants et date. Comparez ensuite les indicateurs de l'onglet `Résultats synthèse` d'une copie à l'autre. Gardez si possible le même groupe : des notes données par d'autres personnes ne se comparent pas directement.

## Où trouver les libellés d'origine de la charte ?

Depuis la version 1.3.0, les classeurs formulent les cibles en langage clair. Les libellés d'origine de la charte figurent en [annexe du référentiel](referentiel-onr.md#libelles-de-la-charte) et dans le champ `libelle_charte` de [`data/onr-referentiel.json`](../data/onr-referentiel.json).

## Puis-je réutiliser ou adapter la grille ?

Oui, y compris dans un cadre commercial. Les classeurs, les données et la documentation sont sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : citez l'Institut du Numérique Responsable comme source et signalez vos modifications. Les scripts sont sous [EUPL-1.2](https://interoperable-europe.ec.europa.eu/collection/eupl/eupl-text-eupl-12) : si vous diffusez une version modifiée, diffusez-la sous la même licence.

## L'outil est-il un audit ou une certification ?

Ni l'un ni l'autre. C'est un instrument d'auto-évaluation et de dialogue interne. Il ne délivre aucun score de conformité ni label, et ne se substitue pas à une évaluation par un tiers.

## Comment citer la GPC-ONR ?

Les métadonnées de citation sont dans [`CITATION.cff`](../CITATION.cff), au format Citation File Format 1.2.0, lisible par GitHub, Zenodo et les gestionnaires de références.

## Comment contribuer ?

Voir [`CONTRIBUTING.md`](../CONTRIBUTING.md). Les contributions passent par une pull request avec commits signés (DCO, `git commit -s`).
