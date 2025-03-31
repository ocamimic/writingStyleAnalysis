import requests
from bs4 import BeautifulSoup
import re

def prepareText(link):
    """変数のページのtab構文の中身を受け取り、各tabの中身をarrayで入手"""
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    elems = soup.select("div.yui-content > div")
    outputArray = [e.text.replace('\u3000\u3000', '\u2015\u2015') for e in elems]
    return outputArray

def calcRate(body:int, part:int):
    """第一引数に対する第二引数の割合を%で出す。"""
    rate = round((part / body) * 100, 4)
    return f'{rate}%'

def matchLen(text, target):
    """第一引数に含まれるtargetの数を返す。targetは正規表現を想定"""
    result = re.findall(target, text)
    return result

def newLines(text):
    """改行の数と空行の数を返す"""
    #new line
    nl = len(re.findall('\n', text))
    #empty line
    el = len(re.findall('(?<=\n)\n',text))
    return [nl,el]