from pymystem3 import Mystem
m = Mystem()
import os
import nltk
import re

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

for root, dirs, files in os.walk('./Corpus/Suspense'):
    lens = {}
    for f in files:
        print(f)
        if f.endswith('.txt'):
            o = open('./Corpus/Suspense/' + f, 'r', encoding='utf-8').read()
            # print(o)
            punct = re.compile('[.?!]')
            o = punct.split(o)
            sentences = []
            for i in o:
                if i is not '':
                    sentences.append(i)

        lens_of_sent = 0
        for i in sentences:
            i = lemmas(i)
            print(i)
            print(len(i.split()))

