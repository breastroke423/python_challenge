# Excelから読み込んだ時の課題

# ランダム
import random
# 休止時間の制御
from time import sleep
# Excelを読み込むのに必要
import xlrd
import pprint

# ファイルパス指定して作ってもらったどのファイルでも可能に
inputFilePath = input('Excelファイルのパスを入力してください (Win：ファイル上で「Shift ＋ 右クリック から パスのコピー」/Mac：「⌘+option+C」): ')
# ファイルパスコピーしてそのままペーストで使える

workbook = xlrd.open_workbook(inputFilePath.strip('"'))
inputSheetName = input('使用するシートを入力してください ： ')
sheet = workbook.sheet_by_name(inputSheetName)

# 問題文一覧を作成
qArray = sheet.col_values(0)
aArray = sheet.col_values(1)

# ランダムな数字を生成
numList = list(range(int(len(qArray))))
random.shuffle(numList)

for num in numList:
    i = 5
    print(" ")
    print(" ")
    print(" ")
    print("＝＝＝＝問題＝＝＝＝")
    print(qArray[num])
    print("＝＝＝＝＝＝＝＝＝＝")
    print("カウント")
    while i >= 0:
        print(i)
        sleep(1)
        i -= 1
    print("＝＝＝＝答え＝＝＝＝")
    print(aArray[num])
    print("＝＝＝＝＝＝＝＝＝＝")
    sleep(2)

print("END")