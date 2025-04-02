import spacy
from src import wordDict
from src import AnalysisCore as AC

nlp = spacy.load('ja_ginza')
class processer:
    text:str | list
    word = []
    sent = []
    def __init__(self, text):
        if type(text) == list:
            text = "".join(text)
        self.text = text
        doc = nlp(text)
        for s in doc.sents:
            self.sent.append(s)
        for token in doc:
            token_attrs = [token.lemma_,token.pos_,token.tag_]
            self.word.append([str(a) for a in token_attrs])

    def voclev(self):
        """
        word[2]をハイフンで切り、最初の～詞を基準に品詞ごとの重みづけをする。
        単語を難易度の辞書に突き合わせ、重みx難易度でスコア化
        全単語のスコア平均を返す
        """
        p = searchWord(self.word)
        ave = sum(p) / len(p)
        return ave
                
    def styleAnalysis(self):
        """
        各品詞の語数に対する出現頻度
        """
        NOUN = []#名詞
        AUX = []#助動詞
        ADP = []#助詞
        VERB = []#動詞
        pos = {'NOUN': NOUN,'AUX': AUX,'ADP': ADP,'VERB': VERB}
        array = [NOUN, AUX, ADP, VERB]
        for elem in self.word:
            if elem[1] in pos:
                pos[elem[1]].append(elem[0])
        rateWord = [AC.calcRate(len(self.word),len(e)) for e in array]
        return rateWord
    
    def lenSents(self):
        """
        １文の平均長さ
        """
        var = 0
        for x in self.sent:
            var += len(x)
        return f'{var / len(self.sent)}文字'

def searchWord(wordList:list):
    """
    voclevを短くまとめたかった
    """
    sb = wordDict.balance
    wd = wordDict.wordDiff
    ans = []
    for elem in wordList:
        e = [elem[0], ((elem[2].split('-')))[0]]
        b = sb[e[1]] if e[1] in sb else 0
        for x in wd:
            if (x[0] == e[0] and e[1] in x[3] and b != 0):
                ans.append(round(x[1] * b, 4))        
    return ans
