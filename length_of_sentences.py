from pymystem3 import Mystem
import os
import re

m = Mystem()


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


def meanLengthSent(corpus):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        for f in files:
            if f.endswith('.txt'):
                lens_of_sent = 0
                #print(f)
                o = open('./Corpus/' + corpus + '/Original/' + f, 'r', encoding='utf-8').read()
                # print(o)
                punct = re.compile('[.?!]')
                o = punct.split(o)
                sentences = []
                for i in o:
                    if i is not '':
                        sentences.append(i)
                for i in sentences:
                    i = lemmas(i)
                    # print(i)
                    lens_of_sent += len(i.split())
                #print(lens_of_sent)
                #print(len(sentences))
                medium_len_of_sent = lens_of_sent/len(sentences)
                yield(round(medium_len_of_sent, 2))
                #print('\n')


#for i in meanLengthSent('Suspense'): print(i)