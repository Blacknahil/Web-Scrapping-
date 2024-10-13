from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    
    html=urlopen("http://www.pythonscraping.com/pages/page3.html")
    html_content=html.read()

    bs=BeautifulSoup(html_content,"html.parser")

    twoAttrTags=bs.find_all( lambda tag: len(tag.attrs)==2)

    for ele in twoAttrTags:
        print(ele.attrs)
except Exception as e:
    print(f"An error occured: {e}")