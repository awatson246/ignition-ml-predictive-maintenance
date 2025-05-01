import paho.mqtt.client as mqtt
import time
import random

broker = "192.168.106.9"  # use your Ignition Gateway IP if running MQTT Distributor there
topic = "pi/temperature"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    temp = random.randint(48, 52)
    message = f"{temp}"
    client.publish(topic, message)
    time.sleep(1)
