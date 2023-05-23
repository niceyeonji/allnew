import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = "AppleGothic"

# JSON 파일로부터 데이터 읽기
filename = 'fire.json'
df = pd.read_json(filename)

# '년월' 열을 날짜형으로 변환
df['년월'] = pd.to_datetime(df['년월'])

# 2020년 데이터 필터링
df_2020 = df[df['년월'].dt.year == 2020]

# 2021년 데이터 필터링
df_2021 = df[df['년월'].dt.year == 2021]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(df_2020['년월'], df_2020['횟수'], label='2020년')
plt.bar(df_2021['년월'], df_2021['횟수'], label='2021년')
plt.xlabel('월')
plt.ylabel('발생건수')
plt.title('2020년 vs. 2021년 발생건수')
plt.legend()
plt.xticks(rotation=45)

filename = 'fireGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' 저장 되었습니다.')
plt.show()