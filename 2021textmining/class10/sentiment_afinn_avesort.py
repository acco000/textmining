from collections import Counter
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
afinn = Afinn()

for each in quotes:
    lines_each_quote.append(sent_tokenize(each))


affection_docs = []
for each in lines_each_quote:
    affection_ave = []

    for line in each:
        af_value = afinn.score(line)
        morph = nltk.word_tokenize(line)
        affection_ave.append(af_value/len(morph))

    affection_docs.append(affection_ave)

for doc_id in range(len(lines_each_quote)):
    print('\n',file_names[doc_id])
    afection_each = affection_docs[doc_id]

    print("[Positive]")
    for line_id, aff_v in sorted(enumerate(afection_each), key=lambda x: x[1], reverse=True)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)

    print("[Negative]")
    for line_id, aff_v in sorted(enumerate(afection_each), key=lambda x: x[1], reverse=False)[:3]:
        print(lines_each_quote[doc_id][line_id], aff_v)
