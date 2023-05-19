import pandas as pd
import json

csv_data = pd.read_csv("temp.csv", sep = ",")
csv_data.to_json("temp.json", orient = "records")
# json_data = json.dumps({"temp": csv_data.to_dict(orient="records")})

# with open("temp.json", "w", encoding="utf-8") as json_file:
#     json_file.write(json_data)