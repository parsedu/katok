import string, re
from nltk.tokenize import word_tokenize

# def capitalizer(string: str) -> str:
#     return string.upper()
#
# def replace_letters_with_X(string: str) -> str:
#     return re.sub(r"[а-яА-Я]", "*", string)

file_name = "text_data.txt"
file = open(file_name, 'r', encoding='utf_8_sig')
content = file.read()
print(content)

translating = str.maketrans('', '', string.punctuation)
translating1 = str.maketrans('', '', ' ')
translating2 = str.maketrans('', '', '-')

vocabulary = content.translate(translating).translate(translating1).translate(translating2)
print(vocabulary)
# print(capitalizer(vocabulary))
# print(replace_letters_with_X(vocabulary))
file.close()
