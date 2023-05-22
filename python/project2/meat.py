import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.kmta.or.kr/kr/data/stats_spend.php"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# <table> 요소 선택
table1 = soup.select_one("table")

# 추출한 데이터를 저장할 리스트 생성
data = []

# <table> 내부의 행(tr)을 돌면서 데이터 추출
for row in table1.select("tr"):
    th = row.find("th", scope="row")
    if th:
        row_data = [th.get_text(strip=True)] + [value.get_text(strip=True) for value in row.select("td")]
        data.append(row_data)

# 추출한 데이터로 데이터프레임 만들기
df = pd.DataFrame(data[1:], columns=['year', 'beaf', 'pork', 'chicken', 'total', 'beaf1', 'pork1', 'chicken1', 'total1'])
# df.set_index('year', inplace=True)

# 만든 데이터프레임 확인!
print(df)

# csv로 저장하기
# filename = 'meat.csv'
filename = 'meat.json'
myencoding = 'utf-8'
# df.to_csv(filename, encoding=myencoding, mode='w', index=True)
df.to_json(filename, mode='w', index=True, orient = "records")
print(filename + '파일 저장 완료')

