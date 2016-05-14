from openpyxl import load_workbook
wb = load_workbook(filename='suspense_paragraphs.xlsx')
ws = wb['Лист1']
n = 1
for row in ws.rows:
    for cell in row:
        if cell.value is not None:
            o = open('./Corpus/Suspense/Original/suspense' + str(n) + '.txt', 'w', encoding='utf-8')
            print(cell.value)
            print('\n\n')
            o.write(cell.value)
            o.close()
        n += 1
