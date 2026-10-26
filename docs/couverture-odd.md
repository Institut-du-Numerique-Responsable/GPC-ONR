# Couverture des ODD

Comment les 32 cibles des ONR contribuent aux 17 Objectifs de développement durable (ODD) de l'Agenda 2030, et quels indicateurs suivre pour observer cette couverture.

!!! note "Proposition à valider"
    Ce rapprochement est une proposition de travail. Il repose sur un jugement d'experts et doit être relu collectivement avant tout usage public. Les données sont dans [`data/onr-odd.csv`](https://github.com/Institut-du-Numerique-Responsable/GPC-ONR/blob/main/data/onr-odd.csv).

## Méthode

Chaque cible ONR est reliée à des **cibles ODD** (par exemple `12.5`), pas seulement à des ODD. On distingue deux types de liens :

| Lien | Poids | Sens |
|---|---|---|
| Principal | 2 | La cible ONR répond directement à la cible ODD. Une seule par cible ONR. |
| Contributif | 1 | La cible ONR y contribue de façon indirecte ou partielle. |

Chaque lien du fichier de données porte une justification en une phrase.

## Tableau de correspondance

| Cible | En bref | ODD principal | ODD contributifs |
|---|---|---|---|
| `1.1` | Savoir d'où vient notre matériel, combien de temps il sert, et où il finit. | **12.2** | 12.5, 13.2, 7.3 |
| `1.2` | Garder le matériel plus longtemps, même une fois qu'il est payé. | **12.5** | 12.2, 8.4 |
| `1.3` | Faire des sites et des applications qui consomment peu et servent vraiment. | **9.4** | 12.2, 13.2 |
| `1.4` | Prendre des habitudes qui économisent le matériel, l'énergie et les fournitures. | **12.2** | 7.3, 15.2 |
| `1.5` | Ne plus jeter : réparer, réemployer, recycler. | **12.5** | 8.5, 11.6, 3.9 |
| `1.6` | Faire tourner le numérique avec de l'électricité renouvelable. | **7.2** | 13.2 |
| `1.7` | N'utiliser l'IA que si elle sert vraiment, et choisir la moins gourmande. | **12.2** | 7.3, 9.4 |
| `1.8` | Savoir ce que l'IA coûte à la planète, et le faire baisser. | **12.6** | 13.2, 6.4, 7.3 |
| `2.1` | Acheter en regardant l'impact social et écologique, pas seulement le prix. | **12.7** | 8.7, 8.8 |
| `2.2` | Faire des sites et des applications utilisables par les personnes handicapées, et mesurer où on en est. | **10.2** | 9.c, 4.5 |
| `2.3` | Faire des outils simples, faciles à utiliser, et vraiment utilisés. | **10.2** | 9.c, 4.4 |
| `2.4` | Demander leur avis aux futurs utilisateurs, et ne livrer que ce dont ils ont besoin. | **16.7** | 10.2 |
| `2.5` | S'assurer que l'IA traite tout le monde correctement. | **10.3** | 5.1, 16.b |
| `3.1` | Utiliser les données avec bon sens, en pensant aux gens et à la planète. | **12.8** | 12.2, 16.10 |
| `3.2` | Ne pas piéger l'utilisateur avec des écrans qui l'induisent en erreur. | **16.10** | 12.8, 16.3 |
| `3.3` | Ne demander que les données vraiment nécessaires. | **16.10** | 12.2 |
| `3.4` | Recruter des profils variés dans les métiers du numérique. | **10.2** | 5.5, 8.5 |
| `3.5` | Se soucier de celles et ceux qui fabriquent et font tourner le numérique. | **8.8** | 8.7, 3.4 |
| `3.6` | Se fixer des règles claires sur les données et l'IA, et les respecter. | **16.6** | 16.10, 10.3 |
| `3.7` | Mener une démarche responsable, et la faire connaître. | **12.6** | 17.17 |
| `3.8` | Prévenir qu'on parle à une machine, et garder un humain qui tranche. | **16.6** | 16.7, 16.10 |
| `4.1` | Mesurer nos impacts avec les mêmes méthodes que les autres, pour pouvoir se comparer. | **17.19** | 17.18, 12.6 |
| `4.2` | Regarder si nos services tiennent leurs promesses dans le temps, et le dire. | **16.6** | 17.19, 12.6 |
| `4.3` | Continuer d'innover, en mesurant l'impact et en le disant clairement. | **9.5** | 12.6 |
| `4.4` | Garder la maîtrise de nos données, de nos outils et de nos fournisseurs. | **9.1** | 9.b, 16.10 |
| `5.1` | Se demander à quoi sert vraiment un nouveau service, et pour qui. | **10.2** | 9.5, 1.4 |
| `5.2` | Reconnaître les initiatives internes qui améliorent le travail de tous. | **8.8** | 3.4, 17.17 |
| `5.3` | Demander leur avis aux personnes concernées avant de décider. | **17.17** | 16.7 |
| `5.4` | Laisser une organisation où celles et ceux qui suivront pourront encore agir. | **4.7** | 15.9, 13.3 |
| `5.5` | Suivre quelques indicateurs simples pour voir si on progresse. | **17.19** | 12.6, 16.6 |
| `5.6` | Proposer des améliorations, même quand elles ne sont pas numériques. | **12.2** | 9.5 |
| `5.7` | Choisir avec les équipes, pas à leur place. | **8.8** | 4.4, 16.7 |

