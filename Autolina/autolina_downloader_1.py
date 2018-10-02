import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


my_url = "https://www.autolina.ch/auto/aston-martin-db11/1226273"
my_client = ureq(my_url)
my_html = my_client.read()
my_client.close()
page_soup = soup(my_html, "lxml")


def function(type):
	y = ""
	for x in type:
		y += str(x)
	y+=";"
	return(y)


for x in page_soup.select("table > tr > td"):
	for btag in x.select("b"):
		


		y = str(btag)
		print(y)

		self.y = function(y)

		self.ystr = self.correct(self.y)

	def correct(self,string):
		self.string = ""
		self.list = list(string)
		self.listm = list(string)
		self.poptol = 0
		for x in range(0,len(self.list)-1):
			if x-1<0:
				x1 = 0
			else:
				x1 = x-1
			if x+1 >=len(self.list):
				x2 = len(self.list)-1
			else:
				x2 = x+1
			if self.list[x] not in self.letterlist and (self.list[x1] not in self.letterlist or self.list[x2] not in self.letterlist) or self.list[x]=="\n":
				self.listm.pop(x-self.poptol)
				self.poptol += 1

		for x in self.listm:
			self.string = str(self.string+x)
		return(self.string)

		































# import urllib.request
# import urllib.parse
# import re

# url = "https://www.autolina.ch/auto/aston-martin-db11/1226273"
# values = {"s" : "basics", "submit" : "search"}

# data = urllib.parse.urlencode(values)
# data = data.encode("utf-8")
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# whatineed = re.findall(r'<b>(.*?)</b>', str(respData))
# for b in whatineed:
# 	print(b)