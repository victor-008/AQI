import json
from datetime import datetime
from paho.mqtt import client as mqtt_client
from csv_logger import save_to_csv

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/greenhouse"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        data["timestamp"] = datetime.now().isoformat()
        save_to_csv(data)
        print("Data logged:", data)
    except Exception as e:
        print("Error processing message:", e)

def start_mqtt():
    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT)
    client.loop_start()

