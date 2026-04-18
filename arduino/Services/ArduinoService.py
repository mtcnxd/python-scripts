from serial import Serial

class ArduinoService:
	def __init__(self):
		try:
			self.port = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=5)

		except as error:
			print(f"Error al abrir el puerto: {error}")
			return

	def connect(self):
		pass

	def get_data(self):
		pass
