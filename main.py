from bs4 import BeautifulSoup

# Read html file and print existing content
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # Use Beautiful soup to render html content 
    soup = BeautifulSoup(content, 'lxml')
    # Find element by div tag and class attribute
    course_cards = soup.find_all('div', class_='card')

    # Looping through each course card for course details
    for course in course_cards:
        course_name = course.h5.text
        course_description = course.p.text
        course_price = course.a.text.split()[-1]

        print(course_name,'-',course_description,'It costs',course_price)
