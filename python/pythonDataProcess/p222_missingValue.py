import numpy as np
import pandas as pd
from pandas import Series

filename = "excel02.csv"

print('\n 누락된 데이터 샘플 데이터프레임')
myframe = pd.read_csv(filename, index_col="이름")
print(myframe)

print('\n fillna() 메소드 이용')
print(myframe.fillna(0, inplace=False))

print('\n# inplace=False 이므로 원본 변동은 없음.')
print(myframe)

print('\n# inplace=True 이므로 원본 변동이 생김.')
myframe.fillna(0, inplace=True)
print(myframe)

print('\n 누락된 데이터 샘플 데이터프레임')
myframe.loc[['강감찬', '홍길동'], ['국어', '영어']] = np.nan
myframe.loc[['박영희', '김철수'], ['수학']] = np.nan
print(myframe)

print('\n# 임의의 값을 다른 값으로 치환')
print('\n# 국어 컬럼의 NaN 값들을 15로 변경')
mydict = {'국어' : 15, '영어' : 25, '수학' : 35}
myframe.fillna(mydict, inplace=True)

print(myframe)
print('-' * 40)

myframe.loc[['박영희'], ['국어']] = np.nan
myframe.loc[['홍길동'], ['영어']] = np.nan
myframe.loc[['김철수'], ['수학']] = np.nan

print(myframe)
print('-' * 40)

mydict = {'국어' : myframe['국어'].mean(),
          '영어' : myframe['영어'].mean(),
          '수학' : myframe['수학'].mean()}

myframe.fillna(mydict, inplace=True)

print(myframe)
print('-' * 40)
