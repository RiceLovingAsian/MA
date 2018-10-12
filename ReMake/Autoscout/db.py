import sqlite3
ATTRS = ('preis','brand','modell','kilometer','ps','leergewicht','getriebeart','hubraum','antriebsart','anzahl türen','anzahl sitze','kraftstoff','verbrauch')



def createdb():
	conn = sqlite3.connect('AUTOSCOUT.db')
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

#createdb()
def insert(car):
	finstring='('
	for x in ATTRS:
		try:finstring+='"{}",'.format(car.findict[x.encode()])
		except:finstring +='"{}",'.format(x)
	finstring = finstring[:-1]
	finstring += ')'
	print(finstring.encode())
	dictoo = dict()
	for x in ATTRS:
		try:dictoo[x] = car.findict[x]
		except: dictoo[x] = '-'
	insstring="("
	for x in dictoo.keys():
		insstring+='"{0}",'.format(dictoo[x])
	insstring = insstring[:-1]
	insstring += ')'
	conn = sqlite3.connect('AUTOSCOUT.db')
	c = conn.cursor()
	finstring = "INSERT INTO CARS(price,brand,modell,km,ps,leergewicht,getriebsart,hubraum,antriebsart,türen,sitze,treibstoff,verbrauch) VALUES {0};".format(finstring)
	c.execute(finstring)
	conn.commit()
		

def showcount():
	conn = sqlite3.connect('AUTOSCOUT.db')
	c = conn.cursor()
	c.execute('SELECT count(*) from cars;')
	count = c.fetchall()[0][0]
	return count