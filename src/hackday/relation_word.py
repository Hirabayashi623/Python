from hackday import morphological as split
from collections import OrderedDict
from hackday import twitter
import re

if __name__ == '__main__':
    wordcount = {}

    # twitterから関連ツイートを検索
    tweets = twitter.search('乃木坂', count=100, type='recent')

    for tweet in tweets:
#         print(tweet)
        words = split.split(tweet, filter='9')
        for word in words:
            # 数字だけ、英字だけは除外
            word = re.sub(r'^[0-9０-９a-zA-Z]+$', "", word)
            if len(word) > 0:
                wordcount.setdefault(word, 0)
                wordcount[word] += 1

    results = OrderedDict()
    for k, v in wordcount.items():
        results.setdefault(v, '')
        results[v] = results[v] + ',' + k

    for k,v in results.items():
        print(k, ' -> ', v)
