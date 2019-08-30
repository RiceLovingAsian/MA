import bs4
import as24_scraping_1 as as24s 
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup 

#Datenbank wird erstellt mit dem Modul db , Socket wird importiert um das socket-Problem zu beheben
import db,socket
db.createdb()
carlist = []
count = 0
stopit = False
for x in range(1,4000):
	my_ulr = "https://www.autoscout24.ch/de/autos/alle-marken?page={}&st=1&vehtyp=10".format(x)
	try:uClient = ureq(my_ulr)
	except socket.gaierror:stopit = True
	if stopit:
		stopit=False
	else:
		myData = uClient.read()

		uClient.close

		page_soup = soup(myData, "html.parser")

		articles = page_soup.findAll("a",  {"class" : "primary-link"}, href= True)

			
		#run nimmt als Argument den ganzen Link, hier werden die Teile der Links zusammengesetzt.
		for a in articles:
			count+=1
			print('Inserat {}'.format(count))
			print('https://www.autoscout24.ch{}'.format(str(a['href'])))
			car = as24s.run('https://www.autoscout24.ch{}'.format(str(a['href'])))	
			if not car.quitit:db.insert(car)


print('************************************************')
print('Finished scraping Autoscout24 database\nThe local db contains {} entries'.format(db.showcount()))
print('************************************************')