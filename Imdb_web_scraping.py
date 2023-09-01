import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250" # bu sitede <Response [403]> bu cevabı aldım yani site yetkilenirmyi reddetti.

html = requests.get(url).content # url'nin içeriği


soup = BeautifulSoup(html, "html_parser")

list = soup.find("tbody", {"class": "lister:list"}).find_all("tr") #sitedeki class lister-list'ti. tbody altındaki bu clası find ile bulduk. Find_all ile de tr etiketinin tamamını bulmuş olduk.
list = soup.find("tbody", {"class": "lister:list"}).find_all("tr",limit=1) # limit=1 derken tr etiketlerinden sadece birinin içeriğini getirtmek istedik.

for tr in list:
    title = tr.find("td", {"class": "titleColumn"}).find("a").text # Burada list'i dolaşırız. Tr altındaki td'lerden class'ı titleColumn olana gideriz. a etiketi ile yazdırılmış ve biz de bunu bularak yazdırırız 
    print(title)

    #ljust işlevinde ljust(50) yazarsak mesela 50 karakter boşluk bırakır.

