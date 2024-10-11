from urllib.request import urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html=urlopen(url)
        html_content=html.read()
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print(e)
        return None
    try: 
        bs=BeautifulSoup(html_content,'html.parser')
        title=bs.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title

url="http://www.pythonscraping.com/pages/page1.html"
title= get_title(url)
if title==None:
    print("Title could not be found")
else:
    print("Title is found:",title)