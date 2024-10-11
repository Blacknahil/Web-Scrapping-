from urllib.request import urlopen
from bs4 import BeautifulSoup
# import lxml


html=urlopen('http://www.pythonscraping.com/pages/page1.html')
html_content=html.read()
# print(html_content)


# built in statndard html parser
bs_html_parser= BeautifulSoup(html_content, 'html.parser')
# print(bs_html_parser.div)
print(bs_html_parser.prettify())

# external c library forgiving html mistakes correcting faster tho
bs_lxml= BeautifulSoup(html_content,"lxml")
# print(bs_lxml.div)
# print(bs_lxml.prettify())



# a thrid approach of parsing html is using html5lib a c external library
# slower than both lxml and html.parser.
# for messy or handwritten HTML sites.

bs_html5lib = BeautifulSoup(html_content,"html5lib")
# print(bs_html5lib.h1)
print(bs_html5lib.prettify())


