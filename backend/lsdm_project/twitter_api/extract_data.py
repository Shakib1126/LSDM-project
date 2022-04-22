import pandas as pd
from twython import Twython, TwythonError
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
import matplotlib.pyplot as plt
from datetime import datetime
from nltk.corpus import opinion_lexicon

from .models import twitter_data
# import plotly.express as px
# import tzlocal  
# from pytz import timezone

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('vader_lexicon')
# nltk.download('opinion_lexicon')


consumer_key = "ZpuyQUWyiM09NQwLK9MTNfQHt"
consumer_secret = "IQ6HWO4OsrxBNsXJILPw26fgzKHzuthKQvpuPo55xFXfdmYXpG"
access_token = "2937336096-DrpKKvHQxG6ruCb78EtiStQF6XkL3KMtX6nLzX6"
access_token_secret = "KKGedqXnm9VtuXFW4tMRMRKoiHUx8Ibd99yLlMZyIWhzX"

class extractData():



    def into_lower(x):
      return(x.lower())


    # Function to remove web links from text
    def remove_links(x):
        return re.sub(r'http\S+', '', x)


    # Function to remove punctuations from tweets
    def remove_punctuations(x):
        return re.sub(r'[^\w\s]',"",x)


    def remove_username(x):
        return re.sub('@[\w]+','',x)



    # Function to remove emojis from the tweets
    def remove_emoji(x):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags 
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', x)


    # Function to remove stopwords from tweets
    def remove_stopwords(x):
        return ' '.join([word for word in x.split() if word not in stopwords.words("english")])


    # Function to Lemmatize the text in tweets
    def word_lemmatization(x):
        lemmatizer = WordNetLemmatizer()
        word_list = nltk.word_tokenize(x)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        return lemmatized_output

    
    def search_tweets(key):
      twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    # geocode = '29.42458,-98.49461,200mi' # latitude,longitude,distance(mi/km)
      search_results = twitter.search(q=key,count=2, lang ="en")
      for tweet in search_results['statuses']:
        text = tweet['text']
        user = tweet['user']['name']
        created_at = tweet['created_at']
        hashtags = tweet['entities']['hashtags']
        user_mentions = tweet['entities']['user_mentions']
        url = tweet['entities']['urls']
        ins = twitter_data(tweets = text,user = user,created_at=created_at, hashtags=hashtags,user_mentions=user_mentions,url=url)
        ins.save()
    

extractData.search_tweets("chelsea")







    # with open("all_tweets.txt", "a") as f:
    #     try:
    #         for tweet in search_results["statuses"]:
    #             message= tweet["text"]
    #             time,weekday = convert_to_datetime(str(tweet["created_at"]))
    #             #.encode("ascii", "ignore")
    #             f.write(str(name) + ",")
    #             f.write(str(time) + ",")
    #             f.write(str(weekday) + ",")
    #             f.write(word_lemmatization(remove_stopwords(remove_punctuations(remove_links(into_lower(remove_emoji(remove_username(str(message)))))))) + "\n")
                
    #     except TwythonError as e:
    #         print(e)

    # search_tweets(key=["job","work","working","jobless"],geocode="33.6533,-86.8089" +',2000mi', name = "Houston")
    # # for i in range(len(cities_coordinates)):
    # #     search_tweets(key=["job","work","working","jobless"],geocode=cities_coordinates[i]+',2000mi', name = cities_names[i])
