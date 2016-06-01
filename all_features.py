import os
import numpy as np
from bagofwords_vector import bowVector # генератор с векторами bag-of-words (присутсвие/отсутствие леммы), для абзацев
from length_of_paragraph import meanLengthPar # генератор со средними длинами абзацев в предложениях
from length_of_sentences import meanLengthSent # генератор со средними длинами предложений в абзацах
from count_pos import verbsRatio # генератор с ratio глаголы vs. остальные части речи, для абзацев
from verbs_in_past_tense import pastVerbsRatio # генератор с ratio глаголы в прош.вр. vs. все глаголы, для абзацев
from finitnefinit import finitRatio # генератор с ratio финитные vs. нефинитные глаголы, для абзацев
from word_order import wordOrderRatio # генератор с ratio S-V vs. V-S порядок слов, для абзацев


def getCorpusSize(corpus):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        size = 0
        for f in files:
            if f.endswith('.txt'):
                size += 1
        return size


def getFeatures(corpus):

    size = getCorpusSize(corpus)
    all_features = []

    first = []
    for i in bowVector(corpus): # 75 признаков
        first.append(i)
    second = []
    for i in meanLengthPar(corpus, size): # 76ой
        second.append(i)
    third = []
    for i in meanLengthSent(corpus): # 77ой
        third.append(i)
    fourth = []
    for i in verbsRatio(corpus): # 78ой
        fourth.append(i)
    fifth = []
    for i in pastVerbsRatio(corpus): # 79ый
        fifth.append(i)
    sixth = []
    for i in finitRatio(corpus): # 80ый
        sixth.append(i)
    seventh = []
    for i in wordOrderRatio(corpus): # 81ый
        seventh.append(i)


    for i in range(size):
        #print(i)
        a = []
        a += first[i]
        a.append(second[i])
        a.append(third[i])
        a.append(fourth[i])
        a.append(fifth[i])
        a.append(sixth[i])
        a.append(seventh[i])
        all_features.append(a)
    print('Features collected')
    return all_features


#features = getFeatures(corpus)
#np.savez_compressed(corpus + '_features.npz', features)