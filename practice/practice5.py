"""
特定のclass属性を持つ要素を抽出する
"""
import requests, bs4
res = requests.get('https://tonari-it.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('.entry-title.entry-title-link')
for elem in elems:
    print(elem)