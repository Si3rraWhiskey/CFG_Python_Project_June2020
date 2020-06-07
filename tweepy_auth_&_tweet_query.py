# API keys and tokens in IDE

import tweepy as tw
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#travel, #covid, #pandemic"
date_since = "2020-06-03"
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
for tweet in tweets:
    print(tweet.text)
