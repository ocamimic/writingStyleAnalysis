import ginza
import getTexts

URL = "http://ocamiscanvas.wikidot.com/writing-style-analysis"
Texts = getTexts.prepareText(link=URL)
print(Texts)