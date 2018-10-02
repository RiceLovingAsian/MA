from bs4 import BeautifulSoup as  soup 
from urllib.request import urlopen as uReq

my_url = "https://www.veromoda.com/ch/de/vm/kategorie-waehlen/kleider/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")



filename = "Vera_Moda_Scraping_Results.csv"
f = open(filename, "w")

headers = "name, preis\n" 

f.write("")



for i in range(0,20):

	a = page_soup.findAll("a", {"class":"product-tile__name__link"})
	name = a[i].text

	b = page_soup.findAll("em", {"class":"value__price"})
	preis = b[i].text

	
	print("name: " + a[i].text)
	print("preis: " + a[i].text)
	
	f.write(name + "," + preis + "\n")

f.close()