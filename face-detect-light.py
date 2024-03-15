#!/usr/bin/python3

import board
import digitalio
import cv2
import RPi.GPIO as GPIO

from adafruit_servokit import ServoKit
from picamera2 import Picamera2

# Setup GPIO
led = digitalio.DigitalInOut(board.D24)
led.direction = digitalio.Direction.OUTPUT

# Setup Servos
kit = ServoKit(channels=16)

# Grab images as numpy arrays and leave everything else to OpenCV.
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

while True:
    im = picam2.capture_array()

    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    # Turn on light if face detected
    if len(faces) > 0:
        led.value = True
        kit.servo[15].angle = 180
    else:
        led.value = False
        kit.servo[15].angle = 0

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Camera", im)
    cv2.waitKey(1)
