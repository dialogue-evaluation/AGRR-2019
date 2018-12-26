# AGGR-2019
## AGRR: Automatic Gapping Resolution for Russian

Gapping is the most common type of ellipsis, concerning such examples as 
“Ей он рассказывает одно, а нам — совершенно другое”, 
“Кто любит арбуз, а кто - свиной хрящик”,
“Дайте мне две пятерки, а я вам десятку”


### Motivation

The aim of this task is to challenge non-trivial linguistic phenomenon, gapping, that occurs in coordinated structures and elides a repeated predicate, typically from the second clause. Besides the adversity of the construction itself, the phenomenon is naturally rare, which results in lack of training data. During the last two years Gapping has received considerable attention  ( S Schuster, M Lamm, CD Manning 2017; K Droganova, D Zeman  2017; K Droganova et al 2018, S Schuster, J Nivre, CD Manning 2018; Nivre et al 2018). Unfortunately, research was mainly held on insufficient data not exceeding several hundreds of sentences so far. 
This campaign is a pilot event for gapping resolution task for Russian held for the first time.


### Examples (data)

Participants will be provided with a corpus of several thousands of examples coming from texts of different genres, such as news, fiction, and science. Each sentence will be annotated as follows: two remnants R1 and R2, their correlates in the antecedent clause cR1 and cR2, the position of the elided  predicate V and the head of the correspondent predicate cV.
 
 
(1) Тогда я  cV[принял cV]  cR1[ее cR1]  cR2[за итальянку cR2], а  R1[его R1]   V[]  cR2[за шведа cR2].
 
(2) cR1[Иногда cR1] они  cV[развиваются cV]  cR2[слабо cR2],  R1[иногда R1] - V[]   R2[очень сильно R2], и тогда они начинают влиять на ход сюжета, а не наоборот.
 

### Task Description

* **Binary presence-absence classification.** For every sentence decide  if there is a gapping construction in it
* **Gap resolution.** Predict the position of the elided predicate and the correspondent predicate in the antecedent clause
* **Full annotation.** In the clause with the gap predict the linear position of the elided predicate and annotate its remnants. In the antecedent clause find the constituencies that correspond the remnants and the predicate that corresponds the gap


### Data formats and metrics

Input data consists of sentences without any additional markup (raw texts).
For each sentence output should contain 7 lines. 
First line should have 0 or 1 in it, depending on presence of gapping construction in the sentence.
Other output lines should contain gapping element name (cV, cR1, cR2, V, R1, R2), tab symbol and char offsets (first symbol in each sentence has offset 0 1) for annotation borders (two numbers separated by colon (:) symbol) for each gapping element. If the provided sentence lacks certain gapping element, the corresponding line should not contain any symbols after tab.

Example:
Input
Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента, упал с 1980 до 1986 года на 2,8 процента, в 1987 году - на 4,4 процента и в 1989 году - на 0,5 процента.

`
Output
1  
cV  166:170  
cR1  171:190  
cR2  191:206  
V 222:222 254:254   
R1  208:219 240:251  
R2  222:237 254:269  
`

Such output corresponds to the following markup:

Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента,  cV[упал cV]  cR1[с 1980 до 1986 года cR1]  cR2[на 2,8 процента cR2],  V[] R1[в 1987 году R1] -  R2[на 4,4 процента R2] и  V[] R1[в 1989 году R1] -  R2[на 0,5 процента R2].


For the binary presence-absence classification for each sentence all the output lines except the first one are ignored.
For gap resolution task lines corresponding to cR1, cR2, R1, R2 are ignored.
For the full annotation task all output lines are evaluated.

The main metric for binary classification task would be standard f-measure.
Gapping element annotations would be measured by symbol-wise f-measure. E. g. if the gold standard offset for certain gapping element is 10:15 and the prediction is 8:14, we have 4 true positive chars, 1 false negative char and 2 false positive chars and the resulting f-measure equals 0.727.

### AGRR tracks

The following tracks are offered to participants:
**1. Closed track** – open source track. 
convenient for research groups and student teams
Participants are allowed to train their models only on open-access data (open source dictionaries, word embeddings, open parsing systems, etc)
To verify the results, participants should place their code and the model on github, so that it would be publicly available - both for organizers and other teams.

**2. Open track** - no restriction on data and systems used.
recommended for industrial participants, representing their products
Track participants are allowed to bring any data for learning beyond the data provided and use their own commercial programs. Github sharing is not required. 

Participants are welcome to submit their models to both of the tracks under specified constraints.
