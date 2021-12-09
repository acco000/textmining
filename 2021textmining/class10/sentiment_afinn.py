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

afinn = Afinn()

for each in quotes:
    lines_each_quote.append(sent_tokenize(each))

for each in lines_each_quote:
    for line in each:
        af_value = afinn.score(line)
        print(line, af_value)
