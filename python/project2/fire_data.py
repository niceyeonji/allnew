import pandas as pd
from pandas import DataFrame
import json

# csv_data = pd.read_csv("월별발생건수.csv", sep = ",")
# data_dict = csv_data.to_dict(orient="records")
# final_dict = {"data": data_dict}

# with open("fire_count.json", "w") as json_file:
#     json.dump(final_dict, json_file, ensure_ascii=False)

# CSV 파일로부터 데이터 읽기
filename = '월별발생건수.csv'
df = pd.read_csv(filename)

# 데이터 프레임 재구성
# '월별' 열을 인덱스로 설정
df = df.set_index('월별')
# stack() 함수를 사용해 데이터를 재배열. '월별' 열의 값들이 행 방향으로 쌓임
df = df.stack().reset_index()
# 열 이름을 '월별', '년도', '횟수'로 변경
df.columns = ['월별', '년도', '횟수']
#'년도'열을 정수형으로 변환 
df['년도'] = df['년도'].astype(int)
# '월별' 열의 값에서 맨 뒤의 '월'문자를 제거하고, 정수형으로 변환
df['월별'] = df['월별'].str[:-1]
df['월별'] = df['월별'].astype(int)
# '년도'와 '월별' 열을 기준으로 오름차순으로 정렬
df = df.sort_values(['년도', '월별'], ascending=[True, True])
# '월별' 열의 값을 2자리 숫자로 변경(zfill()함수 사용), 문자열로 반환.
df['월별'] = df['월별'].astype(str).str.zfill(2)
# '년도'와 '월별' 열을 결합해 '년월' 열을 생성
df['년월'] = df['년도'].astype(str) + '-' + df['월별']
# 필요한 열만 선택하여 데이터 프레임 재구성
df = df[['년월', '횟수']]

print(df.to_string(index=False))

filename = 'fire.json'
df.to_json(filename, orient='records', force_ascii=False)

print(filename + '파일 저장 완료')