import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i=1
a=[]
j=input("enter the position:")
j=int(j)
j=j-1
tags = soup('a')
count=input("enter the count:")
while(i<=int(count)):
 a[:]=[]
 for tag in tags:
  a.append(tag.get('href', None))
 url=a[j]
 html = urllib.request.urlopen(url, context=ctx).read()
 soup = BeautifulSoup(html, 'html.parser')
 tags = soup('a')
 i=i+1
print(a[j])

