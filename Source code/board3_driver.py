#  Programme for BOARD 3 DRIVER - Actuation board.
#  This MCU receives data from HUB MCU and provides PWM signal to fan driver.
#  BOARD 1 HUB / BOARD 2 SENSORS / BOARD 3 DRIVER
#  script ver 2.0


import network
import ubinascii
import time
from machine import Pin
from machine import PWM
from machine import Timer
from time import sleep
from esp import espnow
from machine import WDT


print('BOARD 3 DRIVER')

#   A WLAN interface must be active to send()/recv()

wireless = network.WLAN(network.STA_IF)
wireless.active(True)					    #  Station is activated
mac = wireless.config('mac')
print('mac address: ', mac)
mac2 = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
print('mac address decoded: ', mac2)


# ESPNOW
e = espnow.ESPNow()
e.init()

peer = b'\xec\x94\xcb[\xc2l'            #  mac address of test board
#  peer = b'\xacg\xb27}\xb0'            #  mac address of HUB BOARD 1 wifi interface
e.add_peer(peer)


#  Pin assigment:
pwm33 = PWM(Pin(33))            # create PWM object from a pin 33
pwm33.freq(1000)                # set PWM frequency from 1Hz to 40MHz


def data_recv():

    global data_raw

    z = 1

    while z <= 1:

        print('Waiting for data')

        msg = e.irecv()                    #  Data received
        data_raw = msg[1].decode()         # tuple can be decoded into str

        print('Data raw: ', data_raw)
        print('Lenth :', len(data_raw))
        print('END of recv')

        z = z + 1



def unwrap_data():

    global LIGHT, FAN_PWM

    z = 1

    while z <= 1:

        if len(data_raw) == 8:

            a, b, c, d, e, f, g, h = data_raw

            light = b
            fan_pwm = e + f + g

            LIGHT = int(light)
            FAN_PWM = int(fan_pwm)

            print('Light: ', LIGHT)
            print('Fan PWM: ', FAN_PWM)

        elif len(data_raw) == 9:

            a, b, c, d, e, f, g, h, i = data_raw

            light = b
            fan_pwm = e + f + g + h

            LIGHT = int(light)
            FAN_PWM = int(fan_pwm)

            print('Light: ', LIGHT)
            print('Fan PWM: ', FAN_PWM)

        z = z + 1



def light_service():

    pin25 = Pin(25, Pin.OUT)        # create output pin on GPIO25

    if LIGHT == 1:

        pin25.on()                  # set pin25 (high) level
        timer = Timer(0)
        timer.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:pin25.off())     #  test period 5 seconds
        print('Light is ON')

    else:

        print('Light is OFF')



def fan_service():

    if FAN_PWM >= 512:
        pwm33.duty(FAN_PWM)                 # set duty cycle
        print('Fan is ON')

    else:
        pwm33.duty(0)                     # turn off PWM on the pin
        print('Fan is OFF')



while True:

    data_recv()
    unwrap_data()
    light_service()
    fan_service()
    print('PROCESS COMPLETED', '\n', '\n')
    time.sleep_ms(500)                      # it needs to be in miliseconds
