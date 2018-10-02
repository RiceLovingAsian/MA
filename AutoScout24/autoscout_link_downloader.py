import bs4 as bs 
import re
import csv
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup




# #for x in range(1,3):
	
# 	#y = str("https://www.autoscout24.ch/de/autos/alle-marken?page="+str(x)+"&sort=makemodel_asc&st=1&vehtyp=10")
	
	

# #for z in range(1,5):
# 	#print(z)

# 	#my_ulr = str("https://www.autoscout24.ch/de/autos/alle-marken?page="+str(x)+"&sort=makemodel_asc&st=1&vehtyp=10")







#wie ich es normalerweise machen würde
#################################################################################################



# my_ulr = "https://www.autolina.ch/auto/jaguar-e-pace/1898607"


# uClient = ureq(my_ulr)

# myData = uClient.read()

# uClient.close

# page_soup = soup(myData, "html.parser")

# make = page_soup.find("div", {"class" : "tables carDtls-properties"}).findAll("b")

# make = str(make)

# makem = make.text

# print(makem)

#make = make[make.find("<b>")+3:make.find("</b>")]
#versucht alles andere als brackets zu bekommen


##################################################################################################











#nächste variante
##############################################################################################	
# import urllib.request
# import urllib.parse 
# import re

# url = "https://www.autolina.ch/auto/jaguar-e-pace/1898607"
# values = {"class" : "tables carDtls-properties"}
# data = urllib.parse.urlencode(values)
# data = data.encode("utf-8")
# req = urllib.request.Request(url , data)
# response = urllib.request.urlopen(req)
# responseData = response.read()


# tables = re.findall(r"<ul>(.*?)</ul>", str(responseData))

# for eachT in tables:
# 	print(eachT)
##############################################################################################







my_page = "https://www.autolina.ch/auto/jaguar-e-pace/1898607"

page = ureq(my_page)

mysoup = soup(page , "html.parser")

box = mysoup.find("div", attrs={"class":"tables carDtls-properties"}) 

name = box.text.strip()

name = name.replace("/","")
name = name.replace("{","")
name = name.replace("}","")
name = name.replace("=","")


# def replace_all(text,dic):
# 	for i, j in dic.iteritems():
# 		text = text.replace(i,j)
# 	return text
# my_text = name
# reps = { "/":"" , "{":"" , "}":"" , "=":""}
# txt = replace_all(my_text, reps)
# print(txt)

name = name.split()

print(name)


#with open("index.csv" , "a") as csv_file:
#	writer = csv.writer(csv_file)
#	writer.writerow([name])



