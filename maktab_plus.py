import requests
from bs4 import BeautifulSoup
import re
link = requests.get("https://maktabkhooneh.org/plus")
text = link.text
page = BeautifulSoup(text, "html.parser")
course_name = page.find_all("div" , attrs={"class" : "course-card__title"})
organizer_name  = page.find_all("div", attrs={"class" : "course-card__uni-title"})

course = list()
organizer = list()
for course_items in course_name:
    course.append(course_items.text)
for organizer_items in organizer_name:
    organizer.append(organizer_items.text)
for l in range(0, len(course)):
    print(course[l], organizer[l])