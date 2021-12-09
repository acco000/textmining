import gensim.models
import scipy.spatial.distance
import scipy.cluster.hierarchy
import matplotlib
from matplotlib.pyplot import show

vocab_file="./w2v/ja.bin"
model = gensim.models.Word2Vec.load(vocab_file)

vocjp=['ビール', '日本酒', 'ウイスキー', 'テキーラ', 'ラーメン', '蕎麦', 'パスタ', 'ハンバーグ', 'カレー']
vocen=['beer', 'sake', 'whisky', 'Tequila', 'Ramen', 'Soba', 'Pasta', 'Hamburg', 'Curry']

wordvec = []
vocnewjp = []
vocnewen = []

for jpw, enw in zip(vocjp, vocen):
    try:
        wordvec.append(model.wv[jpw])
        vocnewjp.append(jpw)
        vocnewen.append(enw)

    except KeyError:
        print(jpw, "is ignored")

print(vocnewjp)
print(vocnewen)

link = scipy.cluster.hierarchy.linkage(wordvec, method='ward')
scipy.cluster.hierarchy.dendrogram(link, labels=vocnewen)
show()
