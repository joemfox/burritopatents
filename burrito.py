import sys
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import twitter
from auth import *

api = twitter.Api(consumer_key=BIkey,consumer_secret=BIskey,access_token_key = BItoken,access_token_secret = BIstoken)
newfile = open(sys.argv[1],"r")
sentence = newfile.readline()
print sentence
if len(sentence)-1 > 135:
    print "too long, truncating"
    sentence = sentence.split(",")[0]
tokens = word_tokenize(sentence)
pos = pos_tag(tokens)
nouns = []
adjectives = []

for word in pos:
    if word[1] == "NN" or word[1] == "NNP" or word[1] == "NNS":
        nouns.append(word)

    if word[1] == "JJ":
        adjectives.append(word)

rand = random.randint(0,len(nouns)-1)
burrito = "burrito"
if rand == 0:
    burrito = "Burrito"

if nouns[rand][1] == "NNS":
    burrito = "burritos"

burritosentence = sentence.replace(nouns[rand][0],burrito,1)

print burritosentence

spicy = "spicy"
if len(adjectives) > 0:
    spicy = adjectives[random.randint(0,len(adjectives)-1)][0]
print spicy
if len(burritosentence) > 60:
    print burritosentence.replace(spicy, "spicy")

# twit.statuses.update(status=burritosentence)
api.PostUpdate(burritosentence)