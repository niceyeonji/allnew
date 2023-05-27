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

# 애플리케이션 상태 확인
@app.get('/')
def healthCheck():
    return "OK"

# node.js에 잘 연결되는지 확인 예시
@app.get("/data")
def get_data():
    data = {"message": "Hello, FastAPI!"}
    return data

# 주어진 URL에 대한 GET 요청을 보내고, 응답 결과를 반환합니다.
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        return None


# Json Server에서 데이터 가지고 오기
@app.get('/temp')        
def temp():
    url = "http://192.168.1.58:5000/temp"
    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)


# MongoDB에서 중복 데이터 여부 확인
@app.get('/duplicate')
def duplica(yd):
# 'yd'값을 가지는 문서를 찾기 위한 쿼리 생성
    query = {"년월":yd}
# 해당 쿼리에 맞는 문서의 개수를 가져옵니다.
    count = mycol.count_documents(query)
# 가져온 문서 개수('count')가 0보다 크면 중복 데이터 존재하는 것으로 간주
    return count > 0


# MongoDB에 데이터 추가
@app.get('/add_temp')
#'save_data_temp_mongo'함수는 '/add_temp'엔드포인트에서 호출
async def save_data_temp_mongo():
# 'listResult'와 'listData'라는 빈 리스트를 생성
    listResult = []
    listData = temp()
# listData를 돌면서 각 항목에 대해 중복 여부 확인
    for item in listData:
# 년월 값이 MongoDB에 존재하지 않으면
        if not duplica(item["년월"]):
# item["년월"]에서 탭 문자('\t')를 제거하고 앞뒤 공백 제거해 year_month변수에 할당.
            year_month = item["년월"].replace("\t", "").strip()
# temp_item 딕셔너리 생성해 '년월'과 '평균기온'키에 해당 값 설정
            temp_item = {
                "년월" : year_month,
                "평균기온(℃)" : item["평균기온(℃)"]
            }
# listResult에 temp_item 추가
            listResult.append(temp_item)
# listResult
    if listResult:
        mycol.insert_many(listResult)
    return "데이터가 추가되었습니다."


# mongodb에서 데이터 가지고 오기
@app.get('/tempmongo')
async def tempmongo():
# mycol.find()를 사용하여 MongoDB의 mycol 컬렉션에서 모든 문서 검색, 가져온 문서들의 리스트를 result변수에 저장
    result=list(mycol.find())
    # data={item["년월"]:item["평균기온(℃)"] for item in result}
    # return data
# result를 sorted함수를 사용해 '년월'을 기준으로 오름차순 정렬. key 매개변수에는 각 문서의 '년월'값을 반환하는 람다함수 전달
    sorted_data = sorted(result, key=lambda item: item["년월"])
# 정렬된 데이터를 기반으로 딕셔너리 'data' 생성. 각 문서의 '년월'을 키로, '평균기온'을 값으로 설정
    data = {item["년월"]: item["평균기온(℃)"] for item in sorted_data}
# 생선된 'data' 딕셔너리 반환
    return data


# 특정 연도와 월에 해당하는 데이터 가져오기
@app.get('/month_tempmongo')
# 'year' 매개변수가 'None'인지 확인.
async def month_tempmongo(year=None):
    if year is None:
        return "'년도(ex,2018)'의 입력을 확인해주세요"
    else:
# months 리스트에 원하는 월들을 문자열로 저장
        months=["06","07","08"]
# tempmongo() 함수를 호출해 MongoDB에서 데이터 가져오기. 이 함수는 /tempmongo 엔드포인트를 호출하는 비동기 함수. 가져온 건 result 변수에 저장
        result=await tempmongo()
# data 변수는 빈 딕셔너리로 초기화
# result의 각 아이템을 순회하면서 조건 확인. 년월 값을 '-'로 분리한 후 첫 번째 요소(연도)가 'year'과 일치하는지 확인 and 년월 값을 '-'로 분리한 후 두 번재 요소(월)가 'months'리스트에 포함되는지 확인 
        data = {key:value for key, value in result.items() if key.split('-')[0] == year and key.split('-')[1] in months}
# 최종적으로 'data' 딕셔너리 반환. 주어진 연도와 월에 해당하는 데이터 담고 있음.
        return data


# 특정 년도에 해당하는 월별 평균기온 데이터 가져오기
@app.get('/gettemp')
async def get_tempmongo(year=None):
    if year is None:
        return "'년도(ex,2018)의 입력을 확인해주세요"
    else:
        months = [str(i).zfill(2) for i in range(1, 13)]
        result = await tempmongo()
        data = {key: value for key, value in result.items() if key.split('-')[0] == year and key.split('-')[1] in months}
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

    # 두 데이터프레임을 합치기
    df_combined = pd.concat([df_year1, df_year2])

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

    return df_combined, {"message": "그래프가 생성되었습니다.", "filename": filename}


@app.get('/getmongo')
async def getMongo():
    baseurl = 'http://192.168.1.187:3002'
    try:
        response = requests.get(baseurl + '/getmongo')
        response.raise_for_status()  # 요청이 성공적으로 이루어졌는지 확인
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "db": "mongodb", "service": "/getmongo"}

@app.get('/firemongo')
async def firemongo():
    baseurl = 'http://192.168.1.187:3005'
    try:
        response = requests.get(baseurl + '/firemongo')
        response.raise_for_status()  # 요청이 성공적으로 이루어졌는지 확인
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "db": "mongodb", "service": "/firemongo"}

@app.get('/combined_data')
async def combined_data():
    # '/firemongo' 엔드포인트에서 데이터 가져오기
    baseurl = 'http://192.168.1.187:3005'
    try:
        response = requests.get(baseurl + '/firemongo')
        response.raise_for_status()
        fire_data = response.json()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "db": "mongodb", "service": "/firemongo", "error": str(e)}

    # '/tempmongo' 엔드포인트에서 데이터 가져오기
    try:
        response = await tempmongo()
        temp_data = response
    except Exception as e:
        return {"ok": False, "db": "mongodb", "service": "/tempmongo", "error": str(e)}

    # 가져온 데이터를 합쳐서 데이터프레임 생성
    df_fire = pd.DataFrame(fire_data.items(), columns=['년월', '화재건수'])
    df_temp = pd.DataFrame(temp_data.items(), columns=['년월', '평균기온(℃)'])
    combined_df = pd.merge(df_fire, df_temp, on='년월')

    return combined_df


# MongoDB에 가져온 데이터 데이터프레임 생성
@app.get('/mongodb_to_dataframe')
async def mongodb_to_dataframe():
    result = list(mycol.find())
    df = pd.DataFrame(result)
    return df

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)