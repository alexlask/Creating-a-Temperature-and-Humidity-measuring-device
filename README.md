

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

![image](https://github.com/Lorsted/Creating-a-Temperature-and-Humidity-measuring-device/assets/117736750/4c6a6c5f-f2a2-4fa2-92a5-5ae574689c61)# Creating a Temperature and Humidity measuring device

## Platform

For this project, we have chosen Adafruit as the platform of choice. Adafruit provides a user-friendly and free platform that is particularly suitable for beginners. One of its key features is the ability to create simple visualizations that effectively present data.

To begin, we need to set up an account on Adafruit IO. This account will enable us to take advantage of the platform's data logging and visualization capabilities. Once registered, we can create two separate feeds—one for temperature and another for humidity. The process of setting up feeds is well-documented in the instructions provided on the Adafruit website.

By following the provided instructions, we can easily create feeds on Adafruit IO for temperature and humidity. These feeds will serve as repositories for storing and organizing the sensor data collected by the Raspberry Pi Pico WH. Subsequently, we can leverage Adafruit's visualization tools to present the data in a clear and easily comprehensible manner.
