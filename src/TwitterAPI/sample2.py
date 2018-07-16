#############################
## 新規ツイートする
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
url = 'https://api.twitter.com/1.1/statuses/update.json'

# ツイート内容を入力
print('内容を入力してください')
tweet = input('>> ')
print('**********************************')

params = {
    'status': tweet,
}

res = twitter.post(url, params=params)

# 正常なレスポンスの場合
if res.status_code == 200:
    print('success !!!')
# 異常な場合
else:
    print('Failed: %d' % res.status_code)