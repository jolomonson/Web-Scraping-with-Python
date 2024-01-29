from bs4 import BeautifulSoup
import requests

#  Webscraping from jumia.com.ng
html_text = requests.get('https://www.jumia.com.ng/catalog/?q=sneakers+for+men').text
soup = BeautifulSoup(html_text, 'lxml')

sneakers = soup.find_all('article', class_='prd _fb col c-prd')
for sneaker in sneakers:
    sneaker_name = sneaker.find('h3', class_='name').text
    sneaker_price = sneaker.find('div', class_='prc').text
    #sneaker_discount = sneaker.find('div', class_='bdg _dsct _sm').text
    sneaker_rating = sneaker.find('div', class_='stars _s').text

    print("Name: ",sneaker_name)
    print("Price: ",sneaker_price)
    print("Rating: ",sneaker_rating)

    print('')