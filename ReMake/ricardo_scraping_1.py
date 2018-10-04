import bs4 as bs
import urllib.request
import filter
ATTRS = ('modell','kilometer','ps','leergewicht','getriebeart','hubraum','antriebsart','anzahl türen','anzahl sitze','treibstoff','verbrauch')
	
def function(type):
	y = ""
	for x in type:
		y += str(x.text)
	y+=";"
	return(y)

def lister(tolist,whichitem=0):
	retlist = []
	try:
		for cont in tolist:
			retlist.append(''.join(cont.findAll(text=True)))
		return retlist
	except:
		return False
	
class run():
	def __init__(self,link):
		self.quitit = False
		print(link)
		self.findict = dict()
		filename = "ricardo_scraping_data_1.csv"
		f = open(filename, "a")
		liste = []
		stringlist = ""
		sauce = urllib.request.urlopen(link)
		soup = bs.BeautifulSoup(sauce, 'lxml')
		try:self.price = lister(soup.find('div',{'class':'price mdl-typography--font-light'}))[1]
		except: self.price = False
		if self.price:
			try:arttitle = lister(soup.find('div',{'class':'title'}))[0]
			except: arttitle=lister(soup.find('div',{'class':'titleContainer--1koNs'}))[0]
			self.brand = filter.getbrand(arttitle)
			model = filter.getmodel(self,arttitle)
			self.findict['brand'] = self.brand
			self.findict['price'] = self.price
			self.findict['modell']= model
			try:km = lister(soup.find('div',{'class':'mileage item'}))[1]
			except: km = 0
			self.findict['kilometer']=km
			try:hp = lister(soup.find('div',{'class':'power item'}))[1]
			except: hp = 'Unknown'
			self.findict['ps'] = hp
			prop = soup.find_all('span', {'class' : 'jss170 jss172'})

			value = soup.find_all('span', {'class' : 'jss172'})

			if len(prop) == 0:
				prop = soup.find_all('span', {'class' : 'label'})
				value = soup.find_all('span', {'class' : 'value'})
			prop=lister(prop)
			value=lister(value)
			self.comblist = []
			for x in range(len(prop)):
				self.comblist.append((prop[x],value[x]))
			for x in self.comblist:
				if x[0].lower() in ATTRS:
					self.findict[x[0].lower()]=x[1]
		else:
			self.quitit = True
