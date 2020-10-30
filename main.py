import MeCab
from gensim.models import word2vec
import pprint

model = word2vec.Word2Vec.load('Please enter your Word2Vec Model Path')

def Mecab(data):
    tagger = MeCab.Tagger()
    str_output = tagger.parse(data)
    # pprint.pprint(str_output)
    return str_output

def HinsiSplit(data):
    str_list = data.split("\n")
    result = {}
    for i in str_list:
        temp = i.split("\t")
        if len(temp) >= 2:
            result[temp[0]] = temp[1].split(",")
    # pprint.pprint(result)
    return result

def SelectHinsi(data):
    result = []
    check_list = ["名詞","形容詞","動詞"]
    for key,value in data.items():
        if value[0] in check_list:
            result.append(key)
    # pprint.pprint(result)
    return result

def SadCheck(w1,w2):
    result = {"key":w1,"value":None}
    try:
        result["value"] = model.wv.similarity(w1, w2)
        # print("単語: {0} → {1}類似度：{2}".format(w1,w2,result["value"]))
    except Exception as identifier:
        print(identifier)
    return result

def main(text,word):
    data = SelectHinsi(HinsiSplit(Mecab(text)))
    result = []
    if len(data) != 0:
        for i in data:
            temp = SadCheck(i,word)
            if temp["value"] != None:
                result.append(temp)
        result = sorted(result, key=lambda x:x['value'],reverse=True)
    else:
        result.append({"key":None,"value":0})
    return result

if __name__ == "__main__":
    text = "背中の傷は剣士の恥だ" #感情分析を行う文章
    word ="嬉しい" #感情表す単語
    temp = main(text,word)
    for i in temp:
        print("単語 : {0} → {1}類似度 : {2}".format(i["key"],word,i["value"]))
    # pprint.pprint(temp)
