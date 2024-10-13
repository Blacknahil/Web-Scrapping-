from  urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
count=0
def getLinks(pageUrl,depth):
    global pages,count
    # to prohibit the recursion from going deep and continue infinitely
    if depth>=5:
        return 
    # open html
    try:
        
        html=urlopen("http://en.wikipedia.org{}".format(pageUrl))
        # create a beautiful soup object 
        bs=BeautifulSoup(html.read(),"html.parser")
        # find all the starts with wiki domain in their address 
        found_links=bs.find_all("a",href=re.compile('^(/wiki/)'))
        for link in found_links:
            # check if it is a link href in attrs of link or whatever we are iterating through
            # check if it is not visited yet
            if 'href' in link.attrs and link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                count+=1
                print(newPage,"depth",depth,"count=",count)
                pages.add(newPage)
                
                # print(pages)
                # add to visited 
                # go and crawl this link 
                getLinks(newPage,depth+1)
    except Exception as e:
        print(f"Excpetion occured: {e}")
        return 

getLinks('',0)


    