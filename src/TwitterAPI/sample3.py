#############################
## ツイートの検索
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
url = 'https://api.twitter.com/1.1/search/tweets.json'

# ツイート内容を入力
print('何を調べますか？')
keyword = input('>> ')
print('**********************************')

params = {
    'q'          : keyword,       # 検索ワード
    'count'      : 10,            # 取得する結果の数
    # 'geocode': "35.794507,139.790788,10",  # 緯度、経度、半径
    'lang'       : 'ja',    # 言語コード
    # 'locale': 'ja',
    'result_type': 'popular'    # 取得するツイートの種類(popular:人気, recent:最新, mixed:すべて)
    # until, since_id, max_id, include_entities
}

res = twitter.get(url, params=params)

# 正常なレスポンスの場合
if res.status_code == 200:
    tweets = json.loads(res.text)
    for tweet in tweets['statuses']:
        # print('%s[%s] %s' % (tweet['created_at'], tweet['user']['name'], tweet['text']))
        print(tweet['text'])
# 異常な場合
else:
    print('Failed: %d' % res.status_code)