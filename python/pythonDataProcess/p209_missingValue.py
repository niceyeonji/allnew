import numpy as np
import pandas as pd
from pandas import DataFrame, Series

print('\n# 시리즈의 누락 데이터 처리')
print('# 원본 시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)

print('\n# isnull() 함수 : NaN이면 True')
print(myseries.isnull())

print('\n# notnull() 함수 : NaN이 아니면 True')
print(myseries.notnull())
print("-" * 40)

print('\n# notnull() 이용 참인 항목만 출력')
print(myseries[myseries.notnull()])

print('\n# dropna() 이용 누락 데이터 처리')
print(myseries.dropna())

filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)

print('\n# dropna() 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0)
print(cleaned)

print('\n# how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)

print('\n#how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='any')
print(cleaned)

print('\n# [영어] 칼럼에 NaN 제거')
print(myframe.dropna(subset=['영어']))

print('\n# 컬럼 기준, how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='all')
print(cleaned)

print('\n# 컬럼 기준, how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=1, how='any')
print(cleaned)

print('\n## before')
print(myframe)
myframe.loc[['강감찬', '홍길동'], ['국어']] = np.nan
print('## after')
print(myframe)

print(myframe.dropna(axis=1, how='all'))
print(myframe)

# df.dropna(axis=0 or 1, thresh=n) : 축을 기준으로 n개 미만 입력되면 그 축 삭제. not null count
print('## thresh option')
print(myframe.dropna(axis=1, thresh=2))