from fastapi import FastAPI
import pandas as pd
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json
import chardet

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
mycol = mydb['projectautumn']

@app.get('/')
def healthCheck():
    return "OK"

@app.get('/getmongo')
async def getMongo():
    return list(mycol.find())

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

@app.get('/add_data')
async def add_data():
    with open("fire.json", "r") as file:
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