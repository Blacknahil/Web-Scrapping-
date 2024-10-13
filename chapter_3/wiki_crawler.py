from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random


def crawl(address):
    assert "/wiki" in address
    html=urlopen(f'http://en.wikipedia.org{address}')
    html_content=html.read()
    bs= BeautifulSoup(html_content,"html.parser")
    article_tags=bs.find('div',{"id":"bodyContent"}).find_all("a",href=re.compile('^(/wiki/)((?!:).)*$'))
    print("\n \n \n")
    print(f"New source{address}")
    print("\n \n \n \n")
    res=[]
    for link in article_tags:
        if "href" in link.attrs:
            print(link.attrs["href"])
            res.append(link.attrs["href"])
    print("\n \n \n")
    return res




def main():
    print("insert the address you want to crawl")
    url=""
    while not url:
        url=input()
        
    assert "wikipedia.org/wiki/" in url
    arr=url.split("/")
    link=f"/wiki/{arr[-1]}"
    while link:
        links=crawl(link)
        if not links:
            print("empty array of links")
            print("\n")
        rand=random.choice(links)
        link=rand



if __name__=="__main__":
    main()




    



    
    

        