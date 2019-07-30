'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
commonWords = ["and", "because", "that", "http", "for" "your", "https", "about", "the", "from", "they", "don't", "have", "you", "it's"]

bigtwt = ""
for tweet in tweetData:
    txt = tweet["text"]
    bigtwt += txt

twt_tb = TextBlob(bigtwt)
filtered = {}

wordList = twt_tb.words
for word in wordList:
    if word.lower() in commonWords:
        continue
    if len(word) < 4:
        continue
    if not word.isalpha():
        continue

    filtered[word] = twt_tb.word_counts[word]
#for word in twt_tb:
    #if word in commonWords:

#WordCloud(twt_tb)
wordcloud = WordCloud().generate_from_frequencies(filtered)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
