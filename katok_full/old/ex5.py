import nltk
from nltk.stem import WordNetLemmatizer
tokenized_words = ['go', 'went', 'gone', 'am', 'are', 'is', 'was', 'were']
lemmatizer = WordNetLemmatizer()
nltk.download("wordnet")

print([lemmatizer.lemmatize(word, pos='v') for word in tokenized_words])

