## FUZZY LOGIC MicroPython module - MANDANI INFERENCE
## Script version 2.0 - Created by Ivan Fernandez Alonso
## 26/07/2022
## Functions find_temp and find_hum will find the value for y2 = m(x2 - x1) + y1 of the
## respective membership functions for temperature and humidity
## check appendix for more information

def find_temp(temp):
    global low_temp, mid_temp, high_temp, very_high_temp
    print('Temperature values')

    if temp >= 18 and temp < 21.5:
        low_temp = round(-0.2857 * (temp - 18) + 1, 2)  # y2 = m(x2 - x1) + y1, number of digits
        mid_temp = round(0.2857 * (temp - 18) + 0, 2)
        high_temp = 0
        very_high_temp = 0
        print('low ', low_temp, 'middle ', mid_temp, 'high ', high_temp, 'very high ', very_high_temp)

    elif temp >= 21.5 and temp < 25:
        low_temp = 0
        mid_temp = round(-0.2857 * (temp - 21.5) + 1, 2)
        high_temp = round(0.2857 * (temp - 21.5) + 0, 2)
        very_high_temp = 0
        print('low ', low_temp, 'middle ', mid_temp, 'high ', high_temp, 'very high ', very_high_temp)

    elif temp >= 25 and temp < 28.5:
        low_temp = 0
        mid_temp = 0
        high_temp = round(-0.2857 * (temp - 25) + 1, 2)
        very_high_temp = round(0.2857 * (temp - 25) + 0, 2)
        print('low ', low_temp, 'middle ', mid_temp, 'high ', high_temp, 'very high ', very_high_temp)

    elif temp >= 28.5:
        low_temp = 0
        mid_temp = 0
        high_temp = 0
        very_high_temp = 1
        print('low ', low_temp, 'middle ', mid_temp, 'high ', high_temp, 'very high ', very_high_temp)


def find_hum(hum):
    global very_low_hum, low_hum, mid_hum, high_hum, very_high_hum
    print('Humidity values')

    if hum >= 50 and hum < 62.5:
        very_low_hum = round(-0.08 * (hum - 50) + 1, 2)
        low_hum = round(0.08 * (hum - 50) + 0, 2)
        mid_hum = 0
        high_hum = 0
        very_high_hum = 0
        print('very low ', very_low_hum, 'low ', low_hum, 'middle ', mid_hum, 'high ', high_hum, 'very high ',
              very_high_hum)

    elif hum >= 62.5 and hum < 75:
        very_low_hum = 0
        low_hum = round(-0.08 * (hum - 62.5) + 1, 2)
        mid_hum = round(0.08 * (hum - 62.5) + 0, 2)
        high_hum = 0
        very_high_hum = 0
        print('very low ', very_low_hum, 'low ', low_hum, 'middle ', mid_hum, 'high ', high_hum, 'very high ',
              very_high_hum)

    elif hum >= 75 and hum < 87.5:
        very_low_hum = 0
        low_hum = 0
        mid_hum = round(-0.08 * (hum - 75) + 1, 2)
        high_hum = round(0.08 * (hum - 75) + 0, 2)
        very_high_hum = 0
        print('very low ', very_low_hum, 'low ', low_hum, 'middle ', mid_hum, 'high ', high_hum, 'very high ',
              very_high_hum)

    elif hum >= 87.5 and hum <= 99:
        very_low_hum = 0
        low_hum = 0
        mid_hum = 0
        high_hum = round(-0.08 * (hum - 87.5) + 1, 2)
        very_high_hum = round(0.08 * (hum - 87.5) + 0, 2)
        print('very low ', very_low_hum, 'low ', low_hum, 'middle ', mid_hum, 'high ', high_hum, 'very high ',
              very_high_hum)


def motion_detection(presence):
    global detection

    if presence == 0:
        detection = 0

    elif presence == 1:
        detection = 1


## FUZZY SET OF RULES and MINIMUM FUNCTION

## The temperature could be defined as:
## Low temperature – less than 19.75 ºC but more than 18 ºC
## Middle temperature – less than 23.25 ºC but more than 19.75 ºC
## High temperature – less than 26.75 ºC but more than 23.25 ºC
## Very high temperature - more than 26.75 ºC

## The relative humidity could be defined as:
## Very low humidity – Less than 56.25 %
## Low humidity – Less than 68.75% but more than 56.25 %
## Middle humidity – Less than 81.25 % but more than 68.75 %
## High humidity – Less than 93.75 % but more than 81.25 %
## Very high humidity – Higher than 93.75 %


