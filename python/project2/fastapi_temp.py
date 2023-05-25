from pandas import DataFrame
from fastapi import FastAPI
import pandas as pd
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json
import chardet
import matplotlib.pyplot as plt
from temp_models import Temp
from database import db_conn
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

@app.get('/getmongo')
# async def getMongo():
#     return list(mycol.find())
async def getMongo():
    data = mycol.find({}, {"_id": 0, "년월": 1, "평균기온(℃)": 1})
    result = {d["년월"]: d["평균기온(℃)"] for d in data}
    return result

@app.get('/getmonthly')
async def getmonthly(monthly=None):
    if monthly is None:
        return "날짜를 입력하세요."
    result = mycol.find_one({"년월":monthly})
    if result:
        return result
    else:
        return "검색 결과가 없습니다."

@app.get('/getyear')
# 'year'라는 매개변수를 통해 입력한 연도 받기
async def getyear(year=None):
# 연도가 입력되지 않은 경우 입력하라는 메시지 반환
    if year is None:
        return "연도를 입력하세요."
# results라는 빈 리스트 생성. 입력한 연도에 해당하는 데이터 저장 용도
    results = []
# mycol.find() 메서드 사용해서 MongoDB의 컬렉션에서 모든 데이터 가져옴. 반복문 사용 monthly변수에 현재 아이템의 "년월"값 할당 
    for item in mycol.find():
        monthly = item["년월"]
# 'monthly[:len(year)]'로 monthly값을 연도의 길이만큼 슬라이싱해서 입력한 연도와 비교. 연도 일치하면 해당 아이템을 results 리스트에 추가.
        if monthly[:len(year)] == year:
            results.append(item)
# 'results'리스트가 비어있지 않다면 연도에 해당하는 데이터 반환
    if results:
        return results
# 'results'리스트가 비어있으면 검색결과 없다는 메시지 반환
    else:
        return "검색 결과가 없습니다."
        
def temp():
    url = "http://192.168.1.58:5000/temp"
    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)

def duplica(yd):
    query = {"년월":yd}
    count = mycol.count_documents(query)
    return count > 0

@app.get('/add_temp')
async def save_data_temp_mongo():
    listResult = []
    listData = fire()
    for item in listData:
        if not duplica(item["년월"]):
            listResult.append(item)

    if listResult:
        mycol.insert_many(listResult)
    return "데이터가 추가되었습니다."

@app.get('/tempmongo')
async def tempmongo():
    result=list(mycol.find())
    data={item["년월"]:item["횟수"] for item in result}
    return data

@app.get('/add_data')
async def add_data():
    with open("temp_data.json", "r") as file:
        data = json.load(file)

    for item in data:
        mycol.insert_one(item)

    return "데이터가 추가되었습니다."


@app.get("/del_data")
async def dea_data(monthly=None):
    if monthly is None:
        return "날짜를 입력하세요"
    else:
        month = mycol.find_one({"년월":monthly})
        if month:
            mycol.delete_one({"년월":monthly})
            return list(mycol.find().limit(10))
        else:
            return f"년월 = {monthly} 데이터가 존재하지 않습니다."

@app.get("/temp_graph")
def temp_graph(year1: int, year2: int):
    plt.rcParams['font.family'] = "AppleGothic"

    # JSON 파일로부터 데이터 읽어서 데이터프레임('df')으로 저장.
    filename = 'temp_data.json'
    df = pd.read_json(filename)

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

db = db_conn()
session = db.sessionmaker()

@app.get('/add_total')
async def add_total(year=None):
    if year is None:
        return "'년도(ex, 2018)'를 입력하세요."
    else:
        data = await getmongo(year)

        for date, avr in data.items():
            total = Temp(DATADATE=date, TEMP_AVR=avr)
            session.add(total)

        session.commit()

        results = session.query(Temp).all()

        return results

async def getmongo(year):
    data = mycol.find({}, {"_id": 0, "년월": 1, "평균기온(℃)": 1})
    filtered_data = {d["년월"]: d["평균기온(℃)"] for d in data if d["년월"].startswith(year)}
    return filtered_data


