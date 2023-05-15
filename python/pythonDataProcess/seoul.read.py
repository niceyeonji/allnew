import pandas as pd

filename = 'seoul.csv'
df = pd.read_csv(filename)
print(df)

# 서울특별시 강남구 신사동인 것만 뽑기
result = df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동')]
print(result)

# '서울특별시 강남구 신사동'이면서 단지명이 '삼지'인 것만 뽑기
result = df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동') & (df['단지명'] == '삼지')]
print(result)

newdf = df.set_index(keys=['도로명'])
print(newdf)

result = df.loc[(df['도로명'] == '언주로')]
print(result)

result = newdf.loc[['동일로']]
print(result)
print(len(result))
count = len(newdf.loc['동일로'])
print('count: ', count)
