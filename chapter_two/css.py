from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
html_content=html.read()
bs=BeautifulSoup(html_content,"html.parser")
# print(bs.prettify())
nameList=bs.find_all("span", {"class": "red"})
# print(len(nameList))
# for name in nameList:
#     print("\n", name.get_text())


# headers=bs.find_all(["h1","h2","h3","h4","h5","h6"])


# for header in headers:
#     print(header.get_text())



# how many times does a specific text exists in an html page

# prince=bs.find_all("span",{"class":"red"},string="The prince")
# for pr in prince:
#     print(pr)
    
    
# how to use an attribute or 

redOrGreen=bs.find_all(["span","h1","h2"])
print(len(redOrGreen))


# how to use an attribute anding in searching a beautiful soup object 


redAndGreen= bs.find_all("span",{"class":"red","class":"green"})

for ele in redAndGreen:
    print(ele)
    
