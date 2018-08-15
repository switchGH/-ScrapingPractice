import requests
res = requests.get('https://tonari-it.com')#Responseオブジェクト取得
# print(res.text) #text属性の表示
with open('./html/tonari-it.html','w') as file: # with構文を使いhtmlファイルを書き込むために開く
        file.write(res.text) # text属性を書き込む


