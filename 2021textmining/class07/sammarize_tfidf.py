from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
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

for each in quotes:
    lines_each_quote.append(sent_tokenize(each))



lemmatizer = stem.WordNetLemmatizer()

lemma_each_sent = []

for each in lines_each_quote:
    lemma_each_quote = []

    for line in each:
        morph_qu = nltk.word_tokenize(line)
        pos_qu = nltk.pos_tag(morph_qu)

        lemma_qu = []
        lemma_string = ""

        for word in pos_qu:
          if word[1] == "NN" or word[1] == "NNS" or \
            word[1] == "NNP" or word[1] == "NNPS" or word[1] == "RPR" or \
            word[1] == "VB" or word[1] == "VBD" or \
            word[1] == "VBG" or word[1] == "VBN" or word[1] == "VBP" or \
            word[1] == "VBZ":
                lemma_string = lemma_string + lemmatizer.lemmatize(word[0].lower()) + " "
        lemma_each_quote.append(lemma_string)

    lemma_each_sent.append(lemma_each_quote)

lemma_each_doc = []
for each_doc in lemma_each_sent:
    doc = ""
    for sent in each_doc:
        doc = doc + sent
    lemma_each_doc.append(doc)

vectorizer = TfidfVectorizer(use_idf=True, max_df=0.3)

all_vectors = vectorizer.fit_transform(lemma_each_doc)

words = vectorizer.get_feature_names()

for doc_id in range(len(lemma_each_doc)):
    content_doc = lemma_each_sent[doc_id]
    doc_tfidf = []
    print("\nThe important sentences in:", file_names[doc_id])

    for sent_id, lemma_sent in enumerate(lemma_each_sent[doc_id]):
        words_in_sent = lemma_sent.split(" ")
        sent_tfidf = 0
        #print("tf-idf for each word in sentence #", sent_id, "in Document ",doc_id)
        for a_word in words_in_sent:
                try:
                    sent_tfdif = sent_tfidf + all_vectors.toarray()[doc_id, words.index(a_word)]
                except:
                    pass

        doc_tfidf.append(sent_tfidf/(len(words_in_sent)))

    for imp_id, tfidf in sorted(enumerate(doc_tfidf), key=lambda x: x[1], reverse=True)[:2]:
        print(lines_each_quote[doc_id][imp_id])
