from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

my_url = ""
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


