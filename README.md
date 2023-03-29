# TweetsRanking

### Downloading the live stream twitter data and creating the dataset.
### Classifying the tweets as related to disaster and not related to disaster.
### Sentiment Analysis of the classified tweets.
### Ranking the disaster related tweets.
### Integrating the final model in a web application.



Twitter live stream data is retrieved in the form of tweets using the python package snscrape, then it is stored in an excel format. The types of preprocessing techniques include removal of any urls, emails, removing the retweets to reduce redundancy in tweets, removing the html tags or any mentions in the tweet, and also correcting the spelling mistakes if there are any, in the tweet. The preprocessed dataset is trained using three different machine learning algorithms for classifying the tweets into disaster related and not related. The result of classification algorithm whose testing accuracy is high is sent for sentiment analysis to know whether the tweets are negative, positive or neutral. Finally, the tweets are given ranking using Count Vectorizer and Latent Dirichlet Allocation and the ranked tweets are displayed on a webpage.
