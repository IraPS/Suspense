import re
import copy

f = open('suspense_parsed.txt', 'r').read()
aa = []
a = []
for i in f.split('\n\n'):
    if i is not '':
        aa.append(i)

for i in aa:
    a.append(i.split('\n')) # массив с предложениями, каждое предложение - тоже массив его элементов по порядку


words = []



for i in a:
    w = []
    for u in i:
        w.append([(u.split('\t'))[0], (u.split('\t'))[1], (u.split('\t'))[4], (u.split('\t'))[6], (u.split('\t'))[7]])
    words.append(w)

d = []

#print(words)

for i in words:
    dd = []
    for u in i:
        if u[4] == 'предик':
            ddd = {}
            ddd[int(u[0])] = 'S'
            ddd[int(u[3])] = 'V'
            dd.append(ddd)
            # dd - массив с инфой об S и V
    fdd = []
    for el in dd:
        fd = copy.copy(el)
        for ele in el:
            if el[ele] == 'V':
                for u in i:
                    if int(u[3]) == ele and u[4] == '1-компл':
                        fd[int(u[0])] = 'O'
        fdd.append(fd)
        # fdd - массив с инфой об S и V и O
    #print(dd)
    d.append(fdd)
print(d)