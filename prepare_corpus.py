import os


def lemmas(corpus, file):
    os.system('./' + 'mystem -d -n -i -s --format=json --eng-gr ' + './Corpus/' + corpus + '/Original/' + file + ' ' +
              './Corpus/' + corpus + '/mystemed/' + file.split('.')[0] + '_mystemed.txt')


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
                print(file)
                parse('/Users/IrinaPavlova/Desktop/Uni/2015-2016/Programming/github\ desktop/Suspense/Corpus/' + corpus + '/Original/' + file)

prepare('Akunin')