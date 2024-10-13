from urllib.request import urlopen
from bs4 import BeautifulSoup
import random,re,datetime
from urllib.parse import urlparse

pages=set()
random.seed(datetime.datetime.now().timestamp())


def getInternalLinks(bs,includeUrl):
    includeUrl='{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    
    internalLinks=set()
    
    possibleLinks=bs.find_all("a", href=re.compile('^(/|.*' + includeUrl+ ')'))
    
    for link in possibleLinks:
        cur=link.attrs["href"]
        if cur and cur not in internalLinks:
            if cur.startswith('/'):
                internalLinks.add(includeUrl+cur)
            else:
                internalLinks.add(cur)
        
    
    return list(internalLinks)



def getExternalLinks(bs,excludeUrl):
    externalLinks=set()
    
    possibleLinks=bs.find_all('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$'))
    
    for link in possibleLinks:
        if link.attrs["href"] and link.attrs['href'] not in externalLinks:
            externalLinks.add(link.attrs["href"])
    
    # print("external links", externalLinks)
    return list(externalLinks)


def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bs=BeautifulSoup(html.read(),"html.parser")
    
    externalLinks=getExternalLinks(bs,urlparse(startingPage).netloc)
    # print(externalLinks)
    # return
    
    if len(externalLinks)==0:
        print("No external links found, looking around the site for one")
        print("-"*40)
        
        domain='{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        
        internalLinks=getInternalLinks(bs,domain)
        
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
    




def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink(startingSite)
    print("Random External Link:",externalLink)
    followExternalOnly(externalLink)



followExternalOnly("http://oreilly.com")