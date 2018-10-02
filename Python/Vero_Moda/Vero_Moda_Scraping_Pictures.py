from bs4 import BeautifulSoup as  soup 
import urllib.request
from urllib.request import urlopen as uReq

my_url = "https://www.veromoda.com/ch/de/vm/kategorie-waehlen/kleider/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


# images = page_soup.findAll("img" , {"srcset src":""})
for images in page_soup.findAll("img" , {"srcset src":""}):
	if images.has_attr("href"):
		print (images.attrs["href"])

# for image in images:

# 	a = image.get("data-src")
	



# 	def download_jpg(url, file_path):
# 		path = file_path  + ".jpg"
# 		urllib.request.urlretrieve(url, path)

# 	ulr = a

# 	download_jpg(url, "Vero_Moda_Pictures



THIS DOES NOT WORK !