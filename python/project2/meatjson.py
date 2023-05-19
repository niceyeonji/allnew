import pandas as pd
import json

csv_data = pd.read_csv("meat.csv", sep = ",")
csv_data.to_json("meat.json", orient = "records")
# json_data = json.dumps({"meat": csv_data.to_dict(orient="records")})

# with open("meat.json", "w", encoding="utf-8") as json_file:
#     json_file.write(json_data)