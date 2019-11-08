from selenium import webdriver
from time import sleep
import random
from datetime import datetime

def getLinks(name, link):
    browser = webdriver.Chrome()
    browser.get(link)
    sleep(random.randint(5, 20))
    links = []
    print("start")
    while 1:
        lis = browser.find_elements_by_xpath('//div[4]/div[1]/div[1]/a')
        links.extend(list(map(lambda x: x.get_attribute('href'), lis)))

        # https://riptutorial.com/selenium-webdriver/example/28140/scrolling-using-python
        # if lis: lis[random.randint(len(lis))].


        next = browser.find_element_by_class_name('n-pager__button-next').get_attribute('href')
        while next:
            try:
                sleep(random.randint(1, 250))
                browser.get(next)
                print(datetime.now(), "- next")
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

