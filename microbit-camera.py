from picamera import PiCamera
from gpiozero import Button
from time import sleep
from image_ai import *
from utils import *

imageFileName = 'photo.jpg'
button = Button(4, pull_up=False)
with PiCamera() as camera:
    sleep(5)
    while True:
        button.wait_for_press()
        camera.image_effect = 'colorswap'
        camera.capture(imageFileName)
        subject = getDescription(imageFileName)
        sendMail('vyjayanthi.raja@gmail.com', subject, imageFileName)
        print("Finished sending email")

