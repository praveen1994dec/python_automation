#In DevOps it is used for log analysis/processing
#pip install beautifulsoup4


import urllib.request
from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        print(sp)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()


#Creating a class
class cloud:
    def __init__(self, value):
        self.value = value

#Method inside a class
    def hello(self):
        print(self.value)

#calling aclass with method
test="DevOps a gaya"
cloud(test).hello()