def fuzzy():
    global R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40

    if detection == 0:

        ## R1.	IF temperature is low AND the humidity is very low AND presence is NOT detected THEN the speed is very low.
        R1 = min(low_temp, very_low_hum)

        R2 = 0
        ## R3.	IF temperature is low AND the humidity is low AND presence is NOT detected THEN the speed is very low.
        R3 = min(low_temp, low_hum)

        R4 = 0
        ## R5.	IF temperature is low AND the humidity is middle AND presence is NOT detected THEN the speed is middle.
        R5 = min(low_temp, mid_hum)

        R6 = 0
        ## R7.	IF temperature is low AND the humidity is high AND presence is NOT detected THEN the speed is fast.
        R7 = min(low_temp, high_hum)

        R8 = 0
        ## R9.	IF temperature is low AND the humidity is very high AND presence is NOT detected THEN the speed is fast.
        R9 = min(low_temp, very_high_hum)

        R10 = 0
        ## R11 IF temperature is middle AND the humidity is very low AND presence is NOT detected THEN the speed is very low.
        R11 = min(mid_temp, very_low_hum)

        R12 = 0
        ## R13 IF temperature is middle AND the humidity is low AND presence is NOT detected THEN the speed is very low.
        R13 = min(mid_temp, low_hum)

        R14 = 0
        ## R15	IF temperature is middle AND the humidity is middle AND presence is NOT detected THEN the speed is middle.
        R15 = min(mid_temp, mid_hum)

        R16 = 0
        ## R17	IF temperature is middle AND the humidity is high AND presence is NOT detected THEN the speed is middle.
        R17 = min(mid_temp, high_hum)

        R18 = 0
        ## R19	IF temperature is middle AND the humidity is very high AND presence is NOT detected THEN the speed is fast.
        R19 = min(mid_temp, very_high_hum)

        R20 = 0
        ## R21	IF temperature is high AND the humidity is very low AND presence is NOT detected THEN the speed is very low.
        R21 = min(high_temp, very_low_hum)

        R22 = 0
        ## R23	IF temperature is high AND the humidity is low AND presence is NOT detected THEN the speed is very low.
        R23 = min(high_temp, low_hum)

        R24 = 0
        ## R25	IF temperature is high AND the humidity is middle AND presence is NOT detected THEN the speed is low.
        R25 = min(high_temp, mid_hum)

        R26 = 0
        ## R27	IF temperature is high AND the humidity is high AND presence is NOT detected THEN the speed is middle.
        R27 = min(high_temp, high_hum)

        R28 = 0
        ## R29	IF temperature is high AND the humidity is very high AND presence is NOT detected THEN the speed is middle.
        R29 = min(high_temp, very_high_hum)

        R30 = 0
        ## R31	IF temperature is very high AND the humidity is very low AND presence is NOT detected THEN the speed is very low.
        R31 = min(very_high_temp, very_low_hum)

        R32 = 0
        ## R33	IF temperature is very high AND the humidity is low AND presence is NOT detected THEN the speed is very low.
        R33 = min(very_high_temp, low_hum)

        R34 = 0
        ## R35	IF temperature is very high AND the humidity is middle AND presence is NOT detected THEN the speed is low.
        R35 = min(very_high_temp, mid_hum)

        R36 = 0
        ## R37	IF temperature is very high AND the humidity is high AND presence is NOT detected THEN the speed is middle.
        R37 = min(very_high_temp, high_hum)

        R38 = 0
        ## R39	IF temperature is very high AND the humidity is very high AND presence is NOT detected THEN the speed is fast.
        R39 = min(very_high_temp, very_high_hum)

        R40 = 0

    elif detection == 1:

        R1 = 0
        ## R2.	IF temperature is low AND the humidity is very low AND presence is detected THEN the speed is low.
        R2 = min(low_temp, very_low_hum)

        R3 = 0
        ## R4.	IF temperature is low AND the humidity is low AND presence is detected THEN the speed is low.
        R4 = min(low_temp, low_hum)

        R5 = 0
        ## R6.	IF temperature is low AND the humidity is middle AND presence is detected THEN the speed is middle.
        R6 = min(low_temp, mid_hum)

        R7 = 0
        ## R8.	IF temperature is low AND the humidity is high AND presence is detected THEN the speed is fast.
        R8 = min(low_temp, high_hum)

        R9 = 0
        ## R10.	IF temperature is low AND the humidity is very high AND presence is detected THEN the speed is very fast.
        R10 = min(low_temp, very_high_hum)

        R11 = 0
        ## R12 IF temperature is middle AND the humidity is very low AND presence is detected THEN the speed is very low.
        R12 = min(mid_temp, very_low_hum)

        R13 = 0
        ## R14 IF temperature is middle AND the humidity is low AND presence is detected THEN the speed is low.
        R14 = min(mid_temp, low_hum)

        R15 = 0
        ## R16	IF temperature is middle AND the humidity is middle AND presence is detected THEN the speed is fast.
        R16 = min(mid_temp, mid_hum)

        R17 = 0
        ## R18	IF temperature is middle AND the humidity is high AND presence is detected THEN the speed is fast.
        R18 = min(mid_temp, high_hum)

        R19 = 0
        ## R20	IF temperature is middle AND the humidity is very high AND presence is detected THEN the speed is very fast.
        R20 = min(mid_temp, very_high_hum)

        R21 = 0
        ## R22	IF temperature is high AND the humidity is very low AND presence is detected THEN the speed is very low.
        R22 = min(high_temp, very_low_hum)

        R23 = 0
        ## R24	IF temperature is high AND the humidity is low AND presence is detected THEN the speed is very low.
        R24 = min(high_temp, low_hum)

        R25 = 0
        ## R26	IF temperature is high AND the humidity is middle AND presence is detected THEN the speed is middle.
        R26 = min(high_temp, mid_hum)

        R27 = 0
        ##  R28	IF temperature is high AND the humidity is high AND presence is detected THEN the speed is fast
        R28 = min(high_temp, high_hum)

        R29 = 0
        ## R30	IF temperature is high AND the humidity is very high AND presence is detected THEN the speed is very fast
        R30 = min(high_temp, very_high_hum)

        R31 = 0
        ## R32	IF temperature is very high AND the humidity is very low AND presence is detected THEN the speed is very low.
        R32 = min(very_high_temp, very_low_hum)

        R33 = 0
        ## R34	IF temperature is very high AND the humidity is low AND presence is detected THEN the speed is very low.
        R34 = min(very_high_temp, low_hum)

        R35 = 0
        ## R36	IF temperature is very high AND the humidity is middle AND presence is detected THEN the speed is middle.
        R36 = min(very_high_temp, mid_hum)

        R37 = 0
        ##  R38	IF temperature is very high AND the humidity is high AND presence is detected THEN the speed is fast
        R38 = min(very_high_temp, high_hum)

        R39 = 0
        ## R40	IF temperature is very high AND the humidity is very high AND presence is detected THEN the speed is very fast
        R40 = min(very_high_temp, very_high_hum)

    print('END OF FUZZYFICATION')


