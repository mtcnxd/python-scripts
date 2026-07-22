from serial import Serial

class ArduinoService:
	def __init__(self):
		self.port = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=5)

	def connect(self):
		pass

	def get_data(self):
		pass
