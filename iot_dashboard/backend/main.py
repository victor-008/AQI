from fastapi import FastAPI
import pandas as pd
import os
from mqtt_client import start_mqtt

app = FastAPI()

CSV_FILE = "../sensor_data.csv"

start_mqtt()

@app.get("/")
def root():
    return{"status": "Air Quality Backend up and Running"}

@app.get("/data")
def get_data():
    if not os.path.exists(CSV_FILE):
        return[]
    
    df = pd.read_csv(CSV_FILE)
    df = df.tail(200)

    return df.to_dict(orient="records")

