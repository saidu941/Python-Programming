import requests
from bs4 import BeautifulSoup
import os

search = input('type something to search in wiki: ')
searc = search.replace(' ', '+')

url= "https://en.wikipedia.org/wiki/"+searc
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

#print(source_code,"source code printed")
#print(plain_text,"plain text printed")
#print(soup,"soup printed")

result_list1 = soup.findAll('div')
print(result_list1,"result set printed")

for div in result_list1:
    r1=div.findAll('h1')
print(r1)

for div in result_list1:
    r2=div.findAll('body')
print(r2)
