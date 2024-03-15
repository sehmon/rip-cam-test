
import RPi.GPIO as GPIO
import time

mp1, mp2, me1 = 20, 16, 21
mp3, mp4, me2 = 25, 24, 12
mp5, mp6, me3 = 26, 18, 23
mp7, mp8, me4 = 6, 13, 5

chan_list = [
        mp1,
        mp2,
        mp3,
        mp4,
        mp5,
        mp6,
        mp7,
        mp8,
        me1,
        me2,
        me3,
        me4
        ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(me1, GPIO.LOW) # motor stop
GPIO.output(me2, GPIO.LOW) # motor stop
GPIO.output(me3, GPIO.LOW) # motor stop
GPIO.output(me4, GPIO.LOW) # motor stop

pwm1 = GPIO.PWM(me1, 1) # This is the pulse frequency of the pulse widths !
pwm2 = GPIO.PWM(me2, 1) # This is the pulse frequency of the pulse widths !
pwm3 = GPIO.PWM(me3, 1) # This is the pulse frequency of the pulse widths !
pwm4 = GPIO.PWM(me4, 1) # This is the pulse frequency of the pulse widths !

pwm1.start(5)
pwm2.start(5)
pwm3.start(5)
pwm4.start(5)

print('Press Ctrl+C to end the program...')
print('Raising...')
GPIO.output(mp1, GPIO.HIGH)  # clockwise
GPIO.output(mp2, GPIO.LOW)

GPIO.output(mp3, GPIO.HIGH)  # counterclockwise
GPIO.output(mp4, GPIO.LOW)

GPIO.output(me1, GPIO.HIGH) # motor driver enable
GPIO.output(me2, GPIO.HIGH) # motor driver enable

time.sleep(5)

GPIO.output(me1, GPIO.LOW) # motor stop
GPIO.output(me2, GPIO.LOW) # motor stop

time.sleep(0.5)

print('Dropping...')
pwm1.start(5) #decreasing dutycycle to 20
pwm2.start(5) #decreasing dutycycle to 20
GPIO.output(mp1, GPIO.LOW)   # counter-clockwise
GPIO.output(mp2, GPIO.HIGH)

GPIO.output(mp3, GPIO.HIGH)   # clockwise
GPIO.output(mp4, GPIO.LOW)

GPIO.output(me1, GPIO.HIGH) # motor driver enable
GPIO.output(me2, GPIO.HIGH) # motor driver enable

time.sleep(1.5)

GPIO.output(me1, GPIO.LOW) # motor stop
GPIO.output(me2, GPIO.LOW) # motor stop
time.sleep(0.5)

pwm1.stop()
pwm2.stop()

GPIO.cleanup()                     # Release resource

