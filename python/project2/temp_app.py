from pandas import DataFrame
from fastapi import FastAPI
import pandas as pd
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json, urllib.request
import chardet
import matplotlib.pyplot as plt
import requests


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
mycol = mydb['projecttemp']

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

@app.get('/temp')        
def temp():
    url = "http://192.168.1.58:5000/temp"
    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)

@app.get('/duplicate')
def duplica(yd):
    query = {"년월":yd}
    count = mycol.count_documents(query)
    return count > 0

@app.get('/add_temp')
async def save_data_temp_mongo():
    listResult = []
    listData = temp()
    for item in listData:
        if not duplica(item["년월"]):
            year_month = item["년월"].replace("\t", "").strip()
            temp_item = {
                "년월" : year_month,
                "평균기온(℃)" : item["평균기온(℃)"]
            }
            listResult.append(temp_item)

    if listResult:
        mycol.insert_many(listResult)
    return "데이터가 추가되었습니다."


# mongodb에서 데이터 가지고 오기
@app.get('/tempmongo')
async def tempmongo():
    result=list(mycol.find())
    # data={item["년월"]:item["평균기온(℃)"] for item in result}
    # return data
    sorted_data = sorted(result, key=lambda item: item["년월"])
    data = {item["년월"]: item["평균기온(℃)"] for item in sorted_data}
    return data

@app.get('/month_tempmongo')
async def month_tempmongo(year=None):
    if year is None:
        return "'년도(ex,2018)의 입력을 확인해주세요"
    else:
        months=["06","07","08"]
        result=await tempmongo()
        data = {key:value for key, value in result.items() if key.split('-')[0] == year and key.split('-')[1] in months}
        return data


# 월별 평균기온 비교 그래프 그리기
@app.get("/temp_graph")
async def temp_graph(year1: int, year2: int):
    plt.rcParams['font.family'] = "AppleGothic"

    result = list(mycol.find())

    df = pd.DataFrame(result, columns=['년월', '평균기온(℃)'])

    # '년월' 열을 날짜형으로 변환
    df['년월'] = pd.to_datetime(df['년월'])

    # 입력한 연도 데이터 필터링
    df_year1 = df[df['년월'].dt.year == year1]
    df_year2 = df[df['년월'].dt.year == year2]

    # 그래프 그리기
    plt.figure(figsize=(10, 6))

    # 입력한 연도 그래프 그리기
    plt.plot(df_year1['년월'].dt.month, df_year1['평균기온(℃)'], marker='o', label=str(year1)+'년')
    plt.plot(df_year2['년월'].dt.month, df_year2['평균기온(℃)'], marker='o', label=str(year2)+'년')

    plt.xlabel('월')
    plt.ylabel('평균기온(℃)')
    plt.title(str(year1)+'년 vs. '+str(year2)+'년 월별 평균기온')
    plt.legend()

    # x축 눈금 설정
    plt.xticks(range(1, 13), ['01월', '02월', '03월', '04월', '05월', '06월', '07월', '08월', '09월', '10월', '11월', '12월'])

    filename = 'tempGraph_'+str(year1)+'_'+str(year2)+'.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    plt.close()

    return {"message": "그래프가 생성되었습니다.", "filename": filename}