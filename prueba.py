import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)

client.loop_start()

client.publish("uide/lab/temperaturas", "22.22")

client.disconnect()

print("Mensaje enviado")