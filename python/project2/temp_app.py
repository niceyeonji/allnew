from fastapi import FastAPI
from database import db_conn
from temp_models import Temp
from fastapi_temp import getmongo

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

@app.get('/')
async def healthCheck():
    return "OK"


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