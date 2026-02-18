from nltk.stem.porter import PorterStemmer
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']
porter = PorterStemmer()
print([porter.stem(word) for word in tokenized_words])

from nltk.stem.snowball import SnowballStemmer
tokenized_words = ['рыбаки', 'рыбаков', 'рыбаками']
snowball = SnowballStemmer("russian")
print([snowball.stem(word) for word in tokenized_words])