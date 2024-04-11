import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session
import crud
import database
from datetime import datetime



# Función para obtener una nueva sesión de la base de datos
def get_db():
    return database.SessionLocal()

# Configuración del broker
BROKER = "localhost"  # Cambia a la dirección IP de tu broker si es necesario
PORT = 1883

# Callback cuando nos conectamos al broker
def on_connect(client, userdata, flags, rc):
    print("Conectado con el código: " + str(rc))
    client.subscribe("hospedaje/temperatura/#")

# Callback cuando recibimos un mensaje
def on_message(client, userdata, msg):
    temperatura_rec = msg.payload.decode()
    topico = msg.topic
    print(f"Mensaje recibido en el tópico {topico} -> {temperatura_rec}")
    db = get_db()  # Obtener una nueva sesión
    current_datetime = datetime.now()
    try:
        datos_creados = crud.insert_data_temperature(db, current_datetime , topico, temperatura_rec)
        print(datos_creados)
    finally:
        db.close()  # Asegúrate de cerrar la sesión

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

# Loop infinito para mantener la suscripción activa
client.loop_forever()
