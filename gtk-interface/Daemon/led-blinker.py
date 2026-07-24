import RPi.GPIO as gpio
import time

class BoardService:
    def __init__(self):
        # Select the fisical pin 12 (GPIO18)
        self.ledPin = 12
        
        # Configure the pinout as fisical pin numbers
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.ledPin, gpio.OUT)

    def blink(self):
        gpio.output(self.ledPin, True)
        time.sleep(0.10)
        gpio.output(self.ledPin, False)
        time.sleep(0.15)

    def cleanup(self):
        gpio.cleanup()


try:
    while True:
        board_service = BoardService()
        board_service.blink()
        time.sleep(3)

except Exception as error:
    print(f"ERROR: {error}")
    board_service.cleanup()

finally:
    board_service.cleanup()
        
