from bs4 import BeautifulSoup

# Read html file and print existing content
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # Use Beautiful soup to render html content 
    soup = BeautifulSoup(content, 'lxml')
    # Find specific tag element in the html content
    tags = soup.find_all('h5')

    print(tags)