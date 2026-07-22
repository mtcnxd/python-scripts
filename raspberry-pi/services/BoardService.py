import RPi.GPIO as gpio
import time

class BoardService:
    def __init__(self):
        self.ledPin = 18
        pass

    def blink(self):
        gpio.output(self.ledPin, True)
        time.sleep(0.5)
        gpio.output(self.ledPin, False)
        time.sleep(0.5)