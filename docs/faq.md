# Questions fréquentes

## Qu'est-ce que la GPC-ONR ?

La GPC-ONR est une grille de priorisation des cibles des Objectifs du Numérique Responsable. C'est un classeur tableur qui aide une organisation à évaluer collectivement, cible par cible, l'écart entre ce qui compte pour elle et ce qu'elle fait réellement, puis à en déduire un ordre d'action. Elle est publiée par l'Institut du Numérique Responsable sous licence MIT.

## Que sont les Objectifs du Numérique Responsable (ONR) ?

Les ONR sont les engagements de la charte de l'Institut du Numérique Responsable, structurés en 5 axes et 28 cibles : Sobriété, Inclusion, RSE, Résilience et stratégie, Management. La liste complète figure dans le [référentiel](referentiel-onr.md).

## À qui s'adresse l'outil ?

Aux organisations de toute taille engagées ou candidates à une démarche de numérique responsable : entreprises, TPE/PME, associations, collectivités et acteurs publics. Il n'exige pas de compétence technique particulière, mais suppose de réunir plusieurs services autour de la table.

## Combien de temps faut-il pour remplir la grille ?

Compter une demi-journée à une journée d'atelier pour un premier passage sur les 28 cibles, selon le nombre de participants et le niveau de documentation disponible en amont. Vous pouvez traiter les axes séparément, en plusieurs séances.

## Faut-il remplir les 28 cibles ?

Non. Le classeur compte une cible non évaluée en « non complétée » et ne la classe pas. Une cible hors du périmètre de l'organisation se note avec une importance de 0, ce qui la classe en « intervention non pertinente ». Les deux cas sont distincts et se lisent différemment dans la synthèse.

## Comment le niveau de priorité est-il calculé ?

Par croisement de l'importance de la cible (0 à 3) et de la performance actuelle (1 à 4), selon une matrice fixe qui produit sept niveaux, de l'intervention urgente à l'intervention non pertinente. Le détail est dans la [méthodologie](methodologie.md), et la matrice au format machine dans [`data/matrice-priorisation.json`](../data/matrice-priorisation.json).

## Quelle différence entre le Template et l'Exemple ?

Le **Template** est le classeur vierge à utiliser. L'**Exemple** est une copie pré-remplie par une organisation fictive, fournie pour illustrer le niveau de détail attendu ; il est commenté dans [exemple-commente.md](exemple-commente.md).

## Faut-il Microsoft Excel ?

Non. Le classeur s'ouvre avec LibreOffice Calc, Excel, ou tout tableur compatible `.xlsx`. Il ne contient pas de macro : seulement des formules et de la mise en forme conditionnelle.

## L'outil est-il un audit ou une certification ?

Ni l'un ni l'autre. C'est un instrument d'auto-évaluation et de dialogue interne. Il ne délivre aucun score de conformité ni label, et ne se substitue pas à une évaluation par un tiers.

## Comment citer la GPC-ONR ?

Les métadonnées de citation sont dans [`CITATION.cff`](../CITATION.cff), au format Citation File Format 1.2.0, lisible par GitHub, Zenodo et les gestionnaires de références.

## Comment contribuer ?

Voir [`CONTRIBUTING.md`](../CONTRIBUTING.md). Les contributions passent par une pull request avec commits signés (DCO, `git commit -s`).
