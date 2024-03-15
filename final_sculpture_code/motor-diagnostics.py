
import RPi.GPIO as GPIO
import time
import atexit


mp1, mp2, me1 = 20, 16, 21
mp3, mp4, me2 = 25, 24, 12
mp5, mp6, me3 = 26, 18, 23
mp7, mp8, me4 = 6, 13, 5
mp9, mp10, me5 = 27, 22, 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(me1, GPIO.OUT)
GPIO.setup(me2, GPIO.OUT)
GPIO.setup(me3, GPIO.OUT)
GPIO.setup(me4, GPIO.OUT)
GPIO.setup(me5, GPIO.OUT)

GPIO.setup(mp1, GPIO.OUT)
GPIO.setup(mp2, GPIO.OUT)
GPIO.setup(mp3, GPIO.OUT)
GPIO.setup(mp4, GPIO.OUT)
GPIO.setup(mp5, GPIO.OUT)
GPIO.setup(mp6, GPIO.OUT)
GPIO.setup(mp7, GPIO.OUT)
GPIO.setup(mp8, GPIO.OUT)
GPIO.setup(mp9, GPIO.OUT)
GPIO.setup(mp10, GPIO.OUT)

GPIO.output(me1, GPIO.LOW) # motor stop
GPIO.output(me2, GPIO.LOW) # motor stop
GPIO.output(me3, GPIO.LOW) # motor stop
GPIO.output(me4, GPIO.LOW) # motor stop GPIO.output(me5, GPIO.LOW) # motor stop

pwm1 = GPIO.PWM(me1, 1) # This is the pulse frequency of the pulse widths !
pwm2 = GPIO.PWM(me2, 1.1) # This is the pulse frequency of the pulse widths !
pwm3 = GPIO.PWM(me3, 0.9) # This is the pulse frequency of the pulse widths !
pwm4 = GPIO.PWM(me4, 1) # This is the pulse frequency of the pulse widths !
pwm5 = GPIO.PWM(me5, 0.7) # This is the pulse frequency of the pulse widths !


def cleanup():
    print("Stoping motors and cleaning GPIO")
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()
    pwm5.stop()

    GPIO.cleanup()                     # Release resource


def run_ambient():
    print("Running ambient mode")
    pwm1.ChangeFrequency(1)
    pwm2.ChangeFrequency(1.1)
    pwm3.ChangeFrequency(0.9)
    pwm4.ChangeFrequency(1)
    pwm5.ChangeFrequency(0.7)

    GPIO.output(mp1, GPIO.LOW)   # counter-clockwise
    GPIO.output(mp2, GPIO.HIGH)
    GPIO.output(mp3, GPIO.LOW)   # clockwise
    GPIO.output(mp4, GPIO.HIGH)
    GPIO.output(mp5, GPIO.LOW)   # counter-clockwise
    GPIO.output(mp6, GPIO.HIGH)
    GPIO.output(mp7, GPIO.LOW)   # clockwise
    GPIO.output(mp8, GPIO.HIGH)
    GPIO.output(mp9, GPIO.LOW)   # clockwise
    GPIO.output(mp10, GPIO.HIGH)

    pwm1.start(4)
    pwm2.start(4)
    pwm3.start(5)
    pwm4.start(6)
    pwm5.start(1)

def run_sync():
    print("Running in Sync Mode")
    pwm1.ChangeFrequency(1)
    pwm2.ChangeFrequency(1)
    pwm3.ChangeFrequency(1)
    pwm4.ChangeFrequency(1)
    pwm5.ChangeFrequency(1)

    GPIO.output(mp1, GPIO.LOW)   # counter-clockwise
    GPIO.output(mp2, GPIO.HIGH)
    GPIO.output(mp3, GPIO.HIGH)   # clockwise
    GPIO.output(mp4, GPIO.LOW)
    GPIO.output(mp5, GPIO.HIGH)   # counter-clockwise
    GPIO.output(mp6, GPIO.LOW)
    GPIO.output(mp7, GPIO.LOW)   # clockwise
    GPIO.output(mp8, GPIO.HIGH)
    GPIO.output(mp9, GPIO.HIGH)   # clockwise
    GPIO.output(mp10, GPIO.LOW)

    pwm1.start(3)
    pwm2.start(4)
    pwm3.start(5)
    pwm4.start(6)
    pwm5.start(1)

def main():
    run_ambient()
    #run_sync()
    while(True):
        continue


if __name__ == "__main__":
    atexit.register(cleanup)
    main()
