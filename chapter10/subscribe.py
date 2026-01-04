import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"received: {msg.topic} {msg.payload.decode()}")
    with open("test.log", "a") as f:
        f.write(f"{msg.payload.decode()}")

def on_connect(client, userdata, flags, rc):
    print("connection OK")
    client.subscribe("orz")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
