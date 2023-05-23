import pandas as pd
import json

csv_data = pd.read_csv("시도별산불발생현황.csv", sep = ",")
csv_data.to_json("sidofire.json", orient = "records", force_ascii=False)