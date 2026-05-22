import paho.mqtt.client as mqtt
client = mqtt.Client(mqtt.CallbackAPIVersion. VERSION2)
client.connect("locahost", 1883, 60)

client.publish("uide/lab/temperaturas", "22.22")
client.disconnect()

print("Mensaje enviado")
