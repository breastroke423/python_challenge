import requests
from bs4 import BeautifulSoup
import re
'''
url = "https://techacademy.jp/magazine/18875"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

elems = soup.find_all("h2")

for e in elems:
    print(e)
'''

url = "https://www.yahoo.co.jp/"
res = requests.get(url)
# print(res.text[:50])

# BeautifulSoup(解析対象のHTML/XML, 利用するパーサー)
# １つ目の引数には、解析対象のHTML/XMLを渡します。
# ２つ目の引数として解析に利用するパーサー（解析器）を指定します。

# パーサー	             引数での指定方法	特徴
# Python’s html.parser	“html.parser”	  追加ライブラリが不要
# lxml’s HTML parser  	“lxml”	          高速に処理可
# lxml’s XML parser	    “xml”	          XMLに対応し、高速に処理可
# html5lib	            “html5lib”	      正しくHTML5を処理可

soup = BeautifulSoup(res.text, "html.parser")

# メソッド	 引数	            説明
# find()  	検索するHTMLタグ	引数に一致する 最初の１つの 要素を取得します。
# find_all()	検索するHTMLタグ	引数に一致する 全ての 要素を取得します。

elems = soup.find_all(href = re.compile("news.yahoo.co.jp/pickup"))
print(elems)









