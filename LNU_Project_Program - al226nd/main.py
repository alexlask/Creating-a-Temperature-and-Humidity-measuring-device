# main.py -- put your code here!

import dht
import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
from machine import Pin       # Define pin


# BEGIN SETTINGS
INTERVAL = 15000    # milliseconds
last_sent_ticks = 0  # milliseconds
dht11Sensor = dht.DHT11(machine.Pin(27))


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "YourUsernameHere"
AIO_KEY = "YourPasswordHere"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_TEMPERATURE_FEED = "YourTemperatureFeedHere"
AIO_HUMIDITY_FEED = "YourHumidityFeedHere"


# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.


# Function to publish temperature and humidity values to Adafruit IO MQTT server at previously specified interval
def send_data():
    global last_sent_ticks
    global INTERVAL

    if ((time.ticks_ms() - last_sent_ticks) < INTERVAL):
        return; # Too soon since last one sent.

    dht11Sensor.measure()
    temperature = dht11Sensor.temperature()
    humidity = dht11Sensor.humidity()
    print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))

    print("Publishing: {0} to {1} ... ".format(temperature, AIO_TEMPERATURE_FEED), end='')
    try:
        client.publish(topic=AIO_TEMPERATURE_FEED, msg=str(temperature))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_sent_ticks = time.ticks_ms()

    print("Publishing: {0} to {1} ... ".format(humidity, AIO_HUMIDITY_FEED), end='')
    try:
        client.publish(topic=AIO_HUMIDITY_FEED, msg=str(humidity))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_sent_ticks = time.ticks_ms()


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)


# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever
        client.check_msg()# Action a message if one is received. Non-blocking.
        send_data()       # Sends temperature and humidity readings to Adafruit IO if it's time.
finally:                  # If an exception is thrown ...
    client.disconnect()   # ... disconnect the client and clean up.
    client = None
    print("Disconnected from Adafruit IO.")
