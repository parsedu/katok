import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
text_data = np.array(['Бразилия - моя любовь. Бразилия!', 'Швеция - лучше!', 'Германия бьет обоих'])
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)
# bag_of_words

bag_of_words.toarray()
print(count.get_feature_names_out())

count_2gram = CountVectorizer(ngram_range=(1, 2), stop_words="english", vocabulary=['бразилия'])
bag = count_2gram.fit_transform(text_data)
print(bag.toarray())

# print(count_2gram.vocabulary_)
# print(bag_of_words.toarray())
