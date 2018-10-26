import requests
import sys

print(('うまるを知りたいですか？＞はい'))
title = '干物妹!うまるちゃん'

url = 'https://ja.wikipedia.org/w/api.php'

api_params1 = {
    'action':'query',
    'titles':title,
    'prop':'categories',
    'format':'json'
}

api_params2 = {
    'action':'query',
    'titles':title,
    'prop':'revisions',
    'rvprop':'content',
    'format':'xmlfm'
}

categories = requests.get(url, params = api_params1).json()
page_id = categories['query']['pages']

if '-1' in page_id:
    print('該当するページがありません')
    sys.exit()
else:
    id = list(page_id.keys())
    if 'categories' in categories['query']['pages'][id[0]]:
        categories = categories['query']['pages'][id[0]]['categories']
        for umr in categories:
            print(umr['title'])
    else:
        print('保存できるページを検索できませんでした')
        sys.exit()

print('うまるの情報を保存しますか？＞はい')
user_responce = 'yes'

if user_responce == 'yes':
    data = requests.get(url, params = api_params2)
    with open(title + '.html', 'w', encoding = 'utf_8') as f:
        f.write(data.text)