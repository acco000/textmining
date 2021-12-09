#すべての事象は整理分類予測のどれかに落とし込める
#どういうデータを学習するかにより、予測は変わる
import gensim.models
import sys

vocab_file="./w2v/ja.bin"

model = gensim.models.Word2Vec.load(vocab_file)

try:
    plus_words = ["女性","王"]
    minus_words = ["男性"]
    similar_words = model.wv.most_similar(positive=plus_words, negative=minus_words, topn=5)

    print("足すのは:")
    for each in plus_words:
        print(each)

    print("引くのは:")
    for each in minus_words:
        print(each)

    print("計算結果は:")
    for each in similar_words:
        sim_w = each[0]
        sim_v = each[1]
        print("Similar word: The similarity = ",sim_w,":"'{:.4f}'.format(sim_v))
except:
    print("The word(s) in the calcuration is not in the vocabulary")
