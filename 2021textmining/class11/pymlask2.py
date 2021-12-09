from mlask import MLAsk
import MeCab
import neologdn
import sys
import os
import spacy

sentiment_analyzer = MLAsk("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
results = []

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

for doc_id, each in enumerate(lines_each_quote):
    print('\n', file_names[doc_id])

    for line in each:
        sentiment = sentiment_analyzer.analyze(line)

        print('\n', sentiment['text'])

        sent_emo = sentiment['emotion']

        try:
            print("感情語: ",sent_emo.items())
        except:
            print("感情語: なし")

        try:
            print("極性: ",sentiment['orientation'])
        except:
            print("極性: なし")

        try:
            print("強度: ",sentiment['activation'])
        except:
            print("強度: なし")

        try:
            print("文の感情", sentiment['representative'])
        except:
            print("文の感情: なし")




#results.append(sentiment_analyzer.analyze('お好み焼きは美味しい'))
# results.append(sentiment_analyzer.analyze('え？あまり美味しくない'))
# results.append(sentiment_analyzer.analyze('僕はお好み焼き好き'))
# results.append(sentiment_analyzer.analyze('僕は嫌い'))

for each in results:
    print(each['emotion'])
