import pandas as pd
import json

# Read sido.csv and convert to JSON
sido_csv_data = pd.read_csv("시도별산불발생현황.csv", sep=",")
sido_data_dict = sido_csv_data.to_dict(orient="records")

# Read temp.csv and convert to JSON
temp_csv_data = pd.read_csv("temp.csv", sep=",", skiprows=7, skipfooter=1, engine='python')
temp_data_dict = temp_csv_data.to_dict(orient="records")

# Combine sido_data_dict and temp_data_dict into season_dict
season_dict = {"sido": sido_data_dict, "temp": temp_data_dict}

# Save season.json
with open("season.json", "w", encoding="utf-8") as json_file:
    json.dump(season_dict, json_file, ensure_ascii=False)