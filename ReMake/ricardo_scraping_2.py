import bs4
import ricardo_scraping_1 as rst
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 
carlist = []
filename = "ricardo_scraping_test_1.csv"
f = open(filename, "w")
headers = ["Preis;Marke;Modell;Registrationdate;Kilometers;Fueltype; fuelconsumption ; performance ;cubiccapacity;bodytype; outsidecolor ;numberofdoors;numberofseats ;emptyweight; transmissiontype;drivingwheels \n"]
f.write(headers[0])
f.close()
for x in range(1,90):
	print(x)
	for z in range(1,300):
		print(z)
		my_ulr = str("https://auto.ricardo.ch/de/s?make="+str(x)+"&offer_type=classified&sort_type=registration_date&sort_order=asc&page="+str(z))

		uClient = ureq(my_ulr)

		myData = uClient.read()

		uClient.close

		page_soup = soup(myData, "html.parser")

		articles = page_soup.findAll("a",  {"class" : "ric-article"}, href= True)
		if articles==[]:
			break
		else:
			for a in articles:
				car = rst.run('https://auto.ricardo.ch/'+str(a["href"]))
				print(car.comblist)
				#print(car.markestring,car.modelstring)
