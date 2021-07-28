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

    #results = soup.find_all("div", {"class": "course_card_item"})   
    #for result in results:
    #    item = result.find("div", {"class": "course_card_back"})
    #    description = item.find("p", {"course_description"})
    #    level = item.find("div", {"class" : "course_level"}).span.text
    #    skills = item.find("div", {"class" : "course_skills"}).span.text
    #print(level)



#def get_last_page():
#    request = requests.get(URL)
#    soup = BeautifulSoup(request.text, 'html.parser')
#    pagination = soup.find("div", {"class": "pagination_container"})
#    links = pagination.find_all("a")
#
#    page = []
#    for link in links[1:]:
#        page.append(int(link.string))
#
#    MAX_page = page[-1]
#
#    return MAX_page
#
#def extract_course(last_page):
#    course = []
#
#    for page in range(last_page):
#        page = page + 1
#        result = requests.get(f"{URL}&page={page}")
#        soup = BeautifulSoup(result.text, 'html.parser')
#        results = soup.find_all("div", {"class": "course_card_back"})
#
#        for result in results:
#
#            content = extract_course_content(result)
#            course.append(content)
#    
#    return course
#
#def extract_course_content(html):
#    description = html.find("p", {"class": "course_description"}).text
#    level = html.find("div", {"class": "course_level"}).span.get_text()
#    skills = html.find("div", {"class", "course_skills"}).span.get_text()
#
#    return {
#        "description" : description,
#        "level" : level,
#        "skills" : skills
#    }
#
#def get_course():
#    last_page = get_last_page()
#    course = extract_course(last_page)
#    return course