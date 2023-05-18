import pandas as pd

filename = 'BirthData.csv'
dataframe = pd.read_csv(filename, names=['이름', '직업', '생년월일', '만나이', '비고'])

dataframe.index.name = 'index'

new_df = dataframe[['이름', '생년월일']]

print(new_df)

myencoding = 'utf-8'
filename = 'BDData.csv'
new_df.to_csv(filename, encoding=myencoding, mode='w',  index=False)