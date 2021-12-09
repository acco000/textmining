import gensim.models
import sys

args = sys.argv
word = args[1]

vocab_file="./w2v/ja.bin"

model = gensim.models.Word2Vec.load(vocab_file)

try:
    similar_words = model.wv.most_similar(positive=[word], topn=5)
    for each in similar_words:
        sim_w = each[0]
        sim_v = each[1]
        print("Similar word: ",sim_w)
        print("The similarity: ",'{:.4f}'.format(sim_v))
except:
    print("The query" + word + "is not in the library")
