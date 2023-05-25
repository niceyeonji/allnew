# import pandas as pd
# import json

# csv_data = pd.read_csv("temp.csv", sep = ",")
# data_dict = csv_data.to_dict(orient="records")
# final_dict = {"temp": data_dict}

# with open("temp_data.json", "w") as json_file:
#     json.dump(final_dict, json_file, ensure_ascii=False)

import pandas as pd
import json

csv_data = pd.read_csv("temp.csv", sep=",", skiprows=7, skipfooter=1, engine='python')
data_dict = csv_data.to_dict(orient="records")
final_dict = {"temp": data_dict}

with open("temp_data.json", "w", encoding="utf-8") as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False)

# import pandas as pd
# import json

# csv_data = pd.read_csv("temp.csv", sep=",", skiprows=7)
# data_dict = csv_data.to_dict(orient="records")
# final_dict = {"temp": data_dict}

# with open("temp_data.json", "w", encoding="utf-8") as json_file:
#     json.dump(final_dict, json_file, ensure_ascii=False)