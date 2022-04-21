import requests
from bs4 import BeautifulSoup

URL = f"https://www.inflearn.com/courses/it-programming?order=seq&skill=javascript"

def get_last_page(): # 페이지 추출하기

    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    result = soup.find("div", {"class":"pagination_container"})
    page = []
    result = result.find_all("a")

    for result in result[1:]:
        page.append(int(result.string))
    
    return page[-1]

def extract_course(page): # 코스 추출하기
    course = []
    for page in range(page):
        page + 1
        page = requests.get(f"{URL}&page={page}")
        
        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find_all("div", {"class": "course_card_item"})
        for result in results:
            content = extract_course_content(result)
            course.append(content)

    return course

def extract_course_content(html): # 코스 정보 가져오기
    link = html.find("a", {"class": "course_card_front"})["href"]
    title = html.find("div", {"class": "course_title"}).text
    instructor = html.find("div", {"class": "instructor"}).text
    price = html.find("div", {"class": "price"}).text
    if price == None:
        price = "무료"
    rating = html.find("div", {"class": "star_solid"})["style"]
    rating = round(float(rating.lstrip("width: ").rstrip("%")))

    return {
            "link":f"https://www.inflearn.com{link}",
            "title":title,
            "instructor":instructor,
            "price":price,
            "rating":rating
            }


def get_course():
    page = get_last_page()
    course = extract_course(page)
    return course
