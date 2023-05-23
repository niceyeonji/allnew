from pandas import DataFrame
import pandas as pd


filename = '시도별산불발생현황.csv'
df = pd.read_csv(filename, index_col=0)
print(df)

df2 = df.T
df2['연도'] = df2.index
df2 = df2.reset_index(drop=True)
print(df2)

filename = 'sidofire.json'
df2.to_json(filename, orient='records', force_ascii=False)

print(filename + '파일 저장 완료')
