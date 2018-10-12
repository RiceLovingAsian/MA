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
def getthduckingstring(tostring):
	return str(tostring.decode())

def lister(tolist,whichitem=0):
	retlist = []
	try:
		for cont in tolist:
			retlist.append(''.join(cont.findAll(text=True)))
		return retlist
	except:
		return False
def getcont(text,price=False):
	if price:
		print(text.decode())
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
			self.findict['leergewicht'.encode()] = getcont(self.findict['leergewicht'.encode()])
			try:self.findict['hubraum'.encode()] = getcont(self.findict['hubraum'.encode()])
			except:self.findict['hubraum'.encode()] = 'E-Auto'
			self.findict['ps'.encode()] = getcont(self.findict['ps'.encode()])
			try:self.findict['antriebsart'] = getthduckingstring(self.findict['antriebsart'])
			except:self.findict['antriebsart'.encode()] = getthduckingstring(self.findict['antriebsart'.encode()])
			self.findict['getriebeart'.encode()] = getthduckingstring(self.findict['getriebeart'.encode()])
