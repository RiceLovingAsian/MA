brands = ["lamborghini","peugeot","volvo",'']

def getbrand(artname):
	nameS = artname.lower().split(' ')
	return list(filter(lambda x: x in brands, nameS))[0]
