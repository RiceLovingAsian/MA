import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as ureq


my_url = "https://www.autolina.ch/carList?make=10&model=6&sort=makemodel_asc"
uClient = ureq(my_url)
my_html = uClient.read()
uClient.close()
page_soup = soup(my_html, "lxml")

href = [
"https://www.autolina.ch/ac/carList?make=372&sort=makemodel_asc&page=1" ,
"https://www.autolina.ch/alfa-romeo--145/carList?make=10&model=6&sort=makemodel_asc",
"https://www.autolina.ch/alfa-romeo--147/carList?make=10&model=8&sort=makemodel_asc",
"https://www.autolina.ch/alfa-romeo--155/carList?make=10&model=9&sort=makemodel_asc",
"https://www.autolina.ch/alfa-romeo--156/carList?make=10&model=10&sort=makemodel_asc",




]

