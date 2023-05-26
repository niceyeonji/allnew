import pandas as pd
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json
from fastapi import FastAPI

# MongoDB에 연결
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb....')

mydb = client['test']

# 첫 번째 컬렉션 조회
col1 = mydb["projecttemp"]
data1 = list(col1.find({}, {"_id":0}))

# 두 번째 컬렉션 조회
col2 = mydb["projectautumn"]
data2 = list(col2.find({}, {"_id":0}))

# 데이터프레임 생성
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 데이터프레임 출력
print("DataFrame 1:")
print(df1)

print('-' * 50)

print("DataFrame 2:")
print(df2)

@app.get('/')
async def healthCheck():
    return "OK"

@app.get("/getdata")
async def get_data(date: str):
    result = {}

    # df1에서 해당 날짜에 대한 값 조회
    df1_row = df1[df1["년월"] == date]
    if not df1_row.empty:
        result["df1"] = df1_row.iloc[0]["평균기온(℃)"]
    else:
        result["df1"] = None

    # df2에서 해당 날짜에 대한 값 조회
    df2_row = df2[df2["년월"] == date]
    if not df2_row.empty:
        result["df2"] = df2_row.iloc[0]["횟수"]
    else:
        result["df2"] = None

    return result

@app.get("/getyeardata")
def get_data(year: int):
    # df1에서 해당 연도에 해당하는 데이터들의 평균 계산
    df1_year_avg = df1[df1['년월'].str.startswith(str(year))]['평균기온(℃)'].mean()
    df1_year_avg = round(df1_year_avg, 2)  # 소수점 두 번째 자리까지 반올림

    # df2에서 해당 연도에 해당하는 데이터들의 합 계산
    df2_year_sum = df2[df2['년월'].str.startswith(str(year))]['횟수']
    df2_year_sum = pd.to_numeric(df2_year_sum, errors='coerce').sum()  # 횟수 열을 숫자로 변환하여 합 계산

    return {
        "df1_year_avg": df1_year_avg,
        "df2_year_sum": df2_year_sum
    }


# CSV 파일 경로
csv_path = "combi.csv"

# CSV 파일을 DataFrame으로 읽기
df = pd.read_csv(csv_path)

# DataFrame 출력
print(df)