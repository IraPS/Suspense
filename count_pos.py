import re
import os


def adj(sent):
    k = re.findall('analysis.*?gr.*?A=', sent)
    return len(k)


def adv(sent):
    k = re.findall('analysis.*?gr.*?(ADV|ADVPRO)', sent)
    return len(k)


def num_adj(sent):
    k = re.findall('analysis.*?gr.*?(ANUM)', sent)
    return len(k)


def pron_adj(sent):
    k = re.findall('analysis.*?gr.*?(APRO)', sent)
    return len(k)


def num_comp(sent):
    k = re.findall('analysis.*?gr.*?COM', sent)
    return len(k)


def conj(sent):
    k = re.findall('analysis.*?gr.*?CONJ', sent)
    return len(k)


def intj(sent):
    k = re.findall('analysis.*?gr.*?INTJ', sent)
    return len(k)


def num(sent):
    k = re.findall('analysis.*?gr.*?"NUM', sent)
    return len(k)


def part(sent):
    k = re.findall('analysis.*?gr.*?PART', sent)
    return len(k)


def prep(sent):
    k = re.findall('analysis.*?gr.*?"PR=', sent)
    return len(k)


def noun(sent):
    k = re.findall('analysis.*?gr.*?"S,', sent)
    return len(k)


def verb(sent):
    k = re.findall('analysis.*?gr.*?"V(,|=)', sent)
    return len(k)


def pron_noun(sent):
    k = re.findall('analysis.*?gr.*?SPRO', sent)
    return len(k)


def pos(sent):
    return adj(sent), adv(sent), num_adj(sent), pron_adj(sent), num_comp(sent), conj(sent), intj(sent), num(sent), \
           part(sent), prep(sent), noun(sent), verb(sent), pron_noun(sent)


for root, dirs, files in os.walk('./Corpus/Unsuspense/mystemed'):
    for f in files:
        if f.endswith('.txt'):
            o = open('./Corpus/Unsuspense/mystemed/' + f, 'r', encoding='utf-8').read()
            # print(o)
            o = o.split('{"text":"\\s"}')
            sentences = []
            for i in o:
                if i is not '':
                    sentences.append(i)

            for i in sentences:
                print(i)
                print(pos(i))
                print('\n\n')

