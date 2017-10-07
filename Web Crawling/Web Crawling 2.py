import requests
from bs4 import BeautifulSoup
import os

#created by saria goudarzvand
def search_spider(sea, lim):
    url = "https://en.wikipedia.org/w/index.php?limit="+lim+"&offset=0&search="+sea
    url2= "https://www.youtube.com/results?search_query="
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    result_list = soup.findAll('div', {'class': "mw-search-result-heading"})

    print(source_code,"finder1")
    print(plain_text,"finder2")
    print(soup,"finder3")
    print(result_list,"finder4")

    for div in result_list:
        link = div.find('a')
        href = "https://en.wikipedia.org"+link.get('href')
        if (link.get('href').startswith("http")):
            href=link.get('href')
        get_data(href)


def get_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    body = soup.find('div', {'class': 'mw-parser-output'})
    print(body.text)

search = input('type something to search in wiki: ')
limit = input('how many results do you want to get?: ')

if not os.path.exists(search):
    print("Creating folder " + search)
    os.makedirs(search)

searc = search.replace(' ', '+')
search_spider(searc, limit)