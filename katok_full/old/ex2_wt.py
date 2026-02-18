from nltk.tokenize import word_tokenize, sent_tokenize
import nltk, string
nltk.download('punkt_tab')

file_name = "text_data.txt"
file = open(file_name, 'r', encoding='utf_8_sig')
content = file.read()


translating = str.maketrans('', '', string.punctuation)
translating2 = str.maketrans('', '', '-')

# vocabulary = content.translate(translating).translate(translating2)
# print(word_tokenize(vocabulary))

vocabulary = content.translate(translating2)
print(sent_tokenize(vocabulary))

