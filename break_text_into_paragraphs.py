f = open('Akunin.txt', 'r', encoding='utf-8').read()
t = f.split(' ')

def check(p):
    if p[0] == '–':
        return True
    else:
        return False


def add(m, ind):
    par = m[ind]
    n = 1
    while check(m[ind+n]):
        #print('yes')
        par += '\n'
        par += m[ind+n]
        #print(par)
        n += 1
    #print('ADD FUNC final\n', par)
    return par, ind+n


paragraphs = []

i = 0
while i < len(t):
    pp = False
    if check(t[i]):
        paragraphs.append(add(t, i)[0])
        pp = True
    if pp:
        i = add(t, i)[1]
    else:
        paragraphs.append(t[i])
        i += 1


n = 1
for i in paragraphs:
    if n < 10:
        o = open('./Corpus/Akunin/Original/' + str(0) + str(0) + str(0) + str(n) + '.txt', 'w', encoding='utf-8')
        o.write(i)
        o.close()
    if 9 < n < 100:
        o = open('./Corpus/Akunin/Original/' + str(0) + str(0) + str(n) + '.txt', 'w', encoding='utf-8')
        o.write(i)
        o.close()
    if 99 < n < 1000:
        o = open('./Corpus/Akunin/Original/' + str(0) + str(n) + '.txt', 'w', encoding='utf-8')
        o.write(i)
        o.close()
    if n > 999:
        o = open('./Corpus/Akunin/Original/' + str(n) + '.txt', 'w', encoding='utf-8')
        o.write(i)
        o.close()

    n += 1








