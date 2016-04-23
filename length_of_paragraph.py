import os
import re

lens = {}

for root, dirs, files in os.walk('./Corpus/Suspense'):
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
            print(len(sentences))
            if len(sentences) in lens:
                lens[len(sentences)] += 1
            else:
                lens[len(sentences)] = 1

print(lens)

for i in lens:
    print(str(i) + ' : ' + str(round((lens[i]*100)/136, 2)))

