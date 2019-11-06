from selenium import webdriver
import xlwt
from getInfo import getInfo
import datetime
import json

# берет файл со ссылками (или ссылки) на товары и преобразует в таблицу с характеристиками
def getTab(name, links=None):
    if not links:
        with open('links' + name + '.txt', 'r') as s:
            links = s.read().split('\n')
    browser = webdriver.Chrome()
    book = xlwt.Workbook(encoding="utf-8")
    sh = book.add_sheet()

    infos = list(map(lambda x: getInfo(browser, x), links))
    tabs = set()
    for i in infos:
        tabs.update(set(i.keys()))
    tabs = list(tabs)

    path = 'result' + name + " - " + str(datetime.datetime.today()).replace(":", "=")

    rows = len(infos)
    for i in range(len(tabs)):
        col = tabs[i]
        sh.write(0, i, col)
        for j in range(rows):
            sh.write(j + 1, i, infos[j].get(col))

    with open(path + ".json", "w", encoding="utf8") as write_file:
        json.dump(infos, write_file, ensure_ascii=False)

    book.save(path + ".xls")
    browser.close()

if __name__ == "__main__":
    print(getTab("Стиралки"))

