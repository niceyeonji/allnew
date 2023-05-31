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
from typing import List


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


# 비교 결과 나오게 하기
@app.get('/month_tempmongo')
# 'year' 매개변수가 'None'인지 확인.
async def month_tempmongo(year1=None, year2=None):
    if year1 is None or year2 is None:
        return "연도(ex. 2018)를 입력해주세요."

    months = ["06", "07", "08"]

    async def get_month_data(year):
        result = await tempmongo()
        data = {key: value for key, value in result.items() if key.split('-')[0] == year and key.split('-')[1] in months}
        return data

    data1 = await get_month_data(year1)
    data2 = await get_month_data(year2)

    output = ""

    if data1:
        max_temp1 = max(data1.values())
        avg_temp1 = sum(data1.values()) / len(data1)
        max_month1 = [k for k, v in data1.items() if v == max_temp1][0].split('-')[1]
        output += f"{year1}년의 여름(6월~8월) 중 '가장 기온이 높은 달'은 '{max_temp1}℃'인 {max_month1}월입니다. {year1}년 여름(6월~8월)의 '평균 온도'는 '{avg_temp1:.1f}℃'입니다.\n"

    if data2:
        max_temp2 = max(data2.values())
        avg_temp2 = sum(data2.values()) / len(data2)
        max_month2 = [k for k, v in data2.items() if v == max_temp2][0].split('-')[1]
        output += f"{year2}년의 여름(6월~8월) 중 '가장 기온이 높은 달'은 '{max_temp2}℃'인 {max_month2}월입니다. {year2}년 여름(6월~8월)의 '평균 온도'는 '{avg_temp2:.1f}℃'입니다.\n"

    if avg_temp1 > avg_temp2:
        output += f"{year1}년의 여름이 {year2}년의 여름보다 더 기온이 높았습니다."

    if avg_temp1 < avg_temp2:
        output += f"{year2}년의 여름이 {year1}년의 여름보다 더 기온이 높았습니다."

    return output


# # 특정 년도에 해당하는 월별 평균기온 데이터 가져오기
# @app.get('/gettemp')
# async def get_tempmongo(year=None):
#     if year is None:
#         return "'년도(ex,2018)의 입력을 확인해주세요"
#     else:
#         months = [str(i).zfill(2) for i in range(1, 13)]
#         result = await tempmongo()
#         data = {key: value for key, value in result.items() if key.split('-')[0] == year and key.split('-')[1] in months}
#         return data


# 월별 평균기온 비교 그래프 그리기
@app.get("/temp_graph")
async def temp_graph(year1: int, year2: int):
    plt.rcParams['font.family'] = "AppleGothic"

    result = list(mycol.find())

    df = pd.DataFrame(result, columns=['년월', '평균기온(℃)'])

    # '년월' 열을 날짜형으로 변환
    df['년월'] = pd.to_datetime(df['년월'], format='%Y-%m')

    # 입력한 연도 데이터 필터링
    df_year1 = df[df['년월'].dt.year == year1]
    df_year2 = df[df['년월'].dt.year == year2]

    # 그래프 그리기
    plt.figure(figsize=(10, 6))

    # 입력한 연도 그래프 그리기
    df_year1_sorted = df_year1.sort_values(by='년월')  # 월별 정렬
    df_year2_sorted = df_year2.sort_values(by='년월')  # 월별 정렬

    plt.plot(df_year1_sorted['년월'].dt.month, df_year1_sorted['평균기온(℃)'], marker='o', label=str(year1)+'년')
    plt.plot(df_year2_sorted['년월'].dt.month, df_year2_sorted['평균기온(℃)'], marker='o', label=str(year2)+'년')

    plt.plot(df_year1_sorted['년월'].dt.month[5:8], df_year1_sorted['평균기온(℃)'][5:8], color='red', marker='D', linewidth = "3")
    plt.plot(df_year2_sorted['년월'].dt.month[5:8], df_year2_sorted['평균기온(℃)'][5:8], color='red', marker='D', linewidth = "3")

    plt.xlabel('월')
    plt.ylabel('평균기온(℃)')
    plt.title(str(year1)+'년 vs. '+str(year2)+'년 월별 평균기온')
    plt.legend()

    # x축 눈금 설정
    plt.xticks(range(1, 13), ['01월', '02월', '03월', '04월', '05월', '06월', '07월', '08월', '09월', '10월', '11월', '12월'])

    filename = 'tempGraph_'+str(year1)+'_'+str(year2)+'.png'
    filepath = '/allnew/python/project2/html/public/media/' + filename  # 파일 경로 수정
    plt.savefig(filepath, dpi=400, bbox_inches='tight')
    plt.close()

    return {"message": "그래프가 생성되었습니다.", "filename": filename}


@app.get('/combined_frame/{year1}/{year2}')
async def combined_frame(year1: int, year2: int):
# query 변수 생성. $regex 연산자를 사용하여 "년월"필드 값이 'year1' 또는 'year2'로 시작하는지 확인
    query = {"년월": {"$regex": f"^{year1}|^{year2}"}}
# query를 사용하여 MongoDB에서 해당 쿼리 실행, 결과를 리스트로 반환
    result = list(mycol.find(query))
# 결과를 DataFrame으로 변환
    df = pd.DataFrame(result)
# "년월" 열의 값을 날짜/시간 형식으로 변환
    df["Year"] = pd.to_datetime(df["년월"]).dt.year
    df["Month"] = pd.to_datetime(df["년월"]).dt.month
# df.pivot()을 사용하여 "Year"를 인덱스, "Month"를 열, "평균기온"을 값으로 하는 피벗 테이블 생성
    df_pivot = df.pivot(index="Year", columns="Month", values="평균기온(℃)")
# df_pivot.columns를 정렬해 열을 연도 및 월 순서로 재정렬
    df_pivot = df_pivot.reindex(columns=sorted(df_pivot.columns, key=lambda x: int(x)))

    return df_pivot

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)