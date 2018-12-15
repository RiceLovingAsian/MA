import sqlite3,os
ATTRS = ('preis','brand','modell','kilometer','ps','leergewicht','getriebeart','hubraum','antriebsart','tueren','sitze','treibstoff','verbrauch in l/100 km')
dirname = os.path.dirname(__file__)
DBboi = os.path.join(dirname, './AUTOSCOUT.db')

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

def showcount():
	conn = sqlite3.connect(DBboi)
	c = conn.cursor()
	c.execute('SELECT count(*) from cars;')
	count = c.fetchall()[0][0]
	return count