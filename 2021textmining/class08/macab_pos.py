import MeCab
#import neologdn

m_neolog = MeCab.Tagger("-Ochasen")
mecab_result = m_neolog.parse('高槻駅からバスに乗って高槻キャ-----ンパスまでは30分程度かかります。')
#n_document = neologdn.normalize(u'高槻駅からバスに乗って高槻キャーーーンパスまでは30分程度かかります。')
#mecab_result = m_neolog.parse(n_document)
list_pos = mecab_result.split("\n")

for w in list_pos:
    #print(list_pos)
    each_word = w.split("\t")
    if(each_word[0] != 'EOS' and each_word[0] != ''):
            print(each_word[1])
