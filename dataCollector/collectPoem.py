from bs4 import BeautifulSoup

html_object = open('poets/ajian.htm','rb').read().decode(encoding='gb2312')

soup = BeautifulSoup(html_object,'html.parser')


poem = soup.find_all('p')[3:]

f = open('ajian.txt','w')
for item in poem:
    f.write(item.get_text())
