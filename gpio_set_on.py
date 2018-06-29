#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from gpioController import GPIOController

GPIO_BCM_PIN = 26  

control = GPIOController(GPIO_BCM_PIN,GPIO.LOW)

time.sleep(1)

while(True):
    if(control.input() == GPIO.LOW):
        print("setting pin " + str(GPIO_BCM_PIN) + " to GPIO.HIGH ...")
        control.output(GPIO.HIGH)
    else:
        print("setting pin " + str(GPIO_BCM_PIN) + " to GPIO.LOW ...")
        control.output(GPIO.LOW)
    time.sleep(2)

