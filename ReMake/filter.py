brands = ["aixam","Alfa Romeo","Datsun","American Motors","Aston Martin","Audi","Austin","Bentley","Bertone","Bmw","Bmw-Alpina","Bugatti","Buick","Cadillac","Caterham","Chevrolet","Chrysler","Citroen","citroën","Dacia","Daewoo","Daihatsu","Daimler","De Tomaso","Dodge","Donkervoort","Ferrari","Fiat","Ford","Ford(USA)","Honda","Hs","Hummer","Hyundai","Innocenti","Isuzu","Isuzu(j)","Jaguar","Jeep","Kia","Lada","Lamborghini","Lancia","Land Rover","Land-Rover","Lexus","Ligier","Lotus","Maserati","Mazda","Mercedes-Benz","mercedes","Mg","Minelli","Mini","Mitsubishi","Morgan","Nissan","Oldsmobile","Opel","Peugeot","Pontiac","Porsche","Puch","Qvale","Reliant","Renault","Rolls-Royce","Rover","Saab","Seat","Skoda","Smart","Ssang Yong","Ssangyong","Ssang-yong","Subaru","Suzuki","Talbot","Tata","Toyota","Tvr","Venturi","Volvo","Vw","Volkswagen","Wiesmann","Infiniti","Iveco","Piaggo","Ktm","Sokon","Think","Tesla","Artega","McLaren","Mega","Giotti Victoria","Fisker","Dfsk","Ds Automobiles"]
brands2 = []
badguydict = {
	"land-rover":'land rover',
	"landrover":"land rover",
	"Ssangyong":"ssang yong",
	"Ssang-yong":"ssang yong",
	"volkswagen":"vw"}
for x in brands:
	x = x.lower().split(' ')
	if len(x)!=1:
		for y in x:
			brands2.append(y)
	else:
		brands2.append(x[0])
def getbrand(artname):
	nameS = artname.lower()
	nameS = nameS.split(' ')
	dalist = list(filter(lambda x: x in brands2, nameS))
	if len(dalist)>1:
		if dalist[0].title() in brands:
			retstr = dalist[0]
		else:
		 	retstr = ""
		 	for x in dalist:
		 		retstr += str(x)+' '
	elif len(dalist)==1:
	 	retstr = dalist[0]
	if retstr in badguydict.keys():
		retstr = badguydict[retstr]
	return retstr


def getmodel(car,artname):
	retstr = ''
	artname = artname.lower()
	for x in car.brand.lower().split(' '):
		artname = artname.replace(str(x),'')
	artname = artname.replace("'","")
	artname = artname.replace('"','')
	return artname	
	return retstr
