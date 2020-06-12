# API keys and tokens in IDE

import tweepy as tw
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

search_words = 'travel' or 'holiday' or 'travel abroad' and 'covid' or 'pandemic' or 'covid-19' or 'rona' or 'coronavirus'
lang='en'
result_type='mixed'
## geocode = "51.5074,0.1278,100km" - geocode currently doesn't work - causes no tweets to be returned. this value here should work for London
# Maybe take out these variables for running them for different months

january_tweets = tw.Cursor(api.search,
              q=search_words,
              # geocode=geocode,
              lang=lang,
              result_type=result_type,
              since="2020-01-02",
              max="2020-02-01").items(200)

for tweet in january_tweets:
    print(tweet.text)

february_tweets = tw.Cursor(api.search,
              q=search_words,
              # geocode=geocode,
              lang=lang,
              result_type=result_type,
              since="2020-02-02",
              max="2020-03-01").items(200)

for tweet in february_tweets:
    print(tweet.text)

march_tweets = tw.Cursor(api.search,
              q=search_words,
              # geocode=geocode,
              lang=lang,
              result_type=result_type,
              since="2020-03-02",
              max="2020-04-01").items(200)

for tweet in march_tweets:
    print(tweet.text)


april_tweets = tw.Cursor(api.search,
              q=search_words,
              # geocode=geocode,
              lang=lang,
              result_type=result_type,
              since="2020-04-02",
              max="2020-05-01").items(200)

for tweet in april_tweets:
    print(tweet.text)

may_tweets = tw.Cursor(api.search,
              q=search_words,
              # geocode=geocode,
              lang=lang,
              result_type=result_type,
              since="2020-05-02",
              max="20-06-01").items(200)

for tweet in may_tweets:
    print(tweet.text)
