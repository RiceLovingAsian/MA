brands = ["lamborghini","peugeot","volvo"]

def getbrand(artname):
	nameS = artname.split(' ')
	return list(filter(lambda x: x in brands, nameS))[0]
