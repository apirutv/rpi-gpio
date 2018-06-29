#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO_BCM_PIN = 6 

def my_callback(chanel):
    print("called back:" + str(chanel))

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BCM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(GPIO_BCM_PIN, GPIO.RISING, callback=my_callback, bouncetime=300)

while(True):
    time.sleep(1)
    print("value of pin " + str(GPIO_BCM_PIN) + " = " + str(GPIO.input(GPIO_BCM_PIN)))

