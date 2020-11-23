# Excelから読み込んだ時の課題
# ・クォーテーションマークを配列に入れるときに必ず配列に組み込むようにしないと、Excelベタ打ちが実現しない
# ・Excel一行目は問題と質問の行列になっているから配列としては2行目から読み込んで配列へappendしないといけない
# ↑現段階ではクォーテーション付きのExcelとなっている
# ・ファイルのパスの位置がそれぞれのPCで必要
# ↑外部入力をターミナルでできるように案内を書いて入力してもらって、という作業が必要
# sheet名もかけるようにしておくべきかも。初期値としてはSheet1にしておいて、外部入力もできると汎用性が高まりそう



# ランダム
import random
# 休止時間の制御
from time import sleep
# Excelを読み込むのに必要
import xlrd
import pprint

# 今はパスの位置は直打ちだが、将来構想としてはターミナルで入力できるようにしたい
workbook = xlrd.open_workbook('C:\\Users\\81703\\Desktop\\qasheet.xlsx')
sheet = workbook.sheet_by_name('Sheet1')

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