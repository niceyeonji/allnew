import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "AppleGothic"

# JSON 파일로부터 데이터 읽어서 데이터프레임('df')으로 저장.
filename = 'temp_data.json'
df = pd.read_json(filename)

# '년월' 열을 날짜형으로 변환
df['년월'] = pd.to_datetime(df['년월'])

# 2020년 데이터 필터링
df_2020 = df[df['년월'].dt.year == 2020]
# 2021년 데이터 필터링
df_2021 = df[df['년월'].dt.year == 2021]

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 2020년 그래프 그리기
plt.plot(df_2020['년월'].dt.month, df_2020['평균기온(℃)'], marker='o', label='2020년')
# 2021년 그래프 그리기
plt.plot(df_2021['년월'].dt.month, df_2021['평균기온(℃)'], marker='o', label='2021년')

plt.xlabel('월')
plt.ylabel('평균기온(℃)')
plt.title('2020년 vs. 2021년 월별 평균기온')
plt.legend()

# x축 눈금 설정
plt.xticks(range(1, 13), ['01월', '02월', '03월', '04월', '05월', '06월', '07월', '08월', '09월', '10월', '11월', '12월'])

filename = 'tempGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' 저장되었습니다.')
plt.show()