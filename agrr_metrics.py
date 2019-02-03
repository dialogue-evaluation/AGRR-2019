
# coding: utf-8

# python3 evaluate.py --lemmas correct_file test_file
# 
# For the binary presence-absence classification for each sentence all the output lines except the first one are ignored. For gap resolution task lines corresponding to cR1, cR2, R1, R2 are ignored. For the full annotation task all output lines are evaluated.
# The main metric for binary classification task would be standard f-measure. 
# 
# Gapping element annotations would be measured by symbol-wise f-measure. E. g. if the gold standard offset for certain gapping element is 10:15 and the prediction is 8:14, we have 4 true positive chars, 1 false negative char and 2 false positive chars and the resulting f-measure equals 0.727.

# In[64]:


import sys
import getopt
import numpy as np
import pandas as pd


def help_message():
    print("Использование: python3 evaluate.py [-b|--binary, -r|--resolution] corr_file test_file")
    print("Каждая строка в csv файлах  имеет вид")
    print("Текст<TAB>0 или 1<TAB>cV<TAB>cR1<TAB>cR2<TAB>V<TAB>R1<>R2")
    print("Если вы выполняете задание только по бинарной классификации, ")
    print("Все колонки после class можно оставить пустыми")
    print("Если вы выполняете задание только по gap resolution, ")
    print("укажите -r ")

SHORT_OPTS, LONG_OPTS = "brhd:", ["binary",'resolution', "help", "dump-incorrect="]




# binary classification
def binary_metrics(y_true, y_pred):
    true_pos,false_pos,false_neg = 0,0,0
    for i in range(len(y_true)):
        if y_true[i] == 1 == y_pred[i]:
            true_pos += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            false_neg += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            false_pos += 1
    precision = true_pos/(true_pos + false_pos)
    recall = true_pos/(true_pos + false_neg)
    f1_score = 2*(precision*recall)/(precision + recall)
    return {'f1-score':f1_score, 'precision':precision,
             'recall':recall}


def symbol_wize(y_true1, y_pred1):
    
    if y_true1 == y_pred1:
        return 1
    
    y_true = set(range(int(y_true1.split(':')[0]),int(y_true1.split(':')[1])))
    y_pred = set(range(int(y_pred1.split(':')[0]),int(y_pred1.split(':')[1])))
    true_pos = y_true.intersection(y_pred)
    false_neg = y_true.difference(y_pred)
    false_pos = y_pred.difference(y_true)
    precision = len(true_pos)/(len(true_pos) + len(false_pos))
    recall = len(true_pos)/(len(true_pos) + len(false_neg))
    f1_score = 2*(precision*recall)/(precision + recall)
    return f1_score


def get_rank(gold_class, real_class, gold_span, real_span):
    if gold_class == real_class == 1:
        return symbol_wize(gold_span, real_span)
    elif gold_class == real_class == 0:
        return 1
    else:
        return 0


# full annotation metrics
def gapping_metrics(gold_data, real_data, resolution):

    binary_quality = binary_metrics(gold_data['class'], real_data['class'])
    f1_scores = [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['cV'], real_data.iloc[i]['cV']) for i in range(len(gold_data)) ] +\
    [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['V'], real_data.iloc[i]['V']) for i in range(len(gold_data)) ]
    if resolution:
        f1_scores += [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['cR1'], real_data.iloc[i]['cR1']) for i in range(len(gold_data)) ] +\
        [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['cR2'], real_data.iloc[i]['cR2']) for i in range(len(gold_data)) ]  +\
        [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['R1'], real_data.iloc[i]['R1']) for i in range(len(gold_data)) ]  +\
        [get_rank(gold_data.iloc[i]['class'], real_data.iloc[i]['class'], gold_data.iloc[i]['R2'], real_data.iloc[i]['R2']) for i in range(len(gold_data)) ] 
    sw_quality = np.mean(f1_scores)
    return {'classification_quality':binary_quality['f1-score'], 'symbol-wise_quality':sw_quality}



def read_df(filename):
    df = pd.read_csv(filename, sep='\t')
    df = df.fillna(0)
    return df



if __name__ == "__main__":
    binary, resolution, dump_file = False, False, None
    opts, args = getopt.getopt(sys.argv[1:], SHORT_OPTS, LONG_OPTS)
    for opt, val in opts:
        if opt in ["-b", "--binary"]:
            binary = True
        if opt in ["-r", "--resolution"]:
            resolution = True
        if opt in ["-h", "--help"]:
            help_message()
            sys.exit(1)
        if opt in ["-d", "--dump-incorrect"]:
            dump_file = val
    if len(args) != 2:
        sys.exit("Usage: python3 evaluate.py [-b|--binary, -r|--resolution] corr_file.csv test_file.csv")
    corr_file, test_file = args
    corr_sents, test_sents = read_df(corr_file), read_df(test_file)
    if binary:
        quality = binary_metrics(corr_sents['class'], test_sents['class'])
    else:
        quality = gapping_metrics(corr_sents, test_sents, resolution)
    
    if binary:
        print('Binary classification quality (f1-score): ' + quality['f1_score'] )
        print('Other metrics: ' + '\n Precision: ' + quality['precision'] + '\n Recall: ' + quality['recall'])
        
    else:
        print('Binary classification quality (f1-score): ' + quality['classification_quality'] )
        print('Gapping resolution quality (symbol-wise f-measure): ' + quality['symbol-wise_quality'])
