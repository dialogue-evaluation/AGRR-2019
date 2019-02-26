

# AGRR-2019

## Test data released
We are happy to announce that test data (test.csv) has been released and uploaded to this repo.

### Test data format description
The test data comprises sentences from different genres: news, fiction, social media, technical texts and other sources.
The format of the test data is as follows:
* Columns are tab-separated;
* Rows are separated by newline;
* Every row consists of a sentence text, a class label (1 - has gapping, 0 - doesn't have gapping) and symbol spans of the categories (cV, cR1, cR2, V, R1, R2) if the class label equals 1.

Please make sure to keep this data format in your submissions while filling the empty columns with class labels and span symbol offsets (in case your system does participate in tasks predicting annotations).


One row as it appears in test data uploaded to github:

Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента, упал с 1980 до 1986 года на 2,8 процента, в 1987 году - на 4,4 процента и в 1989 году - на 0,5 процента.\t\t\t\t\t\t\t\n

One row as it is supposed to look like in your submission:

Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента, упал с 1980 до 1986 года на 2,8 процента, в 1987 году - на 4,4 процента и в 1989 году - на 0,5 процента.\t1\t166:170\t171:190\t191:206\t222:222 254:254\t208:219 240:251\t222:237 254:269\n

Columns containing spans can be skipped in case your system does not participate in the tasks predicting annotations.

### Submission process description

All contest rules announced previously remain unchanged.

The test data submission deadline is **18:00 February 23rd (GMT+3) (this Saturday).**

Please send your team’s submission to dialogueeval2019@gmail.com.
Please ensure that your email contains your team’s name and information concerning the tasks (binary presence-absence classification, gap resolution and/or full annotation) and tracks (open track or closed track) you wish to participate in.


### Dates and links
|              | Date           |
| :---         |           ---: |
| [Registration](https://docs.google.com/forms/d/e/1FAIpQLSeiW0h6hvG-4iQC0dOXqyv8Pz-wG6xOhSSbFoIi9L7qsAtWbg/viewform) due   | Jan 25th 2019  | 
| Release of the Training Data     | Jan 26th 2019  |
| Release of the Test Data     | Feb 20th 2019  |
| Systems submissions due     | **18:00 February 23rd (GMT+3)**  |
| Final results from organizers     | Mar 5th 2019   |

## AGRR: Automatic Gapping Resolution for Russian

Gapping is the most common type of ellipsis, concerning such examples as  
 - _Ей он рассказывает одно, а нам — совершенно другое_  
 - _Кто любит арбуз, а кто — свиной хрящик_  
 - _Дайте мне две пятерки, а я вам десятку_


### Motivation

The aim of this task is to challenge non-trivial linguistic phenomenon, gapping, that occurs in coordinated structures and elides a repeated predicate, typically from the second clause. Besides the adversity of the construction itself, the phenomenon is naturally rare, which results in lack of training data. During the last two years Gapping has received considerable attention  ( [S Schuster, M Lamm, CD Manning 2017](http://www.aclweb.org/anthology/W17-0416); [K Droganova, D Zeman  2017](http://www.aclweb.org/anthology/W17-0406); [K Droganova et al 2018](http://www.aclweb.org/anthology/W18-6006); [S Schuster, J Nivre, CD Manning 2018](https://arxiv.org/pdf/1804.06922.pdf); [Nivre et al 2018](http://www.aclweb.org/anthology/W18-6012)).
Unfortunately, research was mainly held on insufficient data not exceeding several hundreds of sentences so far. 
This campaign is a pilot event for gapping resolution task for Russian held for the first time.


### Examples (data)

Participants will be provided with a corpus of several thousands of examples coming from texts of different genres, such as news, fiction, and science. Each sentence will be annotated as follows: two remnants **R1** and **R2**, their correlates in the antecedent clause **cR1** and **cR2**, the position of the elided  predicate **V** and the head of the correspondent predicate **cV**.
 - _Тогда я  **cV[** принял **cV]**  **cR1[** ее **cR1]**  **cR2[** за итальянку **cR2]**, а  **R1[** его **R1]**   **V[]**  **cR2[** за шведа **cR2]**._
 - _**cR1[** Иногда **cR1]** они  **cV[** развиваются **cV]**  **cR2[** слабо **cR2]**,  **R1[** иногда **R1]** — **V[]**   **R2[** очень сильно **R2]**, и тогда они начинают влиять на ход сюжета, а не наоборот._
 

### Task Description

**1. Binary presence-absence classification**    
For every sentence decide if there is a gapping construction in it.  

**2. Gap resolution**  
Predict the position of the elided predicate and the correspondent predicate in the antecedent clause.  

**3. Full annotation**  
In the clause with the gap predict the linear position of the elided predicate and annotate its remnants. In the antecedent clause find the constituents that correspond the remnants and the predicate that corresponds the gap.  


### Data formats and metrics

Input data consists of sentences without any additional markup (raw texts).For each sentence output should contain 7 columns. First column should have 0 or 1 in it, depending on presence of gapping construction in the sentence.
Other output cells separated with tab symbol correspond gapping element names (**cV**, **cR1**, **cR2**, **V**, **R1**, **R2**) and should contain char offsets (first symbol in each sentence has offset 0 1) for annotation borders (two numbers separated by colon (:) symbol) for each gapping element. If the provided sentence lacks certain gapping element, the corresponding cell should not contain any symbols. Here is the example
 
**Input**  
>Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента, упал с 1980 до 1986 года на 2,8 процента, в 1987 году - на 4,4 процента и в 1989 году - на 0,5 процента.

**Output**  

| class | cV  | cR1  | cR2 | V | R1  | R2  |
| :---  | :---  | :---  | :---  | :---  | :---  | :---  |
| 1| 166:170 | 171:190 | 191:206  | 222:222 254:254  | 208:219 240:251 | 222:237 254:269 |


Such output corresponds to the following markup:

 - _Аналогичным образом, среднегодовой прирост ВВП на душу населения, который в странах, расположенных к югу от Сахары, составлял в период с 1965 по 1973 год 3 процента,  **cV[** упал **cV]**  **cR1[** с 1980 до 1986 года **cR1]**  **cR2[** на 2,8 процента **cR2]**,   **R1[** в 1987 году **R1]** — **V[]** **R2[** на 4,4 процента **R2]** и  **R1[** в 1989 году **R1]** —  **V[]** **R2[** на 0,5 процента **R2]**._


For the binary presence-absence classification for each sentence all the output cells except the first one are ignored.
For gap resolution task cells in columns **cR1**, **cR2**, **R1**, **R2** are ignored.
For the full annotation task all output cells are evaluated.

The main metric for binary classification task would be standard f-measure.
Gapping element annotations would be measured by symbol-wise f-measure. E. g. if the gold standard offset for certain gapping element is 10:15 and the prediction is 8:14, we have 4 true positive chars, 1 false negative char and 2 false positive chars and the resulting f-measure equals 0.727.

### AGRR tracks

The following tracks are offered to participants:

**1. Closed track** – open source track  
`convenient for research groups and student teams`  
Participants are allowed to train their models only on open-access data (open source dictionaries, word embeddings, open parsing systems, etc). To verify the results, participants should place their code and the model on github, so that it would be publicly available - both for organizers and other teams.

**2. Open track** - no restriction on data and systems used  
`recommended for industrial participants, representing their products`  
Track participants are allowed to bring any data for learning beyond the data provided and use their own commercial programs. Github sharing is not required. 

Participants are welcome to submit their models to both of the tracks under specified constraints.
