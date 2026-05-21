# Laboratorio MQTT con Mosquitto

Este proyecto tiene como objetivo demostrar el funcionamiento básico de **MQTT** en un entorno de Internet de las Cosas (IoT), utilizando **Mosquitto** como broker de mensajería.

La práctica permite simular cómo diferentes dispositivos, sensores o aplicaciones pueden comunicarse entre sí mediante mensajes ligeros, organizados por tópicos.

---

## ¿Qué es MQTT?

**MQTT** significa *Message Queuing Telemetry Transport*. Es un protocolo de comunicación ligero, muy utilizado en proyectos de **IoT**, donde existen dispositivos con recursos limitados o conexiones de red inestables.

A diferencia de otros modelos donde dos aplicaciones se comunican directamente, MQTT trabaja con un intermediario llamado **broker**.

Los dispositivos no se envían mensajes entre ellos directamente. En su lugar:

- Un dispositivo publica un mensaje.
- El mensaje llega al broker.
- El broker entrega el mensaje a los clientes interesados.

Esto permite una comunicación simple, flexible y eficiente.

---

## ¿Para qué sirve MQTT?

MQTT se utiliza principalmente para enviar y recibir datos entre dispositivos conectados.

Algunos ejemplos de uso son:

- Sensores de temperatura y humedad.
- Sistemas de monitoreo ambiental.
- Dispositivos ESP32 o Arduino conectados a internet.
- Aplicaciones móviles que reciben datos de sensores.
- Sistemas de domótica.
- Monitoreo industrial.
- Alertas automáticas de dispositivos IoT.

Por ejemplo, un sensor puede publicar la temperatura de un aula, y una aplicación puede recibir ese dato en tiempo real.

---

## Arquitectura básica de MQTT

MQTT trabaja con tres elementos principales:

```text
Dispositivo publicador  --->  Broker MQTT  --->  Dispositivo suscriptor