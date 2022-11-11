#  Programme for BOARD 1 HUB
#  This MCU will receive data from BOARD 2 (sensors) and will send data to BOARD 3
#  print builtin function is used along the programme to monitorise the lines on console
#  script ver 2.12 - 11/11/2022

import network
import ssd1306
import ubinascii
import time
import fuzzylogic
from machine import I2C
from machine import Pin
from time import sleep
from esp import espnow

i2c = I2C(scl=Pin(22), sda=Pin(21))     # i2c is obsolete, research on SoftI2C

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


#  A WLAN interface must be active to send()/recv()
wireless = network.WLAN(network.STA_IF)
wireless.active(True)
mac = wireless.config('mac')
print('MAC address of BOARD 1 HUB: ', mac)
#  mac = ubinascii.hexlify(network.WLAN().config('mac') , ':').decode()
#  print(mac)


# ESPNow

e = espnow.ESPNow()
e.init()

peer2 = b'0\xae\xa4\x96\xceA'      #  mac address of ESP32 BOARD 2 SENSORS
e.add_peer(peer2)

peer3 = b'0\xae\xa4\x96\xbf\x90'   #  mac address of ESP32 BOARD 3 driver
e.add_peer(peer3)


#  OLED DISPLAY 0.91 inch

oled.text('HUB DEVICE', 22, 5)
oled.text('______________________________', 0, 10)
oled.text('SMART HOME', 22, 30)
oled.text('SYSTEM', 37, 45)
oled.show()
sleep(2)

oled.fill(0)
oled.text('Waiting for', 20, 20)
oled.text('DATA', 45, 35)
oled.show()
sleep(1)

service_light = 'OFF'
service_fan = 'OFF'



def data_recv():

    global data_raw

    i = 1

    while i <= 1:
        msg = e.irecv()
        data_raw = msg[1].decode()
        if msg:
            print('data raw: ', data_raw)
            aa, bb, cc, dd, ee = data_raw
            temperature = aa + bb
            humidity = cc + dd
            detection = ee
            oled.fill(0)
            oled.text('[Temp]  [Hum]', 10, 3)
            oled.text(temperature, 22, 17)
            oled.text('C', 40, 17)
            oled.text(humidity, 82, 17)
            oled.text('%', 100, 17)
            oled.text('__________________', 0, 24)
            oled.text('Light status ', 2, 39)
            oled.text('Fan status ', 20, 56)
            oled.text(service_light, 105, 39)
            oled.text(service_fan, 105, 56)
            oled.show()
            i = i + 1



def unwrap():

    global temp, hum, state

    print('tuple content: ', data_raw)      # data2 tupla length 11
    a, b, c, d, e = data_raw
    temp = a + b
    hum = c + d
    state = e
    temp = int(temp)
    hum = int(hum)
    state = int(state)
    print('Temp:', temp)
    print('Hum:', hum)
    print('State:', state)



def control_light():

    global light, service_light

    if state == 0:
        light = 0
        service_light = 'OFF'

    elif state == 1:
        light = 1
        service_light = 'ON'

    print('End of control light function')



def control_fan():

    global fan, service_fan

    ## fuzzylogic.init(sensor temperature value, sensor humidity value)

    fuzzylogic.init(temp, hum)

    ## return the final duty cycle percentage into value object

    fan = fuzzylogic.final_value()

    print('End of control fan')


def data_send():

    i = 1

    data_dummy = light, fan

    while i <= 1:

        print('Data type: ', type(data_dummy))
        print('Data dummy: ', data_dummy)

        data_packed = str(data_dummy)           # tuple needs to be converted into string

        e.send(peer3, data_packed, True)

        print('Data dummy sent: ', data_packed)

        i = i + 1



while True:

    print('BOARD 1 HUB START PROGRAM')
    data_recv()
    unwrap()
    control_light()
    control_fan()
    data_send()
    print('PROCESS COMPLETED', '\n')
