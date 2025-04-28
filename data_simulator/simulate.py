import csv
import random
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"  # address of MQTT servor/broker
MQTT_TOPIC = "sensor/data" # topic being published

client = mqtt.Client(client = mqtt.Client(callback_api_version=4)
client.connect(MQTT_BROKER)

filename = "output.csv"
headers = ["timestamp", "temperature", "vibration", "failure_risk"]

with open(filename, mode="a", newline="") as file:
    writer = csv.writer(file) # creates an object that can write row(s) to a file
    writer.writerow(headers) # writes a single row

def generate_data():
    timestamp = time.time()
    temp = random.randint(70, 90)
    vibration = random.randint(0, 20)
    failure = 1 if temp > 80 and vibration > 10 else 0
    return [timestamp, temp, vibration, failure]

def write_to_csv(data):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file) # creates an object that can write row(s) to a file
        writer.writerow(data) # writes a single row

def publish_mqtt(data):
    payload = {"timestamp": data[0], "temperature": data[1], "vibration": data[2], "failure": data[3]}
    print(payload)
    client.publish(MQTT_TOPIC, str(payload))

while True:
    data_row = generate_data()
    write_to_csv(data_row)
    publish_mqtt(data_row)
    #print(f"Generated and published: {data_row}")
    time.sleep(5)
