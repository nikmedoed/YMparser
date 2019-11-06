from selenium import webdriver
from time import sleep
import random


def getInfo(browser, link):
    while 1:
        while 1:
            try:
                time = random.randint(1, 250)
                sleep(time)
                browser.get(link)
                browser.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/h1/a")
            except:
                print('хьюстон, нас банят эгэйн при попытке посмотреть самик. Пауза =', time)
            else:
                break
        try:
            i = lambda x: x.text
            a = list(map(i, browser.find_elements_by_class_name('n-product-spec__name-inner')))
            b = list(map(i, browser.find_elements_by_class_name('n-product-spec__value-inner')))
            info = dict(zip(a, b))
            info["Ссылка"] = link
            print(info)
            return info
        except:
            pass


if __name__ == "__main__":
    browser = webdriver.Chrome()
    print(getInfo(browser, 'https://market.yandex.ru/product--gorodskoi-samokat-reasfalto-predator-230/1967862107/spec?track=tabs'))

