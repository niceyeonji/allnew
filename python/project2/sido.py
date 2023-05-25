from pandas import DataFrame
from fastapi import FastAPI
import pandas as pd
from pymongo import MongoClient
import pydantic
from bson.objectid import ObjectId
import os.path
import json
import urllib.request


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