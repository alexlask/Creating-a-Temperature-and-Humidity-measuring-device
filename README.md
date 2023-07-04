

Written by : Alexander Laskowski – al226nd
 
The purpose of this project is to be able to measure the temperature and humidity and with the help of wifi it will be possible to transfer the measured values to adafruit and later display these values using graphs. This is a project for beginners, and it should take approximately around 3-4 hours to complete the project.

## Objective

I have chosen to build this device because I thought it would be an interesting starting point to IoT and it filled a need which I had at the time as I was curious about the difference between temperature and humidity in rooms connected to each other. These measured values could be used as a starting point as to identify which rooms need to be better ventilated.

## Material

| Name  | Purpose | Name of Vendor | Price (SEK) |
| ------------- | ------------- | ------------- | ------------- |
| Raspberry Pi Pico WH  | Single board microcontroller with wireless function and headers soldered.  | Electrokit  | 109  |
| DHT11  | This sensor measures the Temperature and Humidity of the surrounding.  | Electrokit  | 49  |
| Breadboard | A simple device designed to let you create circuits without the need for soldering.  | Electrokit  | 69  |
| Jumper wires M-M | Used in order to connect the components.  | Electrokit  | 49  |
| Micro USB cable | The cable is used in order to connect the computer to the microcontroller and enabling both charging and the transfer of the program used. | Electrokit  | 39  |


## Computer Setup

For an IDE we use Visual Studio Code. On top of that we will use the PyMakr extension to upload code to the Pico WH. To use the extension we also need to install NodeJS.

### Setting up the environment

1. Install Python if you don't already have it installed.
2. Download and install NodeJS. Make sure to get the current version and not LTS.
3. Download and install the IDE VSCode.
4. Get the PyMakr extension in VSCode.
5. Update firmware on the Raspberry Pi Pico:
   - Download MicroPython firmware. This is a uf2 file. Make sure to get latest one from Releases and not Nightly builds.
   - Connect the micro-USB cable to the Raspberry Pi Pico.
   - While pushing the BOOTSEL button on the board, connect the other end of the micro-USB cable to your computer. After plugging it in you can release the BOOTSEL button.
   - A new drive should pop up in your file system named RPI-RP2 which is the Raspberry Pi Pico storage. Move the uf2, that you downloaded earlier, into this storage.
   - Wait for the board to automatically disconnect and reconnect.

## Putting it together

![image](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/assets/117736750/4c6a6c5f-f2a2-4fa2-92a5-5ae574689c61)

## Platform

For this project, we have chosen Adafruit as the platform of choice. Adafruit provides a user-friendly and free platform that is particularly suitable for beginners. One of its key features is the ability to create simple visualizations that effectively present data.

To begin, we need to set up an account on Adafruit IO. This account will enable us to take advantage of the platform's data logging and visualization capabilities. Once registered, we can create two separate feeds—one for temperature and another for humidity. The process of setting up feeds is well-documented in the instructions provided on the Adafruit website.

By following the provided instructions, we can easily create feeds on Adafruit IO for temperature and humidity. These feeds will serve as repositories for storing and organizing the sensor data collected by the Raspberry Pi Pico WH. Subsequently, we can leverage Adafruit's visualization tools to present the data in a clear and easily comprehensible manner.

## Code

We structure the code using the following format.

![image](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/assets/117736750/07bc71eb-ff3c-43c3-920e-0591a82a6471)

Here is an explanation of the 4 files in the project.

### boot.py
This file runs when the controller is booted. This file has information about how to connect to the wifi network. This file imports the details configured in the secrets.py file and uses it to connect to the network.

Link to the boot file can be found [here](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/blob/main/LNU_Project_Program%20-%20al226nd/boot.py).

### main.py
This file contains the core of the project. It in this file we configure the Adafruit IO settings as well as define the interval for sending data to the feed(s).

Link to the main file can be found [here](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/blob/main/LNU_Project_Program%20-%20al226nd/main.py)

### mqtt.py
This file contains functions related to MQTT. Is used in main when we import the MQTTClient class from this file.

Link to the mqtt file can be found [here](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/blob/main/LNU_Project_Program%20-%20al226nd/mqtt.py)

### secrets.py
This file contains the ssid and password for the wifi.

Link to the secrets file can be found [here](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/blob/main/LNU_Project_Program%20-%20al226nd/secrets.py)

## Transmitting data
In this project we are utilizing the local WiFi network in order to transfer the data readings every 15 seconds. Using the MQTT protocols we transfer to Adafruit in order to be able to display these readings in a Dashboard of our choosing.

## Presenting data
After having set up everything and getting it to run correctly. The Raspberry Pi Pico should now be sending weather data to the feeds specified. We later use these feeds in order to provide data to the dashboard in the way we would like to see them. I prefer to see to two graphs and to gauges to represent the current temperature and humidity and also the historical values recorded. The data is saved as soon as the feed(s) receive new data and is used in the graphs are the data readings from the last 48 hours.

![image](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/assets/117736750/c88b394d-0b51-4009-bb03-c48709a2a6d9)

## Final thoughts and design

Now we're done and we have a final design of our project. Considering this is a beginners project I think that the end results are good. We have a solid understanding of how to connect sensors, how to transfer this data and how to display it in a dashboard. In hindsight I think that I should have added another sensor such as a photosensor in order to have a more complete picture of how the weather is but all things considered I am content with the result.

![Final Picture](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/assets/117736750/feb2f01d-82b4-4625-9e88-ed58bab88300)
