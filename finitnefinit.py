import re
import os


def verb(sent):
    k = re.findall('analysis.*?gr.*?"V(,|=)', sent)
    #print(k)
    #print('FINIT', len(k))
    return len(k)


def nefinit(sent):
    k = re.findall('analysis.*?gr.*?"V(,|=).*?(ger|inf|partcp)', sent)
    #print('NEFINIT', len(k))
    return len(k)


def finitRatio(corpus):
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/mystemed'):
        for f in files:
            all_sentences = []
            if f.endswith('.txt'):
                #print('FILE', f)
                t = open('./Corpus/' + corpus + '/mystemed/' + f, 'r', encoding='utf-8').read()
                o = t.split('{"text":"\\')
                sentences = []
                for i in o:
                    if i is not '':
                        sentences.append(i)
                        all_sentences.append(i)
                #print(len(sentences))
                all_verbs = 0
                nefinit_verbs = 0
                finit_verbs = 0
                for i in sentences:
                    #print(i)
                    #print(pos(i))
                    #print('\n\n')
                    all_verbs += verb(i)
                    nefinit_verbs += nefinit(i)
                finit_verbs = all_verbs - nefinit_verbs
                #print('ALL', all_verbs)
                #print('FINIT', finit_verbs)
                #print('NEFINIT', nefinit_verbs)
                #print(all_pos)
                if finit_verbs == 0:
                    yield -100
                if nefinit_verbs == 0:
                    yield 100
                else:
                    ratio = finit_verbs/nefinit_verbs
                    yield round(ratio, 2)
                #print('\n\n')

                #for i in all_pos: print(i)