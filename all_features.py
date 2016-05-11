import os
import re
from bagofwords_vector import bowVector # генератор с векторами bag-of-words (присутсвие/отсутствие леммы), для абзацев
from length_of_paragraph import meanLengthPar # генератор со средними длинами абзацев в предложениях
from length_of_sentences import meanLengthSent # генератор со средними длинами предложений в абзацах
from count_pos import verbsRatio # генератор с ratio глаголы vs. остальные части речи, для абзацев
from verbs_in_past_tense import pastVerbsRatio # генератор с ratio глаголы в прош.вр. vs. все глаголы, для абзацев
from finitnefinit import finitRatio # генератор с ratio финитные vs. нефинитные глаголы, для абзацев
from word_order import wordOrderRatio # генератор с ratio S-V vs. V-S порядок слов, для абзацев

length_of_suspense_corpus = 136
length_of_unsuspense_corpus = 28

first = []
for i in bowVector('Unsuspense'):
    first.append(i)
second = []
for i in meanLengthPar('Unsuspense', length_of_unsuspense_corpus):
    second.append(i)
third = []
for i in meanLengthSent('Unsuspense'):
    third.append(i)
fourth = []
for i in verbsRatio('Unsuspense'):
    fourth.append(i)
fifth = []
for i in pastVerbsRatio('Unsuspense'):
    fifth.append(i)
sixth = []
for i in finitRatio('Unsuspense'):
    sixth.append(i)
seventh = []
for i in wordOrderRatio('Unsuspense'):
    seventh.append(i)

unsuspense_features = []

for i in range(length_of_unsuspense_corpus):
    #print(i)
    a = []
    a += first[i]
    a.append(second[i])
    a.append(third[i])
    a.append(fourth[i])
    a.append(fifth[i])
    a.append(sixth[i])
    a.append(seventh[i])
    unsuspense_features.append(a)

print(len(unsuspense_features[0]))
