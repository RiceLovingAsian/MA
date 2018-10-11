import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
carlist = []
filename = "ricardo_scraping_test_1.csv"
f = open(filename, "w")
headers = ["Preis;Marke;Modell;Registrationdate;Kilometers;Fueltype; fuelconsumption ; performance ;cubiccapacity;bodytype; outsidecolor ;numberofdoors;numberofseats ;emptyweight; transmissiontype;drivingwheels \n"]
f.write(headers[0])
f.close()
count = 0
for x in range(1,400):
	print('BRAND {}'.format(x))
	for z in range(1,300):
		my_ulr = str("https://auto.ricardo.ch/de/s?make="+str(x)+"&offer_type=classified&sort_type=registration_date&sort_order=asc&page="+str(z))

		uClient = ureq(my_ulr)

		myData = uClient.read()

		uClient.close

		page_soup = soup(myData, "html.parser")

		articles = page_soup.findAll("a",  {"class" : "ric-article"}, href= True)

			
		
								#print(car.markestring,car.modelstring)
		count += len(articles)
		print(count)

		if len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect ric-layout__small--hide'}))==0 and len(page_soup.findAll('button',{'class':'ric-pagination__button mdl-js-button mdl-js-ripple-effect'}))==0:
			break