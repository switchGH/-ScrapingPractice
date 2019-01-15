"""
HTML文字列を解析する
"""
import requests, bs4
res = requests.get('https://tonari-it.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")# BeautifulSoupオブジェクトを作成
#print(soup.title)# title要素を表示
print(soup.h2)
