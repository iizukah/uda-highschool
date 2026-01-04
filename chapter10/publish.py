import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)
for i in range(5):
    message = "hoge\n"
    client.publish("orz", message)
    print(f"send: {message}")
    time.sleep(1)

client.disconnect()
