import spacy
#sampleText = '\nLunaticという語に象徴されるように、月は人を狂わせる。ならば、私にとって彼女は月である。\n夜闇や寒さがそうさせるのか、人々は太陽を追い求める。明るく暖かいあの球は、遠い国では口説き文句に使われる。なるほど、ならば彼女は太陽だ。\n全てと同格でありながら何よりも貴い。彼女は、まさしく私の全てだった。\n\n\n全てを失ったとき、人には何が残るのだろう。私には記憶と身体が残っているが、人間はどうなんだろうか。\n両手に残った脈拍を頬で感じながら、そうぼんやりと考えた。力無く寝転がった彼女が私と同じ"物"になっていることは、もはや疑いようの無い事実である。\n尊属殺とかロボット法三原則とか、きっとこのあたりで裁かれる。どれだけ人間らしくなっても、人工物であることには変わりないのだから。\n――逃げてしまおうか。\nそんな思いつきが、まるで彼女の命令のように身体を満たした。\n\n\n\n\n\nヒト頭脳搭載型アンドロイドを殺人・遺体損壊容疑で逮捕。当該アンドロイドは行方不明だった青山 春香氏(25)が密造したものであり、事故で死亡していた青山氏の妹、雪美氏の脳が使用されていることが確認されている。\nこの事件の反響は大きく、ヒト頭脳搭載型アンドロイドの倫理的問題点が再度議論の的に……\n\n'
sampleText = 'brown fox jumps over the lazy dog.'
nlp = spacy.load('ja_ginza')
 
doc = nlp(sampleText)
#これで文に分ける
sentence = [s.text for s in doc.sents]
print(sentence)

attrs_list = []
for token in doc:
    token_attrs = [
        token.lemma_,  # 基本形
        token.pos_,  # 品詞
        token.tag_,  # 品詞詳細
    ]
    attrs_list.append([str(a) for a in token_attrs])
print(attrs_list)