import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Motor 1
ENA1 = 21
IN1 = 20
IN2 = 16

GPIO.setup(ENA1, GPIO.OUT)
PWM1 = GPIO.PWM(ENA1, 100)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

PWM1.start(8)
