import bs4 as bs
import urllib.request

def function(type):
	y = ""
	for x in type:
		y += str(x.text)
	y+=";"
	return(y)

def lister(tolist):
	retlist = []
	for cont in tolist:
		retlist.append(''.join(cont.findAll(text=True)))
	return retlist

class run():
	letterlist = [";","A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0"]
	def __init__(self,link):
		filename = "ricardo_scraping_data_1.csv"
		f = open(filename, "a")
		liste = []
		stringlist = ""
		sauce = urllib.request.urlopen(link)
		soup = bs.BeautifulSoup(sauce, 'lxml')

		make = soup.find_all('span', {'class' : 'jss170 jss172'})

		value = soup.find_all('span', {'class' : 'jss172'})

		if len(make) == 0:
			make = soup.find_all('span', {'class' : 'label'})
			value = soup.find_all('span', {'class' : 'value'})
		make=lister(make)
		value=lister(value)
		self.comblist = []
		for x in range(len(make)):
			print(x)
			self.comblist.append((make[x],value[x]))
		#f.write(str(self.pricestring+self.markestring+self.modelstring+self.regstring+self.kmstring+self.fueltstring+self.fuelcstring+self.pstring+self.cubicstr+self.bodystr+self.outcstr+self.doorstr+self.seatstr+self.wthstr+self.transstr+self.wheelstr))
		#f.write(lb)
		#f.close()
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
