#############################
## ツイートの検索
#############################


import json
from hackday import config
from requests_oauthlib import OAuth1Session

CK  = config.CONSUMER_KEY
CS  = config.CONSUMER_SECRET
AT  = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

# リクエストURL
url = 'https://api.twitter.com/1.1/search/tweets.json'

def search(keyword, count=10, type='popular'):
    params = {
        'q'          : keyword, # 検索ワード
        'count'      : count,   # 取得する結果の数
        'lang'       : 'ja',    # 言語コード
        'result_type': type     # 取得するツイートの種類(popular:人気, recent:最新, mixed:すべて)
    }

    res = twitter.get(url, params=params)

    result = []

    # 正常なレスポンスの場合
    if res.status_code == 200:
        tweets = json.loads(res.text)
        for tweet in tweets['statuses']:
            result.append(tweet['text'])
        print(len(result),'件取得')
    # 異常な場合
    else:
        print('Failed: %d' % res.status_code)
    return result

if __name__ == '__main__':
    print(search('映画'))