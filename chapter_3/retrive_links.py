from urllib.request import urlopen
from bs4 import BeautifulSoup


html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
html_content=html.read()

bs= BeautifulSoup(html_content,"html.parser")

a_tags=bs.find_all('a')

for link in a_tags:
    if "href" in link.attrs:
        print(link.attrs["href"])
        
        
