from collections import defaultdict
from bs4 import BeautifulSoup
import requests
import sys
import os
import io
import time 




actors = defaultdict(list)
for i in range(10):
    URL = "https://myanimelist.net/topanime.php?type=bypopularity& "
    num = i * 50
    URL = URL + 'limit=' + str(num)
    print(URL)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    tr_elements = soup.find_all("tr", class_='ranking-list')
    j = 0
    for tr in tr_elements:

        link = tr.find(
            "td", class_='title al va-t word-break').find('a', href=True)

        title = tr.find(
            "div", class_='di-ib clearfix').find('a').text
        print(title)
        link = link['href']
        newURL = link + "/characters"
        newPage = requests.get(newURL)
        newSoup = BeautifulSoup(newPage.content, 'html.parser')
        soupStr = str(newSoup.encode('utf-8'))

        index1 = (soupStr).rindex(
            "<h2")
        index2 = soupStr.rindex(
            "</td"
        )
        soupStr = soupStr[:index1] + soupStr[index2:]
        newSoup = BeautifulSoup(soupStr, 'html.parser')
        tables = newSoup.find('table').find(
            'td', valign="top", style='padding-left: 5px;')
        rows = tables.find_all('tr')
        for row in rows:
            std = row.find('td', align="right")
            for names in std.find_all('tr'):
                subStd = names.find('td')
                if(subStd.find('small').text == 'Japanese'):
                    name = subStd.find('a').text
                if title not in actors[name]:
                    actors[name].append(title)
        j = j + 1
        time.sleep(2)
with open('names2', 'w', encoding='utf-8') as f:
    for key in actors:
        f.write(key + ': ')
        for i, item in enumerate(actors[key]):
            if i:
                f.write(', ')
            f.write('%s' % item)

        f.write("\n")
    f.close()
