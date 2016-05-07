import re
import os


def verb(sent):
    k = re.findall('analysis.*?gr.*?"V(,|=)', sent)
    return len(k)


def verb_past(sent):
    k = re.findall('analysis.*?gr.*?"V(,|=).*?praet', sent)
    return len(k)

all_sentences = []

for root, dirs, files in os.walk('./Corpus/Unsuspense/mystemed'):
    for f in files:
        if f.endswith('.txt'):
            print(f)
            all_verbs = 0
            past_verbs = 0
            t = open('./Corpus/Unsuspense/mystemed/' + f, 'r', encoding='utf-8').read()
            o = t.split('{"text":"\\')
            sentences = []
            for i in o:
                if i is not '':
                    sentences.append(i)
                    all_sentences.append(i)
            for i in sentences:
                all_verbs += verb(i)
                past_verbs += verb_past(i)
            print(all_verbs, past_verbs, '\n')