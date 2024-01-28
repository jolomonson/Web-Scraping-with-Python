from bs4 import BeautifulSoup

# Read html file and print existing content
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # Use Beautiful soup to render html content 
    soup = BeautifulSoup(content, 'lxml')
    # Find specified tag element in the html content
    course_title_tags = soup.find_all('h5')

    # Looping through each course title
    for course in course_title_tags:
        print(course.text)
