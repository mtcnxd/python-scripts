import socket
import time

HOST = 'uconsole.local'
PORT = 65432

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
