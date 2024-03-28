import paho.mqtt.client as mqtt
import requests
import json
from datetime import datetime, timedelta


# MQTT Broker Details
broker_address = "mqtt.thingspeak.com"
broker_port = 1883
username = "mwa0000032926629"
password = "8ZDNURZD3Q6PE5EU"

# Function to handle MQTT messages
def on_message(client, userdata, message):
    # Parse received message
    payload = json.loads(message.payload)
    station_id = payload["station_id"]
    temperature = payload["temperature"]
    humidity = payload["humidity"]
    co2 = payload["co2"]

    # Store data to ThingSpeak
    thingspeak_update(station_id, temperature, humidity, co2)

# Function to update ThingSpeak channel with sensor data
def thingspeak_update(station_id, temperature, humidity, co2):
    url = f"https://api.thingspeak.com/update?api_key=YOUR_THINGSPEAK_WRITE_API_KEY&field1={temperature}&field2={humidity}&field3={co2}"
    response = requests.get(url)
    print("ThingSpeak update status:", response.status_code)

# Function to retrieve latest sensor data from ThingSpeak
def get_latest_sensor_data(station_id):
    url = f"https://api.thingspeak.com/channels/{station_id}/feeds.json?api_key=YOUR_THINGSPEAK_READ_API_KEY&results=1"
    response = requests.get(url)
    data = response.json()["feeds"][0]
    temperature = data["field1"]
    humidity = data["field2"]
    co2 = data["field3"]
    print("Latest Sensor Data:")
    print(f"Temperature: {temperature}°C, Humidity: {humidity}%, CO2: {co2} ppm")

# Function to retrieve sensor data for the last five hours from ThingSpeak
def get_sensor_data_last_five_hours(station_id):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=5)
    start_str = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_str = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    url = f"https://api.thingspeak.com/channels/{station_id}/feeds.json?api_key=YOUR_THINGSPEAK_READ_API_KEY&start={start_str}&end={end_str}"
    response = requests.get(url)
    data = response.json()["feeds"]
    print("Sensor Data for the Last Five Hours:")
    for entry in data:
        print(f"Time: {entry['created_at']}, Temperature: {entry['field1']}°C, Humidity: {entry['field2']}%, CO2: {entry['field3']} ppm")

# Initialize MQTT client
client = mqtt.Client()
client.username_pw_set(username, password)
client.on_message = on_message
client.connect(broker_address, broker_port)
client.subscribe("channels/+/subscribe/json", qos=1)

# Start MQTT loop
client.loop_forever()
