import requests,bs4

url = 'https://ja.wikipedia.org/wiki/Python'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")

index = soup.select('#toc')

for i in index:
    print(i.getText())