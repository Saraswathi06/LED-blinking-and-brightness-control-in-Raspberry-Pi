# import modules
import RPi.GPIO as GPIO
import time
 
# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
 
# loop 5 times
for i in range(5):
 
	# flash output pin 3
        GPIO.output(8, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(8, GPIO.LOW)
        time.sleep(1)
 
	# read input pin 5
	if GPIO.input(12) == GPIO.HIGH:
    	print("Pin 12 is on")
	else:
    	print("Pin 12 is off")
