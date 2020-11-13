from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

'''

# ↓用意されたHTML
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# ↓BeautifulSoupの初期化
soup = BeautifulSoup(html_doc, 'html.parser')



# ↓インデントをきれいにして出力
print(soup.prettify())

# 特定のタグだけ指定して抽出
print(soup.title)
print(soup.title.string)
print(soup.title.getText())

# 普通のタグ指定では最初の一つしか取れない
print(soup.a)
# 全部取るときはfind_all
print(soup.find_all("a"))

# 変数に代入してprint
testprint = soup.find_all("a")
print(testprint[0])
print(len(testprint))
j = 1
while j < 4:
    for i in testprint:
        print(str(j)+"."+ i.string)
        j += 1


# すべてのURLを取ってきて、一行ずつprint
testprint2 = soup.find_all("a")
for i in testprint2:
    print(i.get("href"))

~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ↑ここで切り分け↓
~~~~~~~~~~~~~~~~~~~~~~~~~~~

url = "https://review-of-my-life.blogspot.com/"
response = requests.get(url)
print(response.text)

url = "https://review-of-my-life.blogspot.com/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
print(soup.prettify())
~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ↑ここで切り分け↓
~~~~~~~~~~~~~~~~~~~~~~~~~~~
testprint3 = soup.find_all("a")
for i in testprint3:
    print(i.string)
print("↑ここで切り分け↓")
for i in testprint3:
    print(i.get("href"))

~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ↑ここで切り分け↓
~~~~~~~~~~~~~~~~~~~~~~~~~~~
url = "https://review-of-my-life.blogspot.com/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
result = soup.find_all("h3", {"class": "post-title"})
for i in result:
    print(i.text)

url = "https://review-of-my-life.blogspot.com/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
tags = soup.find_all("h3", {"class": "post-title"})
for tag in tags:
    print (tag.a.string)
    print (tag.a.get("href"))
'''




columns = ["Name", "URL"]
df = pd.DataFrame(columns=columns)
# print(df)

se = pd.Series(['LINEから送った画像を文字起こししてくれるアプリを作るときのメモ①', 'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) # 行を作成
df = df.append(se, columns) # データフレームに行を追加
# print(df)

df1 = pd.DataFrame(columns=columns) # 列名を指定する# TODO1 以下の表のようになるように、データフレームを作成してください。
se = pd.Series(['データ解析の実務プロセス入門（あんちべ）』を読んで特に学びが多かったこと', 'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) # 行を作成
df1 = df1.append(se, columns) # データフレームに行を追加
se = pd.Series(['sqlite3覚書 データベースに接続したり、中身のテーブル確認したり', 'https://review-of-my-life.blogspot.com/2018/04/sqlite3.html'], columns) # 行を作成
df1 = df1.append(se, columns)
se = pd.Series(['LINEから送った画像を文字起こししてくれるアプリを作るときのメモ①', '	https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns) # 行を作成
df1 = df1.append(se, columns)
print(df1)






















