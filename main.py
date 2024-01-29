from bs4 import BeautifulSoup
import requests

#  Webscraping from jumia.com.ng
html_text = requests.get('https://www.jumia.com.ng/catalog/?q=sneakers+for+men').text
soup = BeautifulSoup(html_text, 'lxml')

sneakers = soup.find('article', class_='prd _fb col c-prd')
sneaker_name = sneakers.find('h3', class_='name').text

print(sneaker_name)