## MAXIMUM values for the membership functions for speed

def maximum():
    global speed_very_low, speed_low, speed_middle, speed_fast, speed_very_fast

    speed_very_low = max(R1, R3, R11, R12, R13, R21, R22, R23, R24, R31, R32, R33, R34)
    speed_low = max(R2, R4, R14, R25, R35)
    speed_middle = max(R5, R6, R15, R17, R26, R27, R29, R36, R37)
    speed_fast = max(R7, R8, R9, R16, R18, R19, R28, R38, R39)
    speed_very_fast = max(R10, R20, R30, R40)

#    print('very low speed membership', speed_very_low)
#    print('low speed membership', speed_low)
#    print('middle speed membership', speed_middle)
#    print('fast speed membership', speed_fast)
#    print('very fast speed membership', speed_very_fast)

#    print('END OF... JOIN ME FOR A RIDE, SPEED UP THE MUSIC, MAXIMUM OVERDRIVE ')


## DEFUZZIFICATION

## 1. CENTRE OF AREA

def centre():

    global dcog

    dsvl = 25 * speed_very_low
    dsl = 25 * speed_low
    dsm = 25 * speed_middle
    dsf = 25 * speed_fast
    dsvf = 25 * speed_very_fast

    ## 2. CENTRE OF GRAVITY

    wsvl = dsvl * 0
    wsl = dsl * 25
    wsm = dsm * 50
    wsf = dsf * 75
    wsvf = dsvf * 100

    num = wsvl + wsl + wsm + wsf + wsvf
    den = dsvl + dsl + dsm + dsf + dsvf
    dcog = int(num / den)

#    print('End of centre function')
    print('dcog: ', dcog)


def final_value():
    ## the distance of centre of gravity is given between 0 and 99 value
    ## PWM duty cycle is expected to initiate from 50% up to 100% where the
    ## PWM range is between 0 and 1023
    ## The duty cycle is shifted by adding a constant

    data_control = int((dcog * 1023) / 99)
    print('Data control: ', data_control)
    return data_control


def init(temp_rcv, hum_rcv, presence_rcv):

    i = 0

    global dcog

    while i < 1:

        temperature = 0
        humidity = 0
        presence = 0

        if temp_rcv < 18 and hum_rcv < 50:
            dcog = 0
            print('dcog: ', dcog)
            print('END OF THE PROCESS', 'Temperature: ', temp_rcv, 'Humidity: ', hum_rcv)
            i = i + 1

        elif temp_rcv >= 18 and hum_rcv < 50:
            dcog = 0
            print('dcog: ', dcog)
            print('END OF THE PROCESS', 'Temperature: ', temp_rcv, 'Humidity: ', hum_rcv)
            i = i + 1

        elif temp_rcv < 18 and hum_rcv > 50:
            dcog = 0
            print('dcog: ', dcog)
            print('END OF THE PROCESS', 'Temperature: ', temp_rcv, 'Humidity: ', hum_rcv)
            i = i + 1

        elif temp_rcv >= 18 and hum_rcv >= 50:
            temperature = temp_rcv
            humidity = hum_rcv
            presence = presence_rcv
            find_temp(temperature)
            find_hum(humidity)
            motion_detection(presence)
            fuzzy()
            maximum()
            centre()
            final_value()
            print('END OF THE FUZZY PROCESS')
            i = i + 1
