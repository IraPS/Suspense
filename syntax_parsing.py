import os


def lemmas(file):
    os.system('python3 /Users/IrinaPavlova/Desktop/rusyntax/ru-syntax.py ' + file)

for root, dirs, files in os.walk('./Corpus/New/Original'):
    for file in files:
        if file.endswith('.txt'):
            print(file)
            lemmas('/Users/IrinaPavlova/Desktop/Uni/2015-2016/Programming/github\ desktop/Suspense/Corpus/New/Original/' + file)