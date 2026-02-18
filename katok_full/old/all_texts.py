import nltk, string
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
texts = ['bor.txt', 'history.txt', 'law.txt', 'lingvist.txt',
         'material.txt', 'phylosophy.txt', 'sociology.txt',
         'vodorod.txt']

for text in texts:
    content = open(text, 'r', encoding='utf_8_sig').read()

    translating = str.maketrans('', '', string.punctuation)
    translating2 = str.maketrans('', '', '-')
    vocabulary = content.translate(translating).translate(translating2)

    tokenized_words = word_tokenize(vocabulary)

    # tokenized_words = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and', 'pak']
    snowball = SnowballStemmer("russian")
    stop_words = ['и', 'или', 'а', 'но']
    without_stop_words = [word for word in tokenized_words if word not in stop_words]

    korni = [snowball.stem(word) for word in without_stop_words]
    print(korni)

    print("------------------------------")

    medicine_voc = CountVectorizer(ngram_range=(1, 2), stop_words="english", vocabulary=['нитрид', 'бор', 'медицина', 'штамм', 'катетер','антибактериальн', 'орган', 'кость', 'череп'])
    materialoved_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['латекс', 'эластичн', 'износостойк', 'издел', 'материал'])
    chemistry_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['хром', 'водород', 'cr', 'ct20', 'бор', 'оксид'])
    econimics_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['эконом', 'энергоресурс', 'показатели', 'эффективность'])
    physics_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['коэффициент', 'трение'])
    lingvist_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['сленг', 'дискурс','словотворчество','профессионализм','лексика'])
    sociology_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['образование', 'социал','мобильн','индивид','самоутвержд','самореализ', 'власть', 'граждан'])
    phylosophy_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['конвергенция', 'бытие','самоуглубл','душа','субъективн','философ', 'сущность'])
    law_voc = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary=['закон', 'власть','постановление','суд','свобод','контроль', 'обжалование', 'арбитраж', 'граждан'])
    history_voc = CountVectorizer(ngram_range=(1, 2), stop_words="english",
                                  vocabulary=['век', 'царь', 'правлен', 'хозяйство', 'древн', 'средневековье',
                                              'государствен', 'тысячелет', 'казна'])

    bag_of_medicine_words = medicine_voc.fit_transform(korni)
    # print(bag_of_medicine_words.toarray())

    count_medicine_words = 0
    # print('------------------')
    # print('\nКоличество совпадений со словарем медицинских слов:\n')
    for row in bag_of_medicine_words.toarray():
        for column in row:
            if column == 1:
                count_medicine_words += 1

    # print(count_medicine_words)
    # print(medicine_voc.vocabulary_)


    # print('------------------')
    # print('\nКоличество совпадений со словарем материаловедческих слов:\n')
    bag_of_materialoved_words = materialoved_voc.fit_transform(korni)
    count_materialoved_words = 0
    for row in bag_of_materialoved_words.toarray():
        for column in row:
            if column == 1:
                count_medicine_words += 1

    # print(count_materialoved_words)
    # print(materialoved_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем химических слов:\n')
    bag_of_chemistry_words = chemistry_voc.fit_transform(korni)
    count_chemistry_words = 0
    for row in bag_of_chemistry_words.toarray():
        for column in row:
            if column == 1:
                count_chemistry_words += 1

    # print(count_chemistry_words)
    # print(chemistry_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем физических слов:\n')
    bag_of_physics_words = physics_voc.fit_transform(korni)
    count_physics_words = 0
    for row in bag_of_physics_words.toarray():
        for column in row:
            if column == 1:
                count_physics_words += 1

    # print(count_physics_words)
    # print(physics_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем лингвистических слов:\n')
    bag_of_lingvist_words = lingvist_voc.fit_transform(korni)
    count_lingvist_words = 0
    for row in bag_of_lingvist_words.toarray():
        for column in row:
            if column == 1:
                count_lingvist_words += 1

    # print(count_lingvist_words)
    # print(lingvist_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем социологических слов:\n')
    bag_of_sociology_words = sociology_voc.fit_transform(korni)
    count_sociology_words = 0
    for row in bag_of_sociology_words.toarray():
        for column in row:
            if column == 1:
                count_sociology_words += 1

    # print(count_sociology_words)
    # print(sociology_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем философских слов:\n')
    bag_of_phylosophy_words = phylosophy_voc.fit_transform(korni)
    count_phylosophy_words = 0
    for row in bag_of_phylosophy_words.toarray():
        for column in row:
            if column == 1:
                count_phylosophy_words += 1

    # print(count_phylosophy_words)
    # print(phylosophy_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем юридических слов:\n')
    bag_of_law_words = law_voc.fit_transform(korni)
    count_law_words = 0
    for row in bag_of_law_words.toarray():
        for column in row:
            if column == 1:
                count_law_words += 1

    # print(count_law_words)
    # print(law_voc.vocabulary_)

    # print('------------------')
    # print('\nКоличество совпадений со словарем юридических слов:\n')
    bag_of_history_words = history_voc.fit_transform(korni)
    count_history_words = 0
    for row in bag_of_history_words.toarray():
        for column in row:
            if column == 1:
                count_history_words += 1

    # print(count_history_words)
    # print(history_voc.vocabulary_)

    list = {'medicine': count_medicine_words,
            'phylosophy': count_phylosophy_words,
            'history': count_history_words,
            'chemistry': count_chemistry_words,
            'lingvisticial': count_lingvist_words,
            'physics': count_physics_words,
            'law': count_law_words,
            'materialoved': count_materialoved_words,
            'sociologoy': count_sociology_words
            }

    max_count = 0
    subject=''
    for element in list:
        if list.__getitem__(element) > max_count:
            max_count = list.__getitem__(element)
            subject = element


    print("\n===========================\n Вывод:\n")
    print("Область научных знания для текста " + text +" is " + subject + ", так как количество совпадений"
                                                  " со словарем слов наибольшее и равно " + (str)(max_count))
    print("______________________")
