'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
i = 0
for tweet in tweetData:
    blob = TextBlob(tweet["text"])
    twt_pol = blob.polarity
    twt_sub = blob.subjectivity
    polarity.append(twt_pol)
    subjectivity.append(twt_sub)
    i += 1

avg_pol = sum(polarity) / len(polarity)
avg_sub = sum(subjectivity) / len(subjectivity)
print(avg_pol)
print(avg_sub)

# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

plt.hist(polarity, bins = [-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.ylabel('# tweets')
plt.xlabel('polarity')
plt.title('Histogram of Polarity')
plt.axis([-1, 1, 0, 60])
plt.grid(True)
plt.show()

plt.hist(subjectivity, bins = [-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.ylabel('# tweets')
plt.xlabel('subjectivity')
plt.title('Histogram of Subjectivity')
plt.axis([-1, 1, 0, 60])
plt.grid(True)
plt.show()

plt.scatter(polarity, subjectivity)
plt.show()
