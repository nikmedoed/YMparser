from selenium import webdriver
from time import sleep
import string
import random
import xlwt
from getInfo import getInfo
import datetime

def getLinks(name, link):
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(random.randint(1, 250))
    links = []
    print("start")
    while 1:
        lis = browser.find_elements_by_class_name('n-snippet-cell2__image')
        links.extend(list(map(lambda x: x.get_attribute('href'), lis)))
        next = browser.find_element_by_class_name('n-pager__button-next').get_attribute('href')
        while next:
            try:
                sleep(random.randint(1, 250))
                browser.get(next)
            except:
                print('хьюстон, нас банят эгэйн')
            else:
                break
    links = list(map(lambda x: x.split('?')[0] + "/spec?track=tabs", links))
    with open('links\\' + name + '.txt', 'w') as s:
        s.write("\n".join(links))
    browser.close()
    return links

if __name__ == "__main__":
    print(getLinks("Стиралки",
                   "https://market.yandex.ru/catalog--stiralnye-mashiny/54913/list?onstock=1&local-offers-first=0"))

