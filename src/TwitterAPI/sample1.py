#############################
## タイムラインを取得する
## ※自分のツイート
#############################


import json
from TwitterAPI import config
from requests_oauthlib import OAuth1Session

CK  = config.CONSUMER_KEY
CS  = config.CONSUMER_SECRET
AT  = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

# リクエストURL
# url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# パラメータ定義
params = {
    'count': 5,     # 取得数を設定
}

res = twitter.get(url, params=params)

# 正常なレスポンスの場合
if res.status_code == 200:
    # タイムラインを取得
    timelines = json.loads(res.text)
    # タイムライン分繰り返し
    for line in timelines:
        print('%s: %s' % (line['user']['name'], line['text']))
# 異常な場合
else:
    print('Failed: %d' % res.status_code)