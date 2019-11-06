from selenium import webdriver
from time import sleep
import random
import json

def getInfo(browser, link):
    while 1:
        while 1:
            try:
                time = random.randint(1, 250)
                sleep(time)
                browser.get(link)
                browser.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/h1/a")
            except:
                print('хьюстон, нас банят эгэйн при попытке посмотреть этот товар. Пауза =', time)
            else:
                break
        try:
            i = lambda x: x.text
            cost = browser.find_element_by_xpath('//*[@id="n-product-default-offer"]/div[1]/div[2]/span/span').text
            name = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[3]/div[1]/div/div[1]/h1/a').text
            a = list(map(i, browser.find_elements_by_class_name('n-product-spec__name-inner')))
            b = list(map(i, browser.find_elements_by_class_name('n-product-spec__value-inner')))
            info = dict(zip(a, b))
            info["Ссылка"] = link
            info["Цена"] = cost
            info["Название"] = name
            with open("rowdata.txt", 'a', encoding="utf8") as f:
                f.write(json.dumps(info, ensure_ascii=False))
                f.write("\n")
            print(info['Название'], info['Цена'], info['Ссылка'])
            return info
        except:
            pass


if __name__ == "__main__":
    browser = webdriver.Chrome()
    print(getInfo(browser, 'https://market.yandex.ru/product--gorodskoi-samokat-reasfalto-predator-230/1967862107/spec?track=tabs'))
    browser.close()

