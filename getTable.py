from selenium import webdriver
from time import sleep
import string
import random
import xlwt
from getInfo import getInfo
import datetime

# из берет файл со ссылками на товары и преобразует в таблицу с характеристиками
def getData():
    browser = webdriver.Chrome()
    book = xlwt.Workbook(encoding="utf-8")
    sh = book.add_sheet()
    with open('links.txt', 'r') as s:
        links = s.read().split('\n')

    infos = list(map(lambda x: getInfo(browser, x), links))
    tabs = set()
    for i in infos:
        tabs.update(set(i.keys()))
    tabs = list(tabs)

    rows = len(infos)
    for i in range(len(tabs)):
        col = tabs[i]
        sh.write(0, i, col)
        for j in range(rows):
            sh.write(j + 1, i, infos[j].get(col))

    book.save(str(datetime.datetime.today()).replace(":", "=")+".xls")
    browser.close()

if __name__ == "__main__":
    print(getData())

