import csv

def save_to_file(course):
    file = open('course.csv', mode='w', encoding='utf-8', newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "course_link", "instructor", "rating", "price", "description", "level", "skills"]) # 컬럼 생성

    for course in course:
        writer.writerow(list(course.values()))

