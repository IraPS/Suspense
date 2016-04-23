from pymystem3 import Mystem
m = Mystem()

t = 'Чайника, сегодня не было'
lemma = m.lemmatize(t)


def lemmas(text):
    punc = list('.?!-;:",')
    text = [i for i in text if i not in punc]
    text = ''.join(text)
    text = m.lemmatize(text)
    textn = ''
    for w in text:
        if w is not ' ' or '\n':
            textn += w
    return textn


from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os

s_w = stopwords.words('russian')
sw = [i for i in s_w]

v = TfidfVectorizer(stop_words=sw) # убираем стоп-слова
#v = TfidfVectorizer() # не убираем стоп-слова

totalCorpus = []
suspenseCorpus = ''
unsuspenseCorpus = ''

for root, dirs, files in os.walk('./Corpus/Unsuspense'):
    for f in files:
        if f.endswith('.txt'):
            corp = open('./Corpus/Unsuspense/' + f, 'r', encoding='utf-8').read()
            corp = lemmas(corp)
            unsuspenseCorpus += corp
            totalCorpus.append(corp)

for root, dirs, files in os.walk('./Corpus/Suspense'):
    for f in files:
        if f.endswith('.txt'):
            corp = open('./Corpus/Suspense/' + f, 'r', encoding='utf-8').read()
            corp = lemmas(corp)
            # print(corp)
            suspenseCorpus += corp
            totalCorpus.append(corp)

tfidf = v.fit_transform(totalCorpus)


def bag_of_words(corpus):
    feature_names = v.get_feature_names()
    response = v.transform([corpus]) # ТУТ выбираем корпус, для которого считаем tf-idf
    tfidf_dict = {}
    for col in tfidf.nonzero()[1]:
        tfidf_dict[feature_names[col]] = response[0, col]
    tfidf_dict = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True) # ТУТ отсортированные по убыванию слова со значениями
    return tfidf_dict

print(bag_of_words(unsuspenseCorpus))

tfidf = tfidf.todense()
print(tfidf.shape)

# print(np.count_nonzero(tfidf[0]))

# print(v.get_stop_words())


