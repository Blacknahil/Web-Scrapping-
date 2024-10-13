from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
html_content=html.read()

bs= BeautifulSoup(html_content,"html.parser")

article_tags=bs.find('div',{"id":"bodyContent"}).find_all("a",href=re.compile('^(/wiki/)((?!:).)*$'))

for link in article_tags:
    if "href" in link.attrs:
        print(link.attrs["href"])

        
        
