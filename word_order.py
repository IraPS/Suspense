import re

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
    dd = {}
    for u in i:
        if u[4] == 'предик':
            print(u)
            dd[int(u[0])] = 'предикат'
    d.append(dd)
print(d)
