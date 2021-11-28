import RPi.GPIO as GPIO 
import time
 
led = 8
 
GPIO.setmode( GPIO.BOARD) 
GPIO.setup( led, GPIO.OUT)
 
# 50Hz PWM Frequency 
pwm_led = GPIO.PWM( led, 50) 
# Full Brightness, 100% Duty Cycle 
pwm_led.start(100) 
5
for i in range(5):
          duty_s = raw_input("Enter Brightness Value (0 to 100):") 
          # Convert into Integer Value 
          duty = int(duty_s) 
          pwm_led.ChangeDutyCycle(duty) 
          time.sleep(1)
