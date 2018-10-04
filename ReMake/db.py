import sqlite3
ATTRS = ('price','brand','modell','kilometer','ps','leergewicht','getriebeart','hubraum','antriebsart','anzahl türen','anzahl sitze','treibstoff','verbrauch')



def createdb():
	conn = sqlite3.connect('RICARDO.db')
	c = conn.cursor()
	c.execute('''DROP TABLE CARS''')
	c.execute('''CREATE TABLE CARS(
		Code INTEGER NOT_NULL  AUTO_INCREMENT,
		price,
		brand,
		modell,
		km,
		ps,
		leergewicht,
		getriebsart,
		hubraum,
		antriebsart,
		türen,
		sitze,
		treibstoff,
		verbrauch,
		PRIMARY KEY(Code));''')
	conn.close()

#createdb()
def insert(car):
	dictoo = dict()
	for x in ATTRS:
		try:dictoo[x] = car.findict[x]
		except: dictoo[x] = '-'
	insstring="("
	for x in dictoo.keys():
		insstring+='"{0}",'.format(dictoo[x])
	insstring = insstring[:-1]
	insstring += ')'
	conn = sqlite3.connect('RICARDO.db')
	c = conn.cursor()

	finstring = "INSERT INTO CARS(price,brand,modell,km,ps,leergewicht,getriebsart,hubraum,antriebsart,türen,sitze,treibstoff,verbrauch) VALUES {0};".format(insstring)
	c.execute(finstring)
	conn.commit()
		

