from serial import Serial

class ArduinoService:
	def __init__(self):
		self.port = None
		self.data = []

	def __del__(self):
		if self.port is not None:
			self.port.close()

	def connect(self, port="/dev/ttyUSB0", baudrate=9600):
		self.port = Serial(port=port, baudrate=baudrate, timeout=5)

	def get_data(self) -> list:
		if self.port.in_waiting > 0:
			bytes_received = self.port.readline()
			decoded_data = bytes_received.decode().rstrip('\r\n')
			self.data = decoded_data.split(',')

			#print(f"Debug => Data: {self.data} | type: {type(self.data)}")

			return self.data

	def send_data(self, value):
		if self.port:
			self.port.write(value.encode())
			self.port.flush()

	
