import pandas as pd

filename = 'data02.csv'
dataframe = pd.read_csv(filename, names=['학년', '국어', '영어', '수학'])

dataframe.index.name = '이름'
dataframe.loc[['강호민'], ['영어']] = 40
dataframe.loc[['박영희'], ['국어']] = 30

print(dataframe)