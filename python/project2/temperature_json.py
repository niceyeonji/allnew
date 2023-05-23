# import pandas as pd
# import json

# csv_data = pd.read_csv("temp.csv", sep = ",")
# csv_data.to_json("temp.json", orient = "records")

from pandas import DataFrame
import pandas as pd

filename = 'temperature.csv'
dataframe = pd.read_csv(filename, header=0)

dataframe.index.name = '년월'

new_df = dataframe[['년월', '평균기온(℃)']]

print(new_df)

# result = new_df.loc['2018-06']
# print(result)

filename = 'temp_data.json'
new_df.to_json(filename, orient='records', force_ascii=False)

print(filename + '파일 저장 완료')