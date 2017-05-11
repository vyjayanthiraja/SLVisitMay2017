from picamera import PiCamera
from gpiozero import Button
from time import sleep
from image_ai import getEmotion

button = Button(4, pull_up=False)
with PiCamera() as camera:
    while True:
        sleep(5)
        button.wait_for_press()
        imageFileName = 'selfie.jpg'
        camera.capture(imageFileName)
        

