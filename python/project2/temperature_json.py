import pandas as pd
import json

csv_data = pd.read_csv("temperature.csv", sep = ",")
data_dict = csv_data.to_dict(orient="records")
final_dict = {"temp": data_dict}

with open("temp.json", "w") as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False)


# csv_data.to_json("temp.json", orient = "index", force_ascii=False)
# from pandas import DataFrame
# import pandas as pd

# filename = 'temperature.csv'
# dataframe = pd.read_csv(filename, header=0)

# dataframe.index.name = '년월'

# new_df = dataframe[['년월', '평균기온(℃)']]

# print(new_df)

# # result = new_df.loc['2018-06']
# # print(result)

# filename = 'temp_data1.json'
# new_df.to_json(filename, orient='records', force_ascii=False)

# print(filename + '파일 저장 완료')