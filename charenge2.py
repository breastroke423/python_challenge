from bs4 import BeautifulSoup
import requests
import gspread
# ↑スプレッドシートを使うときのimport
from gspread.exceptions import *
# ↑スプレッドシート利用時のエラー内容が書いてある
from oauth2client.service_account import ServiceAccountCredentials
# ↑googleとのサービス連携のために必須
from datetime import datetime
# ↑日時処理
import sys
# ↑pythonシステムに関わる処理を行う関数

def scrape(url, worksheer):
  html = requests.get(url)
  # ↑Webページの様々なResponseオブジェクトを取得
  soup = BeautifulSoup(html.content, "html.parser")
  # html.contentとすることでWebページのHTMLを指定しています。
  # "html.parser"これによって取得したHTMLの内容をパース(htmlの構造や意味を解析してpythonで扱えるようにすること)することができるようになります
  r = next_available_row(worksheet)
  # スプレッドシートの最初の空白行の行番号を返してくれる関数。引数はシート、戻り値はGoogleスプレッドシートの行番号
  datetimestr = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
  worksheet.update_acell('A' + str(r), datetimestr)
  # シート名.update_acell(“セル”, “B”)でセルの値にBを書き込み
  worksheet.update_acell('B' + str(r), url)
  # B列のセルにurl変数に代入されたURLを書き込み
  worksheet.update_acell('C' + str(r), soup.title.get_text())
  # C列のセルにsoup.title.get_text()で得られる値を書き込み
  # soup.titleで、タグが付いたWebページのタイトルを取得
  # 取得したデータにはタグが付いていますので、その後ろに
  # .get_text()を付けることで不要なタグを取り除く
  start_ascii = 67
  # start_ascii変数に67(ASCIIコードで大文字の’C’を意味)を代入
  for i in range(1, 7):
    elems = soup.find_all('h'+ str(i))
    # HTMLのソースの中から、何か要素を探すには、soup.find_all()
    # h○という形の要素を探して取得
    # soup.find_all()でh要素のリストを取得し、elems変数に代入
    text_list = []
    for elem in elems:
      text_list.append(elem.get_text().strip())
      # .strip()を付けることで文字列の両端の不要な空白と改行コードを取り除く
      text = ','.join(text_list)
      worksheet.update_acell(chr(start_ascii + i) + str(r), text)

def next_available_row(worksheet):
  # Googleスプレッドシートの上から数えて一番始めの空の行番号を指定するための関数
  str_list = list(filter(None, worksheet.col_values(1))) # fastest
  # 空文字がある場合、除去
  return str(len(str_list) + 1)

def get_gspread_book(secret_key, book_name):
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  # scope変数に2つのAPIを記述しないとアクセストークンを3600秒毎に
  # 発行し続けなければならないので指定。
  credentials = ServiceAccountCredentials.from_json_keyfile_name(secret_key, scope)
  # 認証情報を設定。secret_keyにはダウンロードしたjsonファイルを指定
  gc = gspread.authorize(credentials)
  # 認証情報を使用して、GoogleAPIにログイン
  book = gc.open(book_name)
  return book


''' メイン処理 '''
if __name__ == '__main__':
    url = 'https://hashikake.com/scraping-python'
    print('url: ' + url + ' のTitle、hタグを抽出します。')
    secret_key = 'My Project 〇〇〇〇.json'
    book_name = 'HTMLスクレイピングテスト'
    sheet_name = 'シート1'
    try:
        sheet = get_gspread_book(secret_key, book_name).worksheet(sheet_name)
    except SpreadsheetNotFound:
        print('Spreadsheet: ' + book_name + 'が見つかりませんでした')
        sys.exit()
    except WorksheetNotFound:
        print('Worksheet: ' + sheet_name + 'が見つかりませんでした')
        sys.exit()
    scrape(url, sheet)
    print('処理が完了しました。')














