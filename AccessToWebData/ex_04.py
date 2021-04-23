from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl,re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link=urlopen('http://py4e-data.dr-chuck.net/known_by_Peige.html',context=ctx).read()
soup=BeautifulSoup(link,'html.parser')
findLink=soup('a')
for i in range(7):
    interest= findLink[17]
    newLink=urlopen(interest.get('href',None))
    soup=BeautifulSoup(newLink,'html.parser')
    findLink=soup('a')
print(interest.text)
