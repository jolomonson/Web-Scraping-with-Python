from bs4 import BeautifulSoup
import requests

#  Webscraping from jumia.com.ng
html_text = requests.get('https://www.jumia.com.ng/catalog/?q=sneakers+for+men').text
soup = BeautifulSoup(html_text, 'lxml')

sneakers = soup.find_all('article', class_='prd _fb col c-prd')
for sneaker in sneakers:
    sneaker_name = sneaker.find('h3', class_='name').text.strip()
    sneaker_price = sneaker.find('div', class_='prc').text.strip()
    #sneaker_discount = sneaker.find('div', class_='bdg _dsct _sm').text
    sneaker_rating = sneaker.find('div', class_='stars _s').text.strip()
    sneaker_info = sneaker.a.get('href')
    
    print("Name: ",sneaker_name)
    print("Price: ",sneaker_price)
    print("Rating: ",sneaker_rating)
    print("More Info: ",'https://www.jumia.com.ng/'+sneaker_info)

    print('')