import nltk, string
from nltk.stem.porter import PorterStemmer


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

content = open("alice.txt", 'r').read()

translating = str.maketrans('', '', string.punctuation)
translating2 = str.maketrans('', '', '-')
vocabulary = content.translate(translating).translate(translating2)

tokenized_words = word_tokenize(vocabulary)

# tokenized_words = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and', 'pak']
porter = PorterStemmer()
print([porter.stem(word) for word in tokenized_words])
