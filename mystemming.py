import os

def lemmas(file):
    os.system('./' + 'mystem -d -n -i -s --format=json --eng-gr ' + './Corpus/Unsuspense/Original/' + file + ' ' + './Corpus/Unsuspense/mystemed/' + file.split('.')[0] + '_mystemed.txt')
for root, dirs, files in os.walk('./Corpus/Unsuspense/Original'):
    for file in files:
        if file.endswith('.txt'):
            lemmas(file)
