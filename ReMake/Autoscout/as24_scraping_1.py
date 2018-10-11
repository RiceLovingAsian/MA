#coding = utf-8
import bs4 as bs
import urllib.request
import filter as filthy
import db,re
ATTRS = ('modell',
	'kilometer',
	'ps',
	'leergewicht',
	'getriebeart',
	'hubraum',
	'antriebsart',
	'anzahl türen',
	'anzahl sitze',
	'kraftstoff',
	'verbrauch')
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

def lister(tolist,whichitem=0):
	retlist = []
	try:
		for cont in tolist:
			retlist.append(''.join(cont.findAll(text=True)))
		return retlist
	except:
		return False
def getcont(text):
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
			for x in self.findict.keys():print(x,'------',self.findict[x])
