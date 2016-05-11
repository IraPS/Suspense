import os


def bowVector(corpus):
    lemmas = ['гробовщик', 'входить', 'операционный', 'кочерга', 'добрый', 'кровь', 'кожа', 'рука', 'жена', 'доктор',
          'директор', 'лежать', 'лицо', 'рассказывать', 'платформа', 'прострелить', 'укусить', 'спрашивать', 'девушка',
          'граф', 'поезд', 'хотеть', 'узнавать', 'нужно', 'муха', 'минута', 'слово', 'пчела', 'кость', 'бросаться',
          'оставаться', 'дескать', 'фельдшер', 'шутить', 'рот', 'увидеть', 'отвечать', 'мочь', 'ужас', 'сиятельство',
          'давать', 'подумать', 'делать', 'пинцет', 'выстреливать', 'станция', 'истопник', 'ах', 'знать', 'сказать',
          'пистолет', 'начальник', 'становиться', 'секретарь', 'проходить', 'умирать', 'нож', 'человек', 'видеть', 'это',
          'мертвец', 'ваш']
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
