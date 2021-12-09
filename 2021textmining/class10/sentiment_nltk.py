from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
from afinn import Afinn
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk import stem
import sys
import os

args = sys.argv
dir_path = args[1]

files = os.listdir(dir_path)

quotes = []
file_names = []

for each in files:
  if each.endswith('.txt') == True:
    file_names.append(each)

    file_path = dir_path + each

    rfp = open(file_path, "r")
    each_quote = rfp.read()
    rfp.close()
    quotes.append(each_quote)


lines_each_quote = []

#ここから１０
vader_analyzer = SentimentIntensityAnalyzer()

for each in quotes:
    lines_each_quote.append(sent_tokenize(each))


affection_doc_c =[]
affection_doc_p =[]
affection_doc_n =[]
affection_doc_f =[]


#affection_docs = []
for each in lines_each_quote:
    #affection_ave = []
    line_c = []
    line_p = []
    line_n = []
    line_f = []

    for line in each:
        af_value = vader_analyzer.polarity_scores(line)
        line_c.append(af_value["compound"])
        line_n.append(af_value["neg"])
        line_f.append(af_value["neu"])
        line_p.append(af_value["pos"])

    affection_doc_c.append(line_c)
    affection_doc_n.append(line_n)
    affection_doc_f.append(line_f)
    affection_doc_p.append(line_p)

for doc_id in range(len(lines_each_quote)):
    print('\n',file_names[doc_id])
    compound_each = affection_doc_c[doc_id]
    neg_each = affection_doc_n[doc_id]
    flat_each = affection_doc_f[doc_id]
    pos_each = affection_doc_p[doc_id]

    print("[Compound]")
    for line_id, aff_v in sorted(enumerate(compound_each), key=lambda x: x[1], reverse=True)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)

    print("[Positive]")
    for line_id, aff_v in sorted(enumerate(pos_each), key=lambda x: x[1], reverse=True)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)

    print("[Flat]")
    for line_id, aff_v in sorted(enumerate(flat_each), key=lambda x: x[1], reverse=True)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)

    print("[Negative]")
    for line_id, aff_v in sorted(enumerate(neg_each), key=lambda x: x[1], reverse=True)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)
