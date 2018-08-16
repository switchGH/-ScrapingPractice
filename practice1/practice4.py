"""
特定のタグの要素を取得する
"""
import requests, bs4
res = requests.get('https://tonari-it.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
elems = soup.select("h2") # セレクタで指定した条件にマッチした要素を全て取得
for elem in elems:
    print(elem)
