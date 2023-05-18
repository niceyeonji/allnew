import requests
from bs4 import BeautifulSoup

def crawl_zodiac_statement(url):
    response = requests.get(url)
    response.raise_for_status()  # 오류 발생 시 예외 처리

    soup = BeautifulSoup(response.text, "html.parser")

    # statement 클래스를 가진 요소 선택하고 텍스트를 추출
    statement_element = soup.find(class_="statement")
    statement_text = statement_element.text.strip()

    return statement_text

# 크롤링할 페이지 URL
keyword = input("띠를 입력하세요.")
url = f"https://zodiac-horoscope.club/ko/{keyword}"

# 사이트의 statement 클래스 부분 크롤링
statement_result = crawl_zodiac_statement(url)
print(statement_result)