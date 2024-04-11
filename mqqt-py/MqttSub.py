import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session
import crud
import database
from datetime import datetime

# Function to obtain a new database session
def get_db():
    return database.SessionLocal()

# Broker configuration
BROKER = "localhost"  # Change to your broker's IP address if necessary
PORT = 1883

# Callback for when we connect to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with code: " + str(rc))
    client.subscribe("hosting/temperature/#")

# Callback for when we receive a message
def on_message(client, userdata, msg):
    received_temperature = msg.payload.decode()
    topic = msg.topic
    print(f"Message received on topic {topic} -> {received_temperature}")
    db = get_db()  # Get a new session
    current_datetime = datetime.now()
    try:
        created_data = crud.insert_data_temperature(db, current_datetime, topic, received_temperature)
        print(created_data)
    finally:
        db.close()  # Make sure to close the session

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

# Infinite loop to keep the subscription active
client.loop_forever()