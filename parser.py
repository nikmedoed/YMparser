from datetime import datetime

from getData import getLinks
from getTable import getTab

with open("toParse.txt", "r", encoding="utf8") as f:
    toParse = list(map(lambda x: x.split(), f.read().split('\n')))

for i in toParse:
    print(datetime.now(), i[0], "- старт")
    links = getLinks(i[0], i[1])
    # getTab(i[0], links)
    print(datetime.now(), i[0], "- закончил")
