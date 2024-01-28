from bs4 import BeautifulSoup

# Read html file and print existing content
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # Use Beautiful soup to prettify html content 
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())