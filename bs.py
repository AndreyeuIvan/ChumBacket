from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReg

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#oppening connection, grabbing the page
 uClient=uReg(my_url)
 page_html = uClient.read()
 uClient.close()
 page_soup=soup(page_html, 'html.parser')

#grab video cards
 page_soup.findAll('div', {'class':'item-container'})
 container = page_soup.findAll('div', {'class':'item-container'})
 len(container)

 print(container)