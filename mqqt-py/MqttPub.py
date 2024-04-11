import paho.mqtt.client as mqtt

# Configuración del broker
BROKER = "localhost"  # Cambia a la dirección IP de tu broker si es necesario
PORT = 1883

# Callback cuando el mensaje es publicado
def on_publish(client, userdata, mid):
    print("Mensaje publicado!")

client = mqtt.Client()
client.on_publish = on_publish
client.connect(BROKER, PORT, 60)

# Publicar un mensaje
topic = "hospedaje/temperatura/cuarto1"
message = "¡Hola MQTT!"
client.publish(topic, message, qos=0)

client.disconnect()
