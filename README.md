# IoT System Development Documentation

## Overview
This repository contains documentation for the development of an IoT (Internet of Things) system consisting of two stations. Station 1 collects environmental data from virtual sensors deployed in the Wokwi platform and transmits it to ThingSpeak for storage and visualization. Station 2 generates simulated sensor data using Python in Google Colab and publishes it to ThingSpeak via MQTT protocol.

## Station 1: Wokwi Integration

### Integration with Wokwi
- The virtual station data was collected from Wokwi, an online platform for simulating Arduino projects.
- Sensors for temperature and humidity were interfaced with the DHT22 sensor within the Wokwi environment.
- A random number generator was implemented for the CO2 sensor since it was not available in Wokwi.
- The virtual station was configured to periodically generate sensor readings.

### Arduino Code Development
- Arduino code was developed to interface with the sensors and Wokwi platform.
- Libraries such as `WiFi.h`, `DHTesp.h`, and `ThingSpeak.h` were included to enable Wi-Fi connectivity, DHT22 sensor functionality, and communication with ThingSpeak.
- Constants were defined for sensor GPIO pin, Wi-Fi credentials, ThingSpeak channel number, API key, and server address.
- A function `generateCO2Value()` was implemented to simulate CO2 values within the specified range using a random number generator.
- The code continuously read sensor data, transmitted it to ThingSpeak, and monitored the data transmission status.

### Data for Station 1
- The transmitted data to ThingSpeak for Station 1 included temperature, humidity, and CO2 concentration.

### Visualization
- Visualizations for temperature, humidity, and CO2 concentration were generated for Station 1 using ThingSpeak's built-in visualization tools.

## Station 2: Python Code in Google Colab

### Setup
- The Python code was executed in Google Colab, leveraging its computational resources and collaborative features.
- Libraries such as `paho.mqtt.client`, `random`, and `time` were imported for MQTT communication, random number generation, and time manipulation, respectively.
- Variables and settings for MQTT communication and ThingSpeak channel configuration were defined.

### Main Code
- A Python script was developed to simulate the generation of random sensor readings for temperature, humidity, and CO2 levels.
- Sensor data was published to a ThingSpeak channel using MQTT protocol.
- Exception handling was included to gracefully handle keyboard interrupt.

### Data for Station 2
- The generated sensor data for temperature, humidity, and CO2 levels was transmitted to ThingSpeak for Station 2.

### Visualization
- Visualizations for temperature, humidity, and CO2 concentration were generated for Station 2 using ThingSpeak's built-in visualization tools.

## Conclusion
This IoT system demonstrates the integration of virtual and simulated sensors with ThingSpeak for real-time data collection and visualization. It provides insights into environmental parameters and showcases the capabilities of Wokwi and Google Colab in IoT development.

