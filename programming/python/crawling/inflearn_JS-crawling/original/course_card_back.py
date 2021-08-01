import requests
from bs4 import BeautifulSoup

URL = f"https://www.inflearn.com/courses/it-programming?order=seq&skill=javascript"

def get_last_page():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    result = soup.find("div", {"class" : "pagination_container"})
    links = result.find_all("a")

    MAX_page = int(links[-1].string)
    return MAX_page

def extract_course(last_page):
    course = []
    for page in range(last_page):
        page = page + 1
        request = requests.get(f"{URL}&page={page}")
        soup = BeautifulSoup(request.text, 'html.parser')
        results = soup.find_all("div", {"class" : "course_card_back"})
        for result in results:
            course.append(extract_course_content(result))
    return course

def extract_course_content(result):
    description = result.find("p", {"class": "course_description"}).text
    level = result.find("div", {"class": "course_level"}).span.text
    skills = result.find("div", {"class": "course_skills"}).span.text
    
    return {"description": description,
        "level" : level,
        "skills" : skills
    }

def get_course():
    last_page = get_last_page()
    course = extract_course(last_page)
    return course