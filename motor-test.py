import random
import time
import math
from adafruit_motorkit import MotorKit

kit = MotorKit()

print("Starting Up")
print("Waiting 3 seconds for startup")
kit.motor4.throttle = 0
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")

t = 0

while(True):
    t_throttle = min((math.sin(t) + 1) / 2, 1)
    print("Setting throttle to {}".format(t_throttle))
    kit.motor4.throttle = t_throttle
    time.sleep(0.2)
    kit.motor4.throttle = None
    time.sleep(1)
    t += 0.1
