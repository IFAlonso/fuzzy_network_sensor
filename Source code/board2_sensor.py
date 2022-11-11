# script for Sensor BOARD 2 - version 1.20 (07/11/2022)

import network
import BME280
import time
from esp import espnow
from time import sleep
from machine import Pin
from machine import SoftI2C

#   A WLAN interface must be active to send()/recv()

wireless = network.WLAN(network.STA_IF)
wireless.active(True)					#  Station is activated


# ESPNOW BLOCK
e = espnow.ESPNow()
e.init()

peer1 = b'\xacg\xb27}\xb0'           # mac address of BOARD 1 HUB wifi interface
peer2 = b'\xec\x94\xcb[\xc2l'        # mac address of TEST BOARD
e.add_peer(peer1)
e.add_peer(peer2)


#  ESP32 - Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=8000)    # object for i2c bus
pir = Pin(19, Pin.IN)                                   # object input pin on GPI19 for PIR sensor
bme = BME280.BME280(i2c=i2c)                            # object for temp & hum sensor



#  MAIN FUNCTIONS

def sensor_bme():                       # funcion for the sensor BME280 temperature and humidity

    i = 1

    global temp, hum

    while i <= 1:

        temp = bme.temperature
        temp = str(int(float(temp)))
        hum = bme.humidity
        hum = str(int(float(hum)))
        print('Temperature: ', temp)        # just for control purposes on console
        print('Humidity: ', hum)            # just for control purposes on console
        i = i + 1

sensor_bme()


def sensor_pir():       # funcion for the PIR sensor module temperature and humidity

    i = 1

    global presence

    while i <= 1:

        presence = pir.value()      # it obtains a high state (detection) or low state (no presence)
        presence = str(int(float(presence)))

        # Console control
        print('Motion detection :', presence)   # just for control purposes on console
        i = i + 1

sensor_pir()


def data():

    data = temp + hum + presence    # data from sensors is packaged
    print('Data packaged: ', data)

    #  Send data to HUB board

    print('sending data to HUB')        # just for control purposes on console
    e.send(peer1, data, True)           # data package is sent to main HUB BOARD 1
    e.send(peer2, data, True)           # data package is sent to TEST BOARD

    print('data sent')


data()


# Global while

while True:                             # main while for calling the three functions

    sensor_bme()
    sensor_pir()
    data()
    print('PROCESS COMPLETED', '\n', '\n')      # just for control purposes on console
    time.sleep_ms(500)                                    # data sensing is processed every second
