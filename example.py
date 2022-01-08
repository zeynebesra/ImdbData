import requests

from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=%C4%B0stanbul" # Site linkimiz

response =  requests.get(url) # Web sayfamızı çekiyoruz.

#print(response)

html_icerigi = response.content # Web sayfamızın içeriğini alıyoruz.

soup = BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

#print(soup.prettify())  # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.

#print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.

# Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
