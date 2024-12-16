from fastapi import FastAPI
import datetime
from functools import lru_cache


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the home page!"}

@app.get("/prueba/{fecha}")
def read_hello(fecha: str):
    fecha=datetime.datetime.strptime(fecha,"%Y-%m-%d")
    tomorrow=fecha+datetime.timedelta(days=1)
    return {"message": "Mañana es "+tomorrow.strftime("%Y-%m-%d")}



