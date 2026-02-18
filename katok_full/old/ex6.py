from nltk import pos_tag
from nltk import word_tokenize
import nltk
# nltk.download("averaged_perceptron_tagger_eng")
# nltk.download("brown")


text_data = "Chris loved outdoor runnig"
text_tagged = pos_tag(word_tokenize(text_data))
print(text_tagged)



from sklearn.preprocessing import MultiLabelBinarizer
tweets = ["I am eating a burrito for breakfast",
          "Political science is and amazing field", "San Francisco is an awesome city"]

tagged_tweets = []
for tweet in tweets:
    tweet_tag = nltk.pos_tag(word_tokenize(tweet))
    tagged_tweets.append([tag for word, tag in tweet_tag])
    one_hot_multi = MultiLabelBinarizer()
    one_hot_multi.fit_transform(tagged_tweets)

one_hot_multi.classes_

from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger

sentences = brown.tagged_sents(categories='news')
train = sentences[:4000]
test = sentences[4000:]
unigram = UnigramTagger(train)
bigram = BigramTagger(train, backoff=unigram)
trigram = TrigramTagger(train, backoff=bigram)
print(trigram.accuracy(test))

