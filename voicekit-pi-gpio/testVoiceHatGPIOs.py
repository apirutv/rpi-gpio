import RPi.GPIO as GPIO
import time
from gpioController import GPIOController

pins = [26,6,13,5]

controls = []
i = 0
for pin in pins:
	controls.append(GPIOController(pin,GPIO.LOW))
	print("control " + str(i) + " initiated for gpio pin " + str(pin))
	i = i + 1

time.sleep(2)

try:
	for control in controls:
		control.output(GPIO.HIGH)
		print(control.input())
    		time.sleep(1)
    		control.output(GPIO.LOW)
    		print(control.input())
		time.sleep(2)
		
    	time.sleep(2)
	print("cleaning up GPIO")
	GPIO.cleanup()


# End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"

    # Reset GPIO settings

    GPIO.cleanup()