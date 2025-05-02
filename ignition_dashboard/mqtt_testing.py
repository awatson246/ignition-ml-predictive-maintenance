import paho.mqtt.client as mqtt

broker = "192.168.103.13"  # Replace with your Ignition Gateway IP
port = 1883
topic = "my/test/topic"
message = "Hello from VS Code!"

client = mqtt.Client()
client.connect(broker, port)
client.publish(topic, message)
client.disconnect()
