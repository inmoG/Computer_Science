import requests
from bs4 import BeautifulSoup
from course_card_front_bak import get_course as get_front_content
from course_card_back_bak import get_course as get_back_content
from save import save_to_file

course_cnt = len(get_front_content())
front = get_front_content()
back = get_back_content()

for item in range(course_cnt):
    front[item].update(back[item]) # front[n] join back[n]

course = front
save_to_file(course)