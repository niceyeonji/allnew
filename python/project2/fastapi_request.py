import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/getmongo')
async def getMongo():
    baseurl = 'http://192.168.1.187:3000'
    try:
        response = requests.get(baseurl + '/getmongo')
        response.raise_for_status()  # 요청이 성공적으로 이루어졌는지 확인
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "db": "mongodb", "service": "/getmongo"}