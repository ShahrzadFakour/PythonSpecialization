from urllib.request import urlopen
import urllib.error , urllib.parse
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  sumNum=0
  address=input("Enter addres:")
  if len(address) < 1 : break
  data= urlopen(address,context=ctx).read()
  tree=ET.fromstring(data)
  counts=tree.findall('.//count')
  for count in counts:
    value=int(count.text)
    sumNum+= value
  print(sumNum)
