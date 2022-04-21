import requests
from bs4 import BeautifulSoup
from course_card_front import get_course as get_front
from course_card_back import get_course as get_back
from save import save_to_file

course_len = len(get_front())

front = get_front()
back = get_back()

for item in range(course_len):
    front[item].update(back[item]) # front[0].update(back[0]) 

course = front

save_to_file(course)

