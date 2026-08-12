import socket
import time

HOST = '127.0.0.1'
PORT = 6600

counter = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
        
        while counter < 20:
            counter +=1
            message = f"counter: {counter}"
            client.sendall(message.encode())
        
            response = client.recv(1024)
            print(f"Received: {response.decode()}")
            
            time.sleep(0.5)

    except Exception as error:
        print(error)
