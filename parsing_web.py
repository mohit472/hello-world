import requests
from bs4 import BeautifulSoup
response=requests.get('https://en.wikipedia.org/wiki/SQL_injection')
html= response.text

soup=BeautifulSoup(html,'html.parser')
print soup
print soup.prettify()
