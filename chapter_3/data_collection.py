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
        try:
            print("header=",bs.h1.get_text())
            print("first paragraph= ", bs.find(id="mw-content-text").find_all('p')[0])
            print("Edit Links",bs.find(id='ca-edit').find('span').find('a').attrs["href"])
            
        except AttributeError as e:
            print(f"attribute error: {e}")
        except Exception as e:
            print(f"Exception occured: {e}")
            
        found_links=bs.find_all("a",href=re.compile('^(/wiki/)'))
        for link in found_links:
            # check if it is a link href in attrs of link or whatever we are iterating through
            # check if it is not visited yet
            if 'href' in link.attrs and link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                count+=1
                print(newPage,"depth",depth,"count=",count)
                print('-'*20)
                pages.add(newPage)
                
                # print(pages)
                # add to visited 
                # go and crawl this link 
                getLinks(newPage,depth+1)
    except Exception as e:
        print(f"Excpetion occured: {e}")
        return 

getLinks('',0)


    