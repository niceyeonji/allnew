import numpy as np
import pandas as pd
from pandas import Series

filename = "과일매출현황.csv"

print('# 원본 데이터프레임')
myframe = pd.read_csv(filename, index_col="과일명")
print(myframe)

print('\n# 누락데이터 채워 넣기')
# myframe.loc[['바나나'], ['구입액']] = 50.00
# myframe.loc[['사과'], ['수입량']] = 20.00
myframe.loc[myframe['구입액'].isnull(), '구입액'] = 50.00
myframe.loc[myframe['수입량'].isnull(), '수입량'] = 20.00

print(myframe)

print('\n# 구입액과 수입량의 각 소계')
print(myframe.sum(axis=0))

print('\n# 과일별 소계')
print(myframe.sum(axis=1))

print('\n# 구입액과 수입량의 평균')
print(myframe.mean(axis=0, skipna=True))

print('\n# 과일별 평균')
print(myframe.mean(axis=1, skipna=True))