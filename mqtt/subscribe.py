import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code: {reason_code}")
    client.subscribe("home/sensors/temp")

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic} | Message: {str(msg.payload.decode())}")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("127.0.0.1", 1883, 60)

mqttc.loop_forever()