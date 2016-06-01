import re
from break_text_into_paragraphs import break_into_paragraphs
from prepare_corpus import prepare

novel = input('Please type the name of the novel which stored in a .txt file: ')

file = open('./Corpus/' + novel + '/' + novel + '.txt', 'r', encoding='utf-8')
text = file.read()
text = re.sub(':\n-', ':\n -', text)
text = re.sub(':\n–', ':\n –', text)
text = text.split('\n')

break_into_paragraphs(text, novel)

prepare(novel)
