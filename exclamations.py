import os

for root, dirs, files in os.walk('./Corpus/Unsuspense/Original'):
    for f in files:
        if f.endswith('.txt'):
            #print(f)
            corp = open('./Corpus/Unsuspense/Original/' + f, 'r', encoding='utf-8').read()
            print(corp.count('!'))
