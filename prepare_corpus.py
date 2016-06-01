import os
import re


def lemmas(corpus, file):
    os.system('./' + 'mystem -d -n -i -s --format=json --eng-gr ' + './Corpus/' + corpus + '/Original/' + file + ' ' +
              './Corpus/' + corpus + '/Mystemed/' + file.split('.')[0] + '_mystemed.txt')


def parse(file):
    os.system('python3 /Users/IrinaPavlova/Desktop/rusyntax/ru-syntax.py ' + file)


def prepare(corpus):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        for file in files:
            if file.endswith('.txt'):
                lemmas(corpus, file)

    for root, dirs, files in os.walk('./Corpus/' + corpus + '/Original'):
        for file in files:
            if file.endswith('.txt'):
                path = os.path.abspath('./Corpus')
                path = re.sub(' ', '\ ', path)
                parse(path + '/' + corpus + '/Original/' + file)

    print('Corpus is ready for analyzing. Please move the files from RU Syntax'
          ' parser\'s "out" folder to your corpus\' "Syntaxed" folder')

