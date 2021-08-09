import requests
from bs4 import BeautifulSoup
from ast import literal_eval

URL = f"https://www.inflearn.com/courses/it-programming?order=recent&skill=javascript"

def get_last_page():

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination_container"})
    links = pagination.find_all("a")

    page = []
    for link in links[1:-1]:
        page.append(link.text)

    MAX_page = int(page[-1])
    return MAX_page


def extract_course(page):
    for page in range(page):
        course = []    
        result = requests.get(f"{URL}&page={page}")    
        soup = BeautifulSoup(result.text, 'html.parser')
        items = soup.find_all("div", {"class": "course_card_item"}) 
        
        for item in items:
            content = extract_course_content(item)
            course.append(content)

    return course

def extract_course_content(html):
    
    link = html.find("a")["href"]
    title = html.find("a", {"class": "course_card_front"}).find("div", {"class": "course_title"}).string
    instructor = html.find("div", {"class": "instructor"}).string
    price = html.find("div", {"class": "price"}).string
    if price == None:
        price = "무료"
    rating = extract_rating(html)
    
    return {
    
        "link" : f"https://www.inflearn.com{link}",
    
        "title" : title,
    
        "instructor" : instructor,
    
        "price" : price,
    
        "rating" : rating
    
    }
    
    
def extract_rating(html):
    result = html.find("div", {"class": "rating"}).find("div", {"class": "star_solid"})["style"]
    rating = round(float(result.lstrip("width: ").rstrip("%")))

    return rating



def get_course():
    last_page = get_last_page()
    course = extract_course(last_page)
    return course