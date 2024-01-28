from bs4 import BeautifulSoup
import requests

#  Webscraping from jumia.com.ng
html_text = requests.get('https://www.jumia.com.ng/catalog/?q=sneakers+for+men').text
soup = BeautifulSoup(html_text, 'lxml')

print(soup.prettify())