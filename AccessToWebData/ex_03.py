from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl,re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link=urlopen('http://py4e-data.dr-chuck.net/comments_1085768.html' , context=ctx).read()
soup=BeautifulSoup(link,'html.parser')
tags=soup('span')
sumOf=0
for tag in tags:
    y=re.findall('[0-9]+',str(tag))
    for i in y:
        num=int(i)
        sumOf=sumOf+num
print(sumOf)
