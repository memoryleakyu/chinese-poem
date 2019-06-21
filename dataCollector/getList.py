import os
from bs4 import BeautifulSoup

path = './poets'
for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        poet = os.path.splitext(fname)[0]
        html_object = open('poets/'+poet+'.htm','rb').read().decode(encoding='gbk')
        soup = BeautifulSoup(html_object,'html.parser')
        poem = soup.find_all('p')[3:]

        f = open('poem/'+poet+'.txt','w')
        for item in poem:
            f.write(item.get_text())