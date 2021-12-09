import gensim
import sys

args = sys.argv
word = args[1]

vocab_file="./w2v/ja.bin"

model = gensim.models.Word2Vec.load(vocab_file)

try:
    wvec = model.wv[word]
    print(wvec)
except:
    print("The word" +word+ "is not in the library")
