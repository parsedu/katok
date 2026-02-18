import nltk, string
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

content = open("alice.txt", 'r').read()

translating = str.maketrans('', '', string.punctuation)
translating2 = str.maketrans('', '', '-')
vocabulary = content.translate(translating).translate(translating2)

tokenized_words = word_tokenize(vocabulary)

# tokenized_words = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and', 'pak']
stop_words = ['a', 'the', 'and', 'or']
print([word for word in tokenized_words if word not in stop_words])
