from textblob import TextBlob
from matplotlib import pyplot as plt
import sys
import tweepy

def percentage(part, whole):
    return 100*float(part)/float(whole)

ApiKey = "EDPJyr5runS8PpPGlWVrdDhG6"
ApiKeySecret = "ShHd8WE1RteAwCxpCuoLfpgZEAs9RXIZbZzMQKvbblpbvLDKva"
AcessToken = "1117280968463802368-erI7RGps3O6kojZWK7tZyfH4LwSYML"
AcessTokenSecret = "RxDKQg6fE1aGVXMBrMV8SQhfSd2OCz2AbDVHuYba98Asm" 

auth = tweepy.OAuthHandler(consumer_key=ApiKey ,consumer_secret = ApiKeySecret )
auth.set_access_token(AcessToken, AcessTokenSecret)
api = tweepy.API(auth)


search = input(" Enter the hashtag you want to search about: ")
n_search_items = int(input(" Enter the number of tweets to be analyzed: "))

tweets = tweepy.Cursor(api.search, q = search).items(n_search_items)

positive_sentiments = 0
negative_sentiments = 0
neutral_sentiments = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if( analysis.sentiment.polarity == 0 ):
        neutral_sentiments += 1
    elif(analysis.sentiment.polarity > 0.0001 ):
        positive_sentiments += 1
    elif( analysis.sentiment.polarity < 0.0001 ):
        negative_sentiments += 1

positive = percentage(positive_sentiments, n_search_items)
negative = percentage(negative_sentiments, n_search_items)
neutral = percentage(neutral_sentiments, n_search_items)


positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')
polarity = format(polarity,'.2f')

print("What is the reaction of people on " + search + " by analyzing " + str(n_search_items) + "tweets?")


print(polarity) 
labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 'Neutral ['+str(neutral)+'%]']
sizes = [positive,negative,neutral]
colors = ['yellow','red','green']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc = 'best')
plt.title("What is the reaction of people on" + search + " by analyzing " + str(n_search_items) + "tweets?")
plt.axis('equal')
plt.tight_layout()
plt.show() 

    
         





                       
          


