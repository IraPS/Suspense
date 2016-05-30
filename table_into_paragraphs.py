from openpyxl import load_workbook
wb = load_workbook(filename='Vystrel.xlsx')
ws = wb['Лист1']
n = 1
for row in ws.rows:
    for cell in row:
        if cell.value is not None:
            if n < 10:
                o = open('./Corpus/Vystrel/Original/' + str(0) + str(0) + str(n) + '.txt', 'w', encoding='utf-8')
                print(cell.value)
                print('\n\n')
                o.write(cell.value)
                o.close()
            if 9 < n < 100:
                o = open('./Corpus/Vystrel/Original/' + str(0) + str(n) + '.txt', 'w', encoding='utf-8')
                print(cell.value)
                print('\n\n')
                o.write(cell.value)
                o.close()
            if n > 99:
                o = open('./Corpus/Vystrel/Original/' + str(n) + '.txt', 'w', encoding='utf-8')
                print(cell.value)
                print('\n\n')
                o.write(cell.value)
                o.close()
            n += 1
