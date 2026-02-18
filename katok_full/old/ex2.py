from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt_tab')
string = "Todays science is the tecnology of the future"
print(word_tokenize(string))
string2 = "Todays science is the tecnology of the future. Tomorrow starts with today"
print(sent_tokenize(string2))
