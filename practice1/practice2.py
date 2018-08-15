"""
レスポンスのエラーをチェックして安全に中止する
"""
import requests
res = requests.get('https://tonari-it.com/not_exists/') # 存在しないURLにアクセス
# print(res.status_code) # status_code属性を表示
res.raise_for_status() #ステータスコードが200番台以外なら、エラーメッセージを吐き出しスクリプトを停止
print(res.text)