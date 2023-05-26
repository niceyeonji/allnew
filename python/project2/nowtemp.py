import json
import urllib.request
from pymongo import MongoClient
from fastapi import FastAPI
import os

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

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        return None

def get_data_from_api(numOfRows, pageNo, st_ymd, ed_ymd, area_id, pa_crop_spe_id):
    end_point = 'https://apis.data.go.kr/1360000/FmlandWthrInfoService/getMmStatistics'
    parameters = ''
    parameters += "?serviceKey=" + get_secret("data_apiKey")
    parameters += "&pageNo=" + str(pageNo)
    parameters += "&numOfRows=" + str(numOfRows)   
    parameters += "&dataType=json"
    parameters += "&ST_YMD=" + str(st_ymd)
    parameters += "&ED_YMD=" + str(ed_ymd)
    parameters += "&AREA_ID=" + str(area_id)   
    parameters += "&PA_CROP_SPE_ID=" + str(pa_crop_spe_id)
    url = end_point + parameters

    result = getRequestUrl(url)
    if result is None:
        return None
    else:
        return url

def save_data_to_mongodb(ed_ymd,area_id,pa_crop_spe_id):
    pageNo = 1
    numOfRows = 10
    st_ymd=202304
    # ed_ymd=nowdate()
    nPage = 0  
    dictResult = [] 
    while(True):
        # print('pageNo : %d, nPage : %d, year:%d' % (pageNo, nPage,year))
        dictData =  get_data_from_api(numOfRows, pageNo, st_ymd, ed_ymd, area_id, pa_crop_spe_id)
        return dictData
        # print('-'*50)
        # print(dictData)

        if (dictData['response']['header']['resultCode'] == "00"):
            totalCount = dictData['response']['body']['totalCount']
            # print('데이터 총 개수 : ', totalCount)  

            for item in dictData['response']['body']['items']:
                # if not duplica(item["sn"],year):
                    dictResult.append(item)

            if totalCount == 0:
                break
            nPage = math.ceil(totalCount / numOfRows)
            if (pageNo == nPage):  
                break  

            pageNo += 1
        else :
            break
    if dictResult:
        mycol.insert_many(dictResult)
    return "데이터 추가되었습니다."

client = MongoClient(get_secret("ATLAS_ConnectionString"))
print('Connected to MongoDB....')

mydb = client['test']
mycol = mydb['projectnowtemp']

app = FastAPI()

@app.get('/nowtemp')
def nowtemp(ed_ymd,area_id,pa_crop_spe_id):
    result = save_data_to_mongodb(ed_ymd,area_id,pa_crop_spe_id)
    return result
# def get_temp_from_api(numOfRows: int, pageNo: int, ST_YMD: str, ED_YMD: str, AREA_ID: str, PA_CROP_SPE_ID: str):
#     data = get_data_from_api(numOfRows, pageNo, ST_YMD, ED_YMD, AREA_ID, PA_CROP_SPE_ID)
#     if data is None:
#         return "Failed to fetch data from the API."
#     else:
#         save_data_to_mongodb(mycol, data)
#         return "Data has been fetched from the API and saved to MongoDB."

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='0.0.0.0', port=3002)