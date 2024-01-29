from bs4 import BeautifulSoup
import requests

#  Webscraping from jumia.com.ng
html_text = requests.get('https://www.jumia.com.ng/catalog/?q=sneakers+for+men').text
soup = BeautifulSoup(html_text, 'lxml')

sneakers = soup.find_all('article', class_='prd _fb col c-prd')
output_file = 'sneakers.txt'

with open(f'sneakers/{output_file}.txt', 'w') as f:
    for sneaker in sneakers:
        sneaker_name = sneaker.find('h3', class_='name').text.strip()
        sneaker_price = sneaker.find('div', class_='prc').text.strip()
        #sneaker_discount = sneaker.find('div', class_='bdg _dsct _sm').text
        sneaker_rating = sneaker.find('div', class_='stars _s').text.strip()
        sneaker_info = sneaker.a.get('href')
    
        f.write(f"Name: {sneaker_name}\n")
        f.write(f"Price: {sneaker_price}\n")
        f.write(f"Rating: {sneaker_rating}\n")
        f.write(f"More Info: {'https://www.jumia.com.ng/'+sneaker_info}")
        print('')

print(f"File saved!")