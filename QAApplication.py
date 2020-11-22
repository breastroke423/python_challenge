# ランダムをインポート
import random
from time import sleep


# 問題文一覧を作成
qArray = [
    "1・OS",
    "2・アプリケーション（アプリケーションソフト）",
    "3・CPU",
    "4・HDD",
    "5・メモリ",
    "6・マザーボード",
    "7・BIOS",
    "8・ドライバ",
    "9・フォルダ（ディレクトリ）",
    "10・GUI",
    "11・CUI",
    "12・ビット",
    "13・バイト",
    "14・ダウンロード",
    "15・インストール"
]




# 答えがそれに対応して一覧としてある
aArray = [
    "1/ コンピューターを動かすためのソフトウェアのこと.コンピューター全体を管理、制御し、人が使えるようにする役割",
    "2/ OS上にインストールして利用するソフトウェア全般のことを意味する言葉.何らかの作業をするためのソフトウェア",
    "3/ Central Processing Unitの略.マウス、キーボード、ハードディスク、メモリー、周辺機器などからデータを受け取り、コンピューターでは 制御・演算を担当",
    "4/ パソコンのデータを保存する部品.補助記憶を担当.データを保管する本棚のように考えらる",
    "5/ メモリは作業デスクのように考えられており、パソコンが処理を実行する際に時に開いて作業のできるソフトの最大値を示します.大きく分けてと読み書き両方できるRAM（ラム）と読み出し専用のROM.",
    "6/ PCはいくつかの部品で構成されており、それぞれの役割や機能のパーツ間の橋渡しをする役割.",
    "7/ パソコンの電源が入って最初に動く、主にハードウェアを制御するプログラムのこと",
    "8/ 内蔵の機器 デバイス、周辺機器などを使用できるようにする橋渡しの役割をするソフトウェアのこと。動作させるためのファイル。デバイスドライバ",
    "9/ ファイルを整理したり、分類したりができる保管場所",
    "10/ マウスや指などでポチポチ操作できる画面のこと。Graphical User Interface（グラフィカル・ユーザ・インターフェイス）",
    "11/ すべての操作をキーボードだけでペチペチやる画面のこと。Character User Interface（キャラクタ・ユーザ・インターフェイス。",
    "12/ 情報の基本単位（英語版）である。二進数の1桁のこと。コンピュータの世界における「0か1が入る箱」の数を表す単位",
    "13/ 8ビットのこと。2進数で8桁の数を表すことができる情報量。ビットが8つ入る大きさの箱の数を表す単位",
    "14/ 他のパソコンやサーバなど別の場所にあるファイルをネットワーク経由で自分のパソコンさんに持ってくる",
    "15/ （ソフトを中に入れて）パソコンやソフトを使えるように準備すること"
]

# ランダムな数字を生成
# num = random.randint(0,int(len(qArray)))
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

# # # 問題文がランダムで出てきます
# print(qArray[int(num)])


# # # 7秒後答えが自動で出てきます
# i = 5
# while i >= 0:
#     print(i)
#     sleep(1)
#     i -= 1

# print(aArray[int(num)])
