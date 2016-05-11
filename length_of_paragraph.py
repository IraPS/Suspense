import os
import re
import numpy as np


def meanLengthPar(corpus, number_of_files):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        all = []
        lens = {}
        for f in files:
            if f.endswith('.txt'):
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
        # print(np.median(all))
        #print('SUSPENSE DATA')
        for i in lens:
            yield round((lens[i]*100)/number_of_files, 2)