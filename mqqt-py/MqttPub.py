import paho.mqtt.client as mqtt

# Broker configuration
BROKER = "localhost"  # Change this to your broker's IP address if necessary
PORT = 1883

# Callback when a message is published
def on_publish(client, userdata, mid):
    print("Message published!")

client = mqtt.Client()
client.on_publish = on_publish
client.connect(BROKER, PORT, 60)

# Publish a message
topic = "hosting/temperature/room1"
message = "Hello MQTT!"
client.publish(topic, message, qos=0)

client.disconnect()