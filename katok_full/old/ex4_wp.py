import nltk, string
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

content = open("WP.txt", 'r', encoding='utf_8_sig').read()

translating = str.maketrans('', '', string.punctuation)
translating2 = str.maketrans('', '', '-')
vocabulary = content.translate(translating).translate(translating2)

tokenized_words = word_tokenize(vocabulary)

# tokenized_words = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and', 'pak']
snowball = SnowballStemmer("russian")
print([snowball.stem(word) for word in tokenized_words])
