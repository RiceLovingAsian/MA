import bs4 as bs
import urllib.request

def function(type):
	y = ""
	for x in type:
		y += str(x.text)
	y+=";"
	return(y)
class run():
	letterlist = [";","A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0"]
	def __init__(self,link):
		filename = "ricardo_scraping_data_1.csv"
		f = open(filename, "a")
		liste = []
		stringlist = ""
		sauce = urllib.request.urlopen(link)
		soup = bs.BeautifulSoup(sauce, 'lxml')

		make = soup.find_all('td', {'data-qa' : 'make'})
		model = soup.find_all('td', {'data-qa' : 'model'})
		registrationdate = soup.find_all('td', {'itemprop' : 'productionDate'})
		kilometers = soup.find_all('td', {'data-qa' : 'kilometers'})
		fueltype = soup.find_all('td', {'data-qa' : 'fueltype'})
		fuelconsumption = soup.find_all('td', {'data-qa' : 'fuelconsumption'})
		performance = soup.find_all('td', {'data-qa' : 'performance'})
		cubiccapacity = soup.find_all('td', {'data-qa' : 'cubiccapacity'})
		bodytype = soup.find_all('td', {'data-qa' : 'bodytype'})
		outsidecolor = soup.find_all('td', {'itemprop' : 'color'})
		numberofdoors = soup.find_all('td', {'data-qa' : 'numberofdoors'})
		numberofseats = soup.find_all('td', {'data-qa' : 'numberofseats'})
		emptyweight = soup.find_all('td', {'itemprop' : 'weight'})
		transmissiontype = soup.find_all('td', {'data-qa' : 'transmissiontype'})
		drivingwheels = soup.find_all('td', {'data-qa' : 'drivingwheels'})
		price = soup.findAll('p',{'itemprop':'price'}, content=True)

		self.price= function(price)
		self.marke = function(make)
		self.model = function(model)
		self.registrationdate = function(registrationdate)
		self.kilometres = function(kilometers)
		self.fueltype =function(fueltype)
		self.fuelconsumption = function(fuelconsumption)
		self.performance = function(performance)
		self.cubiccapacity = function(cubiccapacity)
		self.bodytype = function(bodytype)
		self.outsidecolor =function(outsidecolor)
		self.numberofdoors= function(numberofdoors)
		self.numberofseats = function(numberofseats)
		self.emptyweight =function(emptyweight)
		self.transmissiontype =function(transmissiontype)
		self.wheels =function(drivingwheels)

		self.pricestring = self.correct(self.price)
		self.markestring = self.correct(string=self.marke)
		self.modelstring = self.correct(self.model)
		self.regstring = self.correct(self.registrationdate)
		self.kmstring = self.correct(self.kilometres)
		self.fueltstring = self.correct(self.fueltype)
		self.fuelcstring = self.correct(self.fuelconsumption)
		self.pstring = self.correct(self.performance)
		self.cubicstr = self.correct(self.cubiccapacity)
		self.bodystr = self.correct(self.bodytype)
		self.outcstr = self.correct(self.outsidecolor)
		self.doorstr = self.correct(self.numberofdoors)
		self.seatstr = self.correct(self.numberofseats)
		self.wthstr = self.correct(self.emptyweight)
		self.transstr = self.correct(self.transmissiontype)
		self.wheelstr = self.correct(self.wheels)
		lb = "\n"

		f.write(str(self.pricestring+self.markestring+self.modelstring+self.regstring+self.kmstring+self.fueltstring+self.fuelcstring+self.pstring+self.cubicstr+self.bodystr+self.outcstr+self.doorstr+self.seatstr+self.wthstr+self.transstr+self.wheelstr))
		f.write(lb)
		f.close()
	def correct(self,string):
		self.string = ""
		self.list = list(string)
		self.listm = list(string)
		self.poptol = 0
		for x in range(0,len(self.list)-1):
			if x-1<0:
				x1 = 0
			else:
				x1 = x-1
			if x+1 >=len(self.list):
				x2 = len(self.list)-1
			else:
				x2 = x+1
			if self.list[x] not in self.letterlist and (self.list[x1] not in self.letterlist or self.list[x2] not in self.letterlist) or self.list[x]=="\n":
				self.listm.pop(x-self.poptol)
				self.poptol += 1

		for x in self.listm:
			self.string = str(self.string+x)
		return(self.string)
