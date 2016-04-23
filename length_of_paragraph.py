import os
import re

for root, dirs, files in os.walk('./Corpus/Suspense'):
    lens = {}
    for f in files:
        if f.endswith('.txt'):
            o = open('./Corpus/Suspense/' + f, 'r', encoding='utf-8').read()
            # print(o)
            punct = re.compile('[.?!]')
            o = punct.split(o)
            sentences = []
            for i in o:
                if i is not '':
                    sentences.append(i)
            # print(sentences)
            # print(len(sentences))
            if len(sentences) in lens:
                lens[len(sentences)] += 1
            else:
                lens[len(sentences)] = 1
    print('SUSPENSE DATA')
    for i in lens:
        print(str(i) + ' : ' + str(round((lens[i]*100)/136, 2)))

for root, dirs, files in os.walk('./Corpus/Unsuspense'):
    lens = {}
    for f in files:
        if f.endswith('.txt'):
            o = open('./Corpus/Unsuspense/' + f, 'r', encoding='utf-8').read()
            # print(o)
            punct = re.compile('[.?!]')
            o = punct.split(o)
            sentences = []
            for i in o:
                if i is not '':
                    sentences.append(i)
            # print(sentences)
            # print(len(sentences))
            if len(sentences) in lens:
                lens[len(sentences)] += 1
            else:
                lens[len(sentences)] = 1
    print('UNSUSPENSE DATA')
    for i in lens:
        print(str(i) + ' : ' + str(round((lens[i]*100)/28, 2)))

