#coding = utf-8
import bs4 as bs
import urllib.request
import filter as filthy
import db,re
def function(type):
	y = ""
	for x in type:
		y += str(x.text)
	y+=";"
	return(y)
def cleaner(toclean):
	toclean = toclean.replace(('\n'),'')
	toclean = toclean.replace(('\r'),'')
	toclean = toclean.replace('é','e')
	toclean = toclean.replace('ü','ue')
	toclean = toclean.replace('ä','ae')
	p = re.compile(" {2}")
	a = re.sub(p,"",toclean)
	return a
def gettheduckingstring(tostring):
	return str(tostring.decode())

def lister(tolist,whichitem=0):
	retlist = []
	
	for cont in tolist:
		retlist.append(''.join(cont.findAll(text=True)))
	return retlist
	#except:
	#	return False
def getcont(text,price=False):
	if price:
		p = re.compile(".+?(?=.-)")
		text=(p.search(text.decode()).group())
	permitls = ['1','2','3','4','5','6','7','8','9','0']
	retls = filter(lambda x:x in permitls,str(text))
	retls = list(retls)
	retstr = ""
	for x in retls:
		retstr += x
	try:return int(retstr)
	except: return("-")

def getverb(toverb):
	return gettheduckingstring(toverb).split('/')[2].split('(')[0]
class run():
	def __init__(self,link):
		self.quitit = False
		self.findict = dict()
		liste = []
		stringlist = ""
		try:sauce = urllib.request.urlopen(link)
		except:
			self.quitit=True
		if not self.quitit:
			soup = bs.BeautifulSoup(sauce, 'lxml')
			prop = soup.find_all('div', {'class' : 'prop'})
			value = soup.find_all('div', {'class' : 'value'})
			self.arttitle = cleaner(soup.select('h1.title-main')[0].text.strip().split('(')[0])
			self.brand = filthy.getbrand(self.arttitle)
			self.modell = filthy.getmodel(self,self.arttitle)
			self.findict['brand'.encode()] = self.brand
			self.findict['modell'.encode()] = self.modell
			prop=lister(prop)
			value=lister(value)
			self.comblist = []
			for x in range(len(prop)):
				self.comblist.append((prop[x],value[x]))
			for x in self.comblist:
				#if cleaner(x[0]).lower() in ATTRS:
				self.findict[cleaner(x[0]).lower().encode()]=cleaner(x[1]).encode()
			self.findict['preis'.encode()]=getcont(self.findict['preis'.encode()],True)
			self.findict['kilometer'.encode()] = getcont(self.findict['kilometer'.encode()])
			try:self.findict['leergewicht'.encode()] = getcont(self.findict['leergewicht'.encode()])
			except: self.findict['leergewicht'.encode()]='N/a'
			try:self.findict['hubraum'.encode()] = getcont(self.findict['hubraum'.encode()])
			except:
				try:
					if self.findict['treibstoff'.encode()] == 'Elektro':
						self.findict['hubraum'.encode()] = 'E-Auto'
					else:
						self.findict['hubraum'.encode()] = 'N/a'
				except:
					try:
						if self.findict['treibstoff'] == 'Elektro':
							self.findict['hubraum'.encode()] = 'E-Auto'
						else:
							self.findict['hubraum'.encode()] = 'N/a'
					except:
						self.findict['treibstoff'] = 'N/a'
						self.findict['hubraum'] = 'N/a'
			try:self.findict['ps'.encode()] = getcont(self.findict['ps'.encode()])
			except:
				try:self.findict['ps'] = getcont(self.findict['ps'])
				except:self.findict['ps'] = 'N/a'

			try:self.findict['tueren'.encode()] = gettheduckingstring(self.findict['tueren'.encode()])
			except:
				try:self.findict['tueren']=gettheduckingstring(self.findict['tueren'])
				except:self.findict['tueren']='N/a'
			try:self.findict['sitze'.encode()] = gettheduckingstring(self.findict['sitze'.encode()])
			except:
				try:self.findict['sitze']=gettheduckingstring(self.findict['sitze'])
				except:self.findict['sitze']='N/a'
			try:self.findict['treibstoff'.encode()] = gettheduckingstring(self.findict['treibstoff'.encode()])
			except:
				try:self.findict['treibstoff'] = gettheduckingstring(self.findict['antriebsart'])
				except: self.findict['treibstoff']='N/a'
			try:self.findict['antriebsart'.encode()] = gettheduckingstring(self.findict['antriebsart'.encode()])
			except:
				try:self.findict['antriebsart'] = gettheduckingstring(self.findict['antriebsart'])
				except: self.findict['antriebsart']='N/a'
			try:self.findict['getriebeart'.encode()] = gettheduckingstring(self.findict['getriebeart'.encode()])
			except:
				try:self.findict['getriebeart'] = gettheduckingstring(self.findict['getriebeart'])
				except:self.findict['getriebeart'.encode()]='N/a'
			try:self.findict['verbrauch in l/100 km'.encode()] = getverb(self.findict['verbrauch in l/100 km'.encode()])
			except:
				try:self.findict['verbrauch in l/100 km'] = getverb(self.findict['verbrauch in l/100 km'])
				except:self.findict['verbrauch in l/100 km'] = 'N/a'
			try:self.findict['getriebeart'.encode()]
			except:
				try:
					if self.findict['treibstoff'.encode()] == 'Elektro':
						self.findict['verbrauch in l/100 km'.encode()] = 'E-Auto'
					else:
						self.findict['verbrauch in l/100 km'.encode()] = 'N/a'
				except:
					if self.findict['treibstoff'] == 'Elektro':
						self.findict['verbrauch in l/100 km'.encode()] = 'E-Auto'
					else:
						self.findict['verbrauch in l/100 km'.encode()] = 'N/a'
