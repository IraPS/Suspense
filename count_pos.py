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

all_sentences = []


for root, dirs, files in os.walk('./Corpus/Unsuspense/mystemed'):
    for f in files:
        if f.endswith('.txt'):
            #print('FILE', f)
            t = open('./Corpus/Unsuspense/mystemed/' + f, 'r', encoding='utf-8').read()
            o = t.split('{"text":"\\')
            sentences = []
            all_pos = [0]*13
            for i in o:
                if i is not '':
                    sentences.append(i)
                    all_sentences.append(i)
            #print(len(sentences))
            for i in sentences:
                #print(i)
                #print(pos(i))
                #print('\n\n')
                for k in range(len(pos(i))):
                    all_pos[k] += pos(i)[k]
            #print(all_pos)
            summa = sum(all_pos)
            ratio = all_pos[11]/summa
            print(round(ratio, 2))
            #print('\n\n')

            #for i in all_pos: print(i)

