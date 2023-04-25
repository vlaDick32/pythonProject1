from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.oschadbank.ua/currency-rate")

if response.status_code == 200:
     soup = BeautifulSoup(response.text, features="html.parser")
     soup_list = soup.find_all("a", {"href": "https://www.oschadbank.ua/currency-rate"})
     res = soup_list[0].find('span')
     print(res.text)



