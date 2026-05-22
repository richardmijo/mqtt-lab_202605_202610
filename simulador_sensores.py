import paho.mqtt.client as mqtt
import time
import random
import threading

BROKER = "localhost"
PORT = 1883

TOPICOS = {
    "temperatura": "uide/lab/temperatura",
    "humedad":     "uide/lab/humedad",
    "co2":         "uide/lab/co2",
}

# ── Subscriber ────────────────────────────────────────────────────────────────

def al_conectar(client, userdata, flags, reason_code, properties):
    print(f"[BROKER] Conectado — código: {reason_code}")
    for topico in TOPICOS.values():
        client.subscribe(topico)
        print(f"[SUB]    Suscrito a → {topico}")

def al_recibir_mensaje(client, userdata, msg):
    print(f"[MSG] {msg.topic:<30} → {msg.payload.decode()}")

def iniciar_subscriber():
    sub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriber-aula")
    sub.on_connect = al_conectar
    sub.on_message = al_recibir_mensaje
    sub.connect(BROKER, PORT, 60)
    sub.loop_forever()

def simular_sensor(nombre, topico, unidad, rango_min, rango_max, intervalo):
    pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"sensor-{nombre}")
    pub.connect(BROKER, PORT, 60)
    pub.loop_start()

    print(f"[SENSOR] {nombre} iniciado — publicando en '{topico}' cada {intervalo}s")

    try:
        while True:
            valor = round(random.uniform(rango_min, rango_max), 2)
            mensaje = f"{valor} {unidad}"
            pub.publish(topico, mensaje)
            time.sleep(intervalo)
    except KeyboardInterrupt:
        pass
    finally:
        pub.loop_stop()
        pub.disconnect()

if __name__ == "__main__":
    print("=" * 55)
    print("   Simulador IoT — Laboratorio MQTT (UIDE)")
    print("=" * 55)
    print("Presiona Ctrl+C para detener\n")

   
    hilo_sub = threading.Thread(target=iniciar_subscriber, daemon=True)
    hilo_sub.start()

    time.sleep(1)  

  
    sensores = [
        ("temperatura", TOPICOS["temperatura"], "°C",  18.0, 35.0, 2),
        ("humedad",     TOPICOS["humedad"],     "%HR", 40.0, 90.0, 3),
        ("co2",         TOPICOS["co2"],         "ppm", 400.0, 1200.0, 5),
    ]

    hilos = []
    for args in sensores:
        hilo = threading.Thread(target=simular_sensor, args=args, daemon=True)
        hilo.start()
        hilos.append(hilo)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Simulación detenida.")
