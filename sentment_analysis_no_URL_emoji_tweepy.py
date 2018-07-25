from textblob import TextBlob
import tweepy
import re
from API_tweeter import Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret


consumerKey = Consumer_Key
consumerSecret = Consumer_Secret
accessToken =  Access_Token
accessTokenSecret = Access_Token_Secret

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(key=accessToken,secret=accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)

searchTerm = input("Enter the keyword/hastag to search :")
noOfTwites = int(input("Enter how many tweets to analyze: "))



tweets = tweepy.Cursor(api.search,q=searchTerm+" -rt",lang = 'en',
                       result_type="popular",count = noOfTwites).items(noOfTwites)

"""
Obtaining tweets for searchTerms and the first number pages. for timeline use api.time_time
result_type = "recent"-> recent tweets and "popular" for popular ones
"mix" for a bit of both.
"-rt " -> we exclude retweets.
"""

#Remove emojies, quotation marks, https
for tweet in tweets:
    remove_http_tweet = re.sub(r"http\S+","",tweet.text)
    clean_tweet = " ".join(re.findall("[a-zA-Z]+",remove_http_tweet))
    analysis = TextBlob(clean_tweet).sentiment.polarity
    print("tweet")
    print(clean_tweet)
    print("Sentiment",analysis)
    print(20*"==")