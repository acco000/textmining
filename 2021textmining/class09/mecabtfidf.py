from collections import Counter
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import spacy
from ginza import *
from nltk import stem
import sys
import os
import MeCab
import neologdn

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
#文書を文に分割する処理の始まり
nlp = spacy.load('ja_ginza')
lines_each_quote = []
for each in quotes:
##ここまででファイルを入力してる
    lines_each =[]
    doc = nlp(each)
    for line in doc.sents:
        lines_each.append(str(line).rstrip("\n"))
    lines_each_quote.append(lines_each)

m_neolog = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
lemma_each_sent = []

for each in lines_each_quote:
    lemma_each_quote = []

    for line in each:
        n_document = neologdn.normalize(line)
        mecab_result = m_neolog.parse(n_document)
        list_pos = mecab_result.split("\n")

        lemma_qu = []
        lemma_string = ""

        for w in list_pos:
            each_word = w.split("\t")
            if(each_word[0] != 'EOS' and each_word[0] != ''):
                feature = each_word[3].split("-")
                if(feature[0]== "名詞" and feature[1]!= "非自立") or feature[0] == "動詞" or feature[0] == "形容詞":
                    lemma_string = lemma_string + " " + each_word[2]

        lemma_each_quote.append(lemma_string)

    lemma_each_sent.append(lemma_each_quote)

lemma_each_doc = []
for each_doc in lemma_each_sent:
    doc = ""
    for sent in each_doc:
        doc = doc + sent
    lemma_each_doc.append(doc)

print(lemma_each_doc)
vectorizer = TfidfVectorizer(use_idf=True,max_df=0.3)
vectors = vectorizer.fit_transform(lemma_each_doc)
words = vectorizer.get_feature_names_out()
#print(vectors)

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

        #tf-idfが高い文のみを抽出
        doc_tfidf.append(sent_tfidf/(len(words_in_sent)))

    for imp_id, tfidf in sorted(enumerate(doc_tfidf), key=lambda x: x[1], reverse=True)[:2]:
        print(lines_each_quote[doc_id][imp_id])
