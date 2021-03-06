import sqlite3,os
ATTRS = ('price','brand','modell','kilometer','ps','leergewicht','getriebeart','hubraum','antriebsart','anzahl türen','anzahl sitze','kraftstoff','verbrauch')
dirname = os.path.dirname(__file__)
DBboi = os.path.join(dirname, './RICARDO.db')

def createdb():
	conn = sqlite3.connect(DBboi)
	c = conn.cursor()
	c.execute('''DROP TABLE CARS''')
	c.execute('''CREATE TABLE CARS(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		price INT,
		brand,
		modell, 
		km INT,
		ps INT,
		leergewicht,
		getriebsart,
		hubraum,
		antriebsart,
		türen INT,
		sitze INT,
		treibstoff,
		verbrauch
		);''')
	conn.close()

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
	conn = sqlite3.connect(DBboi)
	c = conn.cursor()
	finstring = "INSERT INTO CARS(price,brand,modell,km,ps,leergewicht,getriebsart,hubraum,antriebsart,türen,sitze,treibstoff,verbrauch) VALUES {0};".format(insstring)
	c.execute(finstring)
	conn.commit()
		
def showcount():
	conn = sqlite3.connect(DBboi)
	c = conn.cursor()
	c.execute('SELECT count(*) from cars;')
	count = c.fetchall()[0][0]
	return count