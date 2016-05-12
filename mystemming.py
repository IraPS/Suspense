import os


def lemmas(file):
    os.system('./' + 'mystem -d -n -i -s --format=json --eng-gr ' + './Corpus/New/Original/' + file + ' ' + './Corpus/New/mystemed/' + file.split('.')[0] + '_mystemed.txt')
for root, dirs, files in os.walk('./Corpus/New/Original'):
    for file in files:
        if file.endswith('.txt'):
            lemmas(file)
