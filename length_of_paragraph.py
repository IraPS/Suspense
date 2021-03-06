import os
import re


def meanLengthPar(corpus, number_of_files):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        all = []
        lens = {}
        for f in files:
            if f.endswith('.txt'):
                # print(f)
                o = open('./Corpus/' + corpus + '/Original/' + f, 'r', encoding='utf-8').read()
                # print(o)
                punct = re.compile('[.?!]')
                o = punct.split(o)
                sentences = []
                for i in o:
                    if i is not '':
                        sentences.append(i)
                # print(sentences)
                # print(len(sentences))
                all.append(len(sentences))
                if len(sentences) in lens:
                    lens[len(sentences)] += 1
                else:
                    lens[len(sentences)] = 1
                yield(len(sentences))


#meanLengthPar('Unsuspense', 123)
#for i in meanLengthPar('Suspense', 141): print(i)