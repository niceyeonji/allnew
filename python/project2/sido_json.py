import pandas as pd
import json

csv_data = pd.read_csv("시도별산불발생현황.csv", sep = ",")
data_dict = csv_data.to_dict(orient="records")
final_dict = {"sido": data_dict}

with open("sido.json", "w") as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False)