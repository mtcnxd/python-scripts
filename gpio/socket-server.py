import socket

HOST = '0.0.0.0' # Listen any client
PORT = 65432

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server.bind((HOST, PORT))
		server.listen()

		print(f"Server listening on {HOST}:{PORT}")

		while True:
			conn, addr = server.accept()

			with conn:
				print(f"Client connected: {addr}")
				while True:
					data = conn.recv(1024)

					if not data:
						print(f"No data")
						break

					print(f"Data received: {data.decode()}")
					conn.sendall(data)

except Exception as error:
	print(error)
