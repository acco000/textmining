from mlask import MLAsk
import MeCab
import neologdn

sentiment_analyzer = MLAsk('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
results = []

results.append(sentiment_analyzer.analyze('お好み焼きは美味しい'))
results.append(sentiment_analyzer.analyze('え？あまり美味しくない'))
results.append(sentiment_analyzer.analyze('僕はお好み焼き好き'))
results.append(sentiment_analyzer.analyze('僕は嫌い'))

for each in results:
    print(each['emotion'])
