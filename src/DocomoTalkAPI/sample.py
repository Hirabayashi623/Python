# -*- coding: utf-8 -*-

import requests
import json
import types

KEY = '645252716873364874763134784e5245395275303339387a6274464e6b3854593934416264754e414f6f41'

#エンドポイントの設定
endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'

url = endpoint.replace('REGISTER_KEY', KEY)
print('URL:', url)

#1回目の会話の入力
utt_content = input('>>')

payload = {'utt' : utt_content, 'context': ''}
print('payload:', payload)
headers = {'Content-type': 'application/json'}

#送信
r = requests.post(url, data=json.dumps(payload), headers=headers)
data = r.json()
print(data)
#jsonの解析
response = data['utt']
context = data['context']

#表示
print("response: %s" %(response))

#2回目以降の会話(Ctrl+Cで終了)
while True:
    utt_content = input('>>')
    payload['utt'] = utt_content
    payload['context'] = data['context']

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    response = data['utt']
    context = data['context']

    print("response: %s" %(response))