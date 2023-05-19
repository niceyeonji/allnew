import pandas as pd

filename = '여름기온.csv'
dataframe = pd.read_csv(filename, names=['Average_tem', 'Average_low', 'Average_high'])

dataframe.index.name = 'monthly'

new_df = dataframe[['Average_tem']]

print(new_df)

# result = new_df.loc['2015-06']
# print(result)

myencoding = 'utf-8'
filename = 'temp.csv'
new_df.to_csv(filename, encoding=myencoding, mode='w',  index=True)