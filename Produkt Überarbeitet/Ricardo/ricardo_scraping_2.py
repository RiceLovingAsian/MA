import bs4
import ricardo_scraping_1 as rst
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
import db
db.createdb()
carlist = []
filename = "ricardo_scraping_test_1.csv"

#badbrands beinhalten Fahrzeuge wie Motorräder, Wohnmobile und weiteres. Diese Fahrzeugarten sind nicht relevant und werden deshalb aussortiert.
badbrands=(121,141,158,154,172,181,195,198,208,255,287,293,299,290,341)
for x in range(1,401):
	print('BRAND {}'.format(x))
	for z in range(1,300):
		if x in badbrands:break
		print('PAGE {}'.format(z))
		my_ulr = str("https://auto.ricardo.ch/de/s?make="+str(x)+"&offer_type=classified&sort_type=registration_date&sort_order=asc&page="+str(z))

		uClient = ureq(my_ulr)

		myData = uClient.read()

		uClient.close

		page_soup = soup(myData, "html.parser")

		articles = page_soup.findAll("a",  {"class" : "ric-article"}, href= True)

			
		
		#Riccardo besitzt Strings mit ganzen und halben URL's. Es wird getestet ob die URL ganz ist. Danach  werden die URL's welche nicht vollständig sind ergänzt.						
		for a in articles:
			if str(a['href'])[0]=='/':
				car = rst.run('https://auto.ricardo.ch'+str(a['href']))
			else:
				car = rst.run(str(a["href"]))
			
			if not car.quitit:db.insert(car)

		if len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect ric-layout__small--hide'}))==0 and len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect'}))==0:
			break
print('************************************************')
print('Finished scraping Ricardo database\nThe local db contains {} entries'.format(db.showcount()))
print('************************************************')