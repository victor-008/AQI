from pydantic import BaseModel

class SensorData(BaseModel):
    timestamp: str
    temperature: float
    humidity: float
    pm1_cf1: int
    pm25_cf1: int
    pm10_cf1: int
    pm1_atm: int
    pm25_atm: int
    pm10_atm: int
    pc_03: int
    pc_05: int
    pc_10: int
    pc_25: int
    pc_50: int
    pc_100: int
