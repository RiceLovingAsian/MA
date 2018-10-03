import sqlite3



def createdb():
	conn = sqlite3.connect('RICARDO.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE CARS(code INTEGER PRIMARY KEY AUTOINCREMENT,price,brand,modell,km,ps,leergewicht,getriebsart,hubraum,antriebsart,türen,sitze,treibstoff,verbrauch)''')
	conn.close()

#createdb()

