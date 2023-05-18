import pandas as pd

filename = '여름기온.csv'
dataframe = pd.read_csv(filename, names=['평균기온', '평균최저기온', '평균최고기온'])

dataframe.index.name = '년월'

new_df = dataframe[['평균기온']]

print(new_df)

myencoding = 'utf-8'
filename = 'temp.csv'
new_df.to_csv(filename, encoding=myencoding, mode='w',  index=True)