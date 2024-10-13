from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random,datetime



# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# new=datetime.datetime.now().timestamp()
# print(new,type(new))

random.seed(datetime.datetime.now().timestamp())

def getLinks(articleUrl):
    try:
        
        html=urlopen("http://en.wikipedia.org{}".format(articleUrl))
        bs=BeautifulSoup(html,"html.parser")
        
        return bs.find("div",{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
    except Exception as e:
        print(f"An exception has occured:{e}")
        return []


links=getLinks('/wiki/Kevin_Bacon')

while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getLinks(newArticle)

