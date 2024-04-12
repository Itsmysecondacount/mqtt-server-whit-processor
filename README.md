# MQTT Server for Sensor Data and Processor

This project is an MQTT server setup that receives temperature data from various sensors and stores it in a database for monitoring and analysis purposes.

## Getting Started

To get the MQTT server up and running, simply navigate to the directory containing the `docker-compose.yml` file and execute the following command:

    bash
    	docker-compose up

If you need to change the port the MQTT server listens on, you can modify the port mapping in the docker-compose.yml file.

## Structure

Within the mqtt-py folder, you'll find a publisher (Pub) and a subscriber (Sub). The publisher is used to simulate data publishing, while the subscriber listens to an MQTT channel for incoming data.

There's also a data processor script that connects to a database to store the data along with the time it was taken and the type of value. The database structure is generalized to accommodate various types of sensor data such as humidity, flow, velocity, etc.

    class ValoresMQTTTemperatura(Base):
    __tablename__ = 'VALORES_MQTT_TEMPERATURA'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    date = Column(DateTime)
    topic = Column(String(255))
    value = Column(String(255))
    attribute1 = Column(String(255))
    attribute2 = Column(String(255))

To connect to your own database, simply change the database URL in the database module.

## Running the Python Files

To execute any Python file in the mqtt-py directory, use:

    python <file_name>.py

It is recommended to work within a virtual environment. Create one and activate it with:

    python -m venv .venv
    source .venv/bin/activate  # On Linux

After activating the virtual environment, install the required dependencies with:

    pip install -r requirements.txt

[Here's how to create a temperature sensor with esp32.](https://github.com/Itsmysecondacount/mqtt-esp32-read-temperature-of-solar-storage)

[Here's how to create a subscriber whit oled and esp32.](https://github.com/Itsmysecondacount/mqtt-sub-whit-display)
