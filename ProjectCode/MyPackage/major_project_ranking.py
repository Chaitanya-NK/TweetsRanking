# -*- coding: utf-8 -*-
"""Major Project Ranking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NMt97WDAihpUseMtKsgYTqrUkcN_gGQ6
"""

import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('C:/Users/chait/Documents/Project/ProjectCode/MyPackage/target_dataset.csv')

data['Tweet'] = data['Tweet'].str.replace(r'http\S+', '', case=False)
data['Tweet'] = data['Tweet'].str.replace(r'@\S+', '', case=False)

analyzer = SentimentIntensityAnalyzer()

sentiments = []
for tweet in data['Tweet']:
    scores = analyzer.polarity_scores(tweet)
    if scores['compound'] > 0:
        sentiment = '1'
    elif scores['compound'] < 0:
        sentiment = '-1'
    else:
        sentiment = '0'
    sentiments.append(sentiment)

data['sentiment'] = sentiments

print(data['sentiment'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt
def graph():
    plt.rcParams['figure.figsize'] = [8,4]
    plt.rcParams['figure.dpi'] = 80
    tweets = pd.read_csv('MyPackage/twitter_sentiment_dataset.csv')
    tweets['sentiment'].value_counts().plot.pie(autopct='%1.2f%%')

data.head()

data.to_csv('twitter_sentiment_dataset.csv', index=False)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import app

def ranking(user_tweet):
  # Load dataset

    data = pd.read_csv('twitter_sentiment_dataset.csv')

    cv = CountVectorizer()
    dtm = cv.fit_transform(data['Tweet'])

    lda_model = LatentDirichletAllocation(n_components=10, random_state=42)
    lda_model.fit(dtm)

    # query_tweet = user_tweet # query tweet
    query_dtm = cv.transform([user_tweet])
    query_topic_distribution = lda_model.transform(query_dtm)[0]

    tweet_topic_distributions = lda_model.transform(dtm)
    similarity_scores = np.dot(tweet_topic_distributions, query_topic_distribution)
    top_tweets_indices = similarity_scores.argsort()[::-1][:10] # top 10 most similar tweets
    top_tweets = data.iloc[top_tweets_indices]['Tweet']

    df = pd.DataFrame(columns=["Rank", "Tweet"])

    for i, tweet in enumerate(top_tweets):
        rank = i + 1
        # print(f"Rank {rank}: {tweet}")
        df.loc[i] = ['Rank ' + str(rank), tweet]
    return df
