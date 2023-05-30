from pandas import DataFrame
from fastapi import FastAPI
import pandas as pd
from pymongo import MongoClient
import pydantic
from bson.objectid import ObjectId
import os.path
import json
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image



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

client = MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to MongoDB....')

mydb = client['test']
mycol = mydb['projectsido']

@app.get('/')
def healthCheck():
    return "OK"

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        return None

@app.get('/sido')        
def sido():
    url = "http://192.168.1.58:5001/sido"
    result = getRequestUrl(url)
    if result is None:
        return None
    else:
        return json.loads(result)

@app.get('/duplicate')
def duplica(si):
    query = {"시도별(1)": si}
    count = mycol.count_documents(query)
    return count > 0

@app.get('/add_sido')
async def save_data_sido_mongo():
    listResult = []
    listData = sido()
    start_inserting = False  # "서울"을 포함한 딕셔너리부터 데이터를 넣기 위한 플래그

    for item in listData:
        if item["시도별(1)"] == "서울":
            start_inserting = True

        if start_inserting and not duplica(item["시도별(1)"]):
            listResult.append(item)

    if listResult:
        mycol.insert_many(listResult)
    return "데이터가 추가되었습니다."

@app.get('/sidomongo')
async def sidomongo():
    cursor = mycol.find({}, {"_id": 0})
    result = [doc for doc in cursor]
    return result

@app.get('/yearly_data')
async def get_yearly_data():
    result = await sidomongo()
    yearly_data = {}
    for item in result:
        for key, value in item.items():
            if key != '시도별(1)':
                if key in yearly_data:
                    yearly_data[key][item['시도별(1)']] = value
                else:
                    yearly_data[key] = {item['시도별(1)']: value}
    return yearly_data

@app.get('/yearly_data/{year}')
async def get_yearly_data(year: str):
    result = await sidomongo()
    yearly_data = {}

    for item in result:
        for key, value in item.items():
            if key != '시도별(1)':
                if key == year:
                    yearly_data[item['시도별(1)']] = value

    return yearly_data

# 연도 입력하면 그 해 가장 큰 규모의 산불 피해를 입은 지역이 나옴
@app.get('/max_value/{year}')
async def get_max_value(year: str):
    result = await sidomongo()
    max_value = float('-inf')
    max_data = {}

    for item in result:
        for key, value in item.items():
            if key != '시도별(1)' and key == year:
                if value != '-' and float(value) > max_value:
                    max_value = float(value)
                    max_data['시도'] = item['시도별(1)']
                    max_data['값'] = value

    return max_data


@app.get('/pie_charts/{year1}/{year2}')
async def generate_pie_charts(year1: str, year2: str):
    plt.rcParams['font.family'] = "AppleGothic"
    result = await sidomongo()
    data1 = {}
    data2 = {}

    for item in result:
        for key, value in item.items():
            if key != '시도별(1)':
                if key == year1:
                    if value != '-':
                        data1[item['시도별(1)']] = float(value)
                elif key == year2:
                    if value != '-':
                        data2[item['시도별(1)']] = float(value)

    # 데이터 처리
    threshold = 0.01  # 1% 미만의 임계값 설정
    data1_combined = {}
    data2_combined = {}

    # year1 데이터 처리
    total1 = sum(data1.values())
    other1 = 0

    for label, value in data1.items():
        if value / total1 >= threshold:
            data1_combined[label] = value
        else:
            other1 += value

    data1_combined['기타'] = other1

    # year2 데이터 처리
    total2 = sum(data2.values())
    other2 = 0

    for label, value in data2.items():
        if value / total2 >= threshold:
            data2_combined[label] = value
        else:
            other2 += value

    data2_combined['기타'] = other2

    # 그래프 생성
    plt.figure(figsize=(10, 6))
    colors = ['#ff9999','#ffc000', '#8fd9b6', '#d395d0', 'yellowgreen', 'lightblue','sandybrown', 'lightskyblue', 'lightcoral', 'paleturquoise', 'thistle']


    # year1 파이 차트
    plt.subplot(1, 2, 1)
    plt.pie(data1_combined.values(), labels=data1_combined.keys(), autopct='%1.1f%%', startangle=90, counterclock=False, colors=colors)
    plt.title(f"시도별 산불 발생 현황 - {year1}")

    # year2 파이 차트
    plt.subplot(1, 2, 2)
    plt.pie(data2_combined.values(), labels=data2_combined.keys(), autopct='%1.1f%%', startangle=90, counterclock=False, colors=colors)
    plt.title(f"시도별 산불 발생 현황 - {year2}")

    plt.tight_layout()  # 그래프 간격 조정

    # Save the pie chart image
    chart_filename = f"firepie_{year1}_{year2}.png"
    filepath = '/allnew/python/project2/html/public/media/' + chart_filename
    plt.savefig(filepath)
    plt.close()
    return {"message": "그래프가 생성되었습니다.", "filename": chart_filename}

@app.get('/sido_frame/{year1}/{year2}')
async def sido_frame(year1: int, year2: int):

    query = {"년월": {"$regex": f"^{year1}|^{year2}"}}
    result = list(mycol.find(query))

    df = pd.DataFrame(result)

    df["Year"] = pd.to_datetime(df["년월"]).dt.year
    df["Month"] = pd.to_datetime(df["년월"]).dt.month

    df_pivot = df.pivot(index="Year", columns="Month", values="평균기온(℃)")

    df_pivot = df_pivot.reindex(columns=sorted(df_pivot.columns, key=lambda x: int(x)))

    return df_pivot

