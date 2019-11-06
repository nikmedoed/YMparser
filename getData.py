from selenium import webdriver
from time import sleep
import string
import random
import xlwt
from getInfo import getInfo
import datetime

def getLinks():
    with open("toParse.txt", "r") as f:

    link = "https://market.yandex.ru/catalog--samokaty/54700/list?hid=7070735&glfilter=7081037%3A11854638&glfilter=7081038%3A11854645&glfilter=7083283%3A11854650&glfilter=7083337%3A85~&onstock=1&local-offers-first=0"
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
    with open('links.txt', 'w') as s:
        s.write("\n".join(links))
    browser.close()

if __name__ == "__main__":
    print(getLinks())

