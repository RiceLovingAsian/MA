import os
import sqlite3


dirname = os.path.dirname(__file__)
DBboi1 = os.path.join(dirname, './Ricardo/RICARDO.db')
DBboi2 = os.path.join(dirname, './Autoscout/AUTOSCOUT.db')


def getfromdb(path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute('''SELECT * FROM CARS''')
	res =c.fetchall()
	return(res)
