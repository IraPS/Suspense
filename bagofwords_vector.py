import os


def bowVector(corpus):
    lemmas = ['сказать', 'рука', 'становиться', 'лицо', 'гробовщик', 'начальник', 'умирать', 'отвечать', 'станция', 'ваш',
          'пчела', 'увидеть', 'хотеть', 'кровь', 'граф', 'сиятельство', 'минута', 'кость', 'лежать',
          'фельдшер', 'пистолет', 'девушка', 'проходить', 'платформа', 'класс', 'прострелить', 'входить', 'ужас', 'истопник',
          'оставаться','выстреливать', 'подумать', 'кочерга', 'ах', 'поезд', 'бросаться',
          'нож', 'директор', 'узнавать', 'рот',
          'операционный', 'мертвец', 'склад', 'кожа', 'доктор', 'сторона', 'укусить', 'дверь', 'живой', 'муха',
          'показываться', 'секретарь', 'секунда', 'пинцет', 'нужно', 'продолжать', 'добрый', 'никто', 'дескать', 'шутя',
          'вера', 'кричать', 'вынимать', 'картина', 'шутить', 'штука', 'выкрикивать', 'закричать',
          'помирать', 'пощечина', 'успевать', 'ампутация', 'бумажка', 'рассказывать', 'позвать']
    for root, dirs, files in os.walk('./Corpus/' + corpus + '/mystemed'):
        for f in files:
            if f.endswith('.txt'):
                # print(f)
                t = open('./Corpus/'+ corpus + '/mystemed/' + f, 'r', encoding='utf-8').read()
                vector = [0]*len(lemmas)
                for i in range(len(lemmas)-1):
                    if lemmas[i] in t:
                        vector[i] = 1
                    else:
                        vector[i] = 0
                yield vector
