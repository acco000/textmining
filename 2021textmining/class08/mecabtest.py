import MeCab
import neologdn

m_neolog = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
mecab_result = m_neolog.parse('高槻駅からバスに乗って高槻キャンパスまでは30分程度かかります。')
print(mecab_result)