## Indicateurs de couverture

Le script `scripts/couverture_odd.py` calcule tous les indicateurs ci-dessous :

```bash
python3 scripts/couverture_odd.py                  # grille d'exemple
python3 scripts/couverture_odd.py ma-grille.json   # votre grille
```

### Indicateurs structurels

Ils décrivent le référentiel lui-même. Ils ne changent que si le référentiel ou le rapprochement change.

| Code | Indicateur | Calcul | Valeur actuelle |
|---|---|---|---|
| S1 | Couverture des ODD | ODD reliés à au moins une cible / 17 | 15/17 (88 %), dont 8/17 (47 %) par un lien principal |
| S2 | Couverture des cibles ODD | Cibles ODD distinctes touchées / 169 | 40/169 (24 %) |
| S3 | Intensité par ODD | Somme des poids des liens (principal 2, contributif 1) | De 0 (ODD 2, 14) à 30 (ODD 12) |
| S4 | Concentration | Part des 3 ODD les plus liés ; indice de Herfindahl | 52 % ; 0,132 |
| S5 | Équilibre des piliers | Intensité par pilier de l'Agenda 2030 (5P) | Prospérité 35 %, Planète 31 %, Paix 18 %, Population 9 %, Partenariats 8 % |
| S6 | ODD orphelins | ODD sans aucun lien | ODD 2 (faim) et ODD 14 (vie aquatique) |

Ce qu'il faut en retenir :

- **Deux ODD dominent** : l'ODD 12 (consommation responsable) et l'ODD 16 (institutions) représentent 43 % de l'intensité totale. Les ODD 8, 9 et 10 suivent à égalité.
- **Le pilier « Population » est faible (9 %)** : la santé (ODD 3), l'éducation (ODD 4) et l'égalité femmes-hommes (ODD 5) ne sont traitées qu'en contribution secondaire.
- **Le climat (ODD 13) n'est jamais un lien principal**, alors qu'il est cité dans 5 cibles. Une cible dédiée aux émissions de gaz à effet de serre du numérique comblerait ce manque.
- **L'eau (ODD 6) n'apparaît qu'à travers l'IA** (cible 1.8). Pourtant, les centres de données et la fabrication des équipements en consomment beaucoup.
- Les ODD 2 et 14 restent orphelins. Ce résultat est attendu pour un référentiel numérique et ne doit pas être forcé.

### Indicateurs d'évaluation

Ils s'appliquent à une grille remplie et pondèrent chaque lien par l'importance donnée à la cible. Une cible non notée est ignorée. Un ODD dont aucune cible liée n'est notée apparaît « n.c. » (non calculé).

| Code | Indicateur | Calcul | Lecture |
|---|---|---|---|
| E1 | Pertinence de l'ODD | Σ(poids × importance) / Σ(poids × 3) | Place de l'ODD dans les priorités de l'organisation |
| E2 | Performance sur l'ODD | Σ(poids × importance × (performance − 1) / 3) / Σ(poids × importance) | 0 % = aucune cible liée atteinte, 100 % = toutes atteintes |
| E3 | Couverture effective | ODD dont la performance E2 atteint au moins 2/3 / ODD pertinents | Part des ODD où l'organisation agit déjà vraiment |
| E4 | Tension | Cibles liées au niveau « urgente » ou « prioritaire » | ODD sur lesquels porter l'effort en premier |

Suivez ces indicateurs à chaque campagne d'évaluation. La comparaison entre deux campagnes, ODD par ODD, montre où l'organisation progresse.

Sur la grille d'exemple, seules les cibles de l'axe Sobriété sont notées. Un seul des six ODD concernés (ODD 8) atteint une performance de 2/3. Les ODD 7, 12 et 13 concentrent les cibles en tension (1.1, 1.3, 1.7 et 1.8).
