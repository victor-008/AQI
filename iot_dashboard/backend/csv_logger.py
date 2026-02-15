import csv
import os

CSV_FILE = "../sensor_data.csv"

FIELDNAMES = [
    "timestamp",
    "temperature",
    "humidity",
    "pm1_cf1",
    "pm25_cf1",
    "pm10_cf1",
    "pm1_atm",
    "pm25_atm",
    "pm10_atm",
    "pc_03",
    "pc_05",
    "pc_10",
    "pc_25",
    "pc_50",
    "pc_100"
]

def save_to_csv(record):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()
        writer.writerow(record)