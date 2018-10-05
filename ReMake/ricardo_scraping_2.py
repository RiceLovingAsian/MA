import bs4
import ricardo_scraping_1 as rst
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
import db
db.createdb()
carlist = []
filename = "ricardo_scraping_test_1.csv"
f = open(filename, "w")
headers = ["Preis;Marke;Modell;Registrationdate;Kilometers;Fueltype; fuelconsumption ; performance ;cubiccapacity;bodytype; outsidecolor ;numberofdoors;numberofseats ;emptyweight; transmissiontype;drivingwheels \n"]
f.write(headers[0])
f.close()

for x in range(1,90):
	print('BRAND {}'.format(x))
	for z in range(1,300):
		print('PAGE {}'.format(z))
		my_ulr = str("https://auto.ricardo.ch/de/s?make="+str(x)+"&offer_type=classified&sort_type=registration_date&sort_order=asc&page="+str(z))

		uClient = ureq(my_ulr)

		myData = uClient.read()

		uClient.close

		page_soup = soup(myData, "html.parser")

		articles = page_soup.findAll("a",  {"class" : "ric-article"}, href= True)

			
		
								#print(car.markestring,car.modelstring)
		
		for a in articles:
			if str(a['href'])[0]=='/':
				car = rst.run('https://auto.ricardo.ch'+str(a['href']))
			else:
				car = rst.run(str(a["href"]))
			if car.quitit:break
			db.insert(car)

		if len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect ric-layout__small--hide'}))==0 and len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect'}))==0:
			break