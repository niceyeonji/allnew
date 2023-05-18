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

# <table> 내부의 행(tr)을 순회하며 데이터 추출
for row in table1.select("tr"):
    th = row.find("th", scope="row")
    if th:
        row_data = [th.get_text(strip=True)] + [value.get_text(strip=True) for value in row.select("td")]
        data.append(row_data)

# Create DataFrame from the data
df = pd.DataFrame(data[1:], columns=['년도', '전체소비우육', '전체소비돈육', '전체소비계육', '전체소비계', '1인우육', '1인돈육', '1인계육', '1인계'])
df.set_index('년도', inplace=True)

# Print the DataFrame
print(df)