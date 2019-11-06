import json
import xlwt
import datetime


# конвертирует json в таблицу
toconvert="yamokat.txt"

with open(toconvert, 'r') as r:
    readed = r.read().split('\n')
    infos = list(map(lambda x: json.loads(x), readed))


book = xlwt.Workbook(encoding="utf-8")
sh = book.add_sheet()

tabs = set()
for i in infos:
    tabs.update(set(i.keys()))
tabs = list(tabs)

rows = len(infos)
for i in range(len(tabs)):
    col = tabs[i]
    sh.write(0, i, col)
    for j in range(rows):
        sh.write(j+1, i, infos[j].get(col))

book.save(str(datetime.datetime.today()).replace(":", "=") + ".xls")