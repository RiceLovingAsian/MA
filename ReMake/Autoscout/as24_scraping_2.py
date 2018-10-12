import bs4
import as24_scraping_1 as as24s
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
import db
db.createdb()
carlist = []

for x in range(1,4000):
	my_ulr = "https://www.autoscout24.ch/de/autos/alle-marken?page={}&st=1&vehtyp=10".format(x)
	uClient = ureq(my_ulr)

	myData = uClient.read()

	uClient.close

	page_soup = soup(myData, "html.parser")

	articles = page_soup.findAll("a",  {"class" : "primary-link"}, href= True)

		
	
							#print(car.markestring,car.modelstring)
	
	for a in articles:
		print('https://www.autoscout24.ch/{}'.format(str(a['href'])))
		car = as24s.run('https://www.autoscout24.ch/{}'.format(str(a['href'])))	
		if car.findict['preis'.encode()]>400000:print('*************************')
		if not car.quitit:db.insert(car)


print('************************************************')
print('Finished scraping Autoscout24 database\nThe local db contains {} entries'.format(db.showcount()))
print('************************************************')