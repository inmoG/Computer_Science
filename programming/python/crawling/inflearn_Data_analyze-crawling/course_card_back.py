from time import process_time
import requests
from bs4 import BeautifulSoup

URL = f"https://www.inflearn.com/courses/data-science/data-analysis"


def get_last_page(): # 페이지 가져오기
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    result = soup.find("div", {"class": "pagination_container"})

    result = result.find_all("a")

    page = []

    for result in result[1:]:
        page.append(int(result.string))
    
    return page[-1]



def extract_course(page):
    course = []

    for page in range(page):
        page + 1
        page = requests.get(f"{URL}?order=seq&page={page}")
    
        soup = BeautifulSoup(page.text, 'html.parser')
        items = soup.find_all("div", {"class": "course_card_item"})

        for item in items:
            content = extract_course_content(item)
            course.append(content)        

    return course

def extract_course_content(html):
    description = html.find("p", {"class":"course_description"}).text
    level = html.find("div", {"class": "course_level"}).text
    skills = html.find("div", {"class": "course_skills"}).text
    
    return {"description": description,
            "level" : level,
            "skills" : skills
            }




def get_course():
    page = get_last_page()
    course = extract_course(page)
    return course

