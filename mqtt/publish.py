import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# Optional: Add authentication or TLS
# client.username_pw_set("user", "password")
# client.tls_set()

client.connect("127.0.0.1", 1883, 60)

client.loop_start()

data = {
    'message':'hola mundo',
    'data': '24.5',
    'status': 200
}

payload = json.dumps(data)

response = client.publish("home/sensors/temp", payload=payload, qos=1, retain=False)

if response.rc == mqtt.MQTT_ERR_SUCCESS:
    print("Publishing payload: ", payload)
else:
    print("Publish failed")

time.sleep(2)
client.loop_stop()
client.disconnect()
