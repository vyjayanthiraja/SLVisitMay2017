from picamera import PiCamera
from gpiozero import Button
from time import sleep
from image_ai import getEmotion

button = Button(4, pull_up=False)
while True:
    with PiCamera() as camera:
        sleep(5)
        button.wait_for_press()
        imageFileName = 'selfie.jpg'
        camera.capture(imageFileName)
        print(getEmotion(imageFileName))
        

