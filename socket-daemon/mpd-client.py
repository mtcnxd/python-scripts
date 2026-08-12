import socket
from time import sleep

HOST = '127.0.0.1'
PORT = 6600

def mpd_send_command(client, command):
    client.sendall(f"{command}\n").encode()

    response = b''

    while True:
        data = client.recv(4096)
        response += data

        if b'\nOK\n' in response:
            break

        return response.decode()

def mpd_parse_response(response):
    data = {}
    for line in response.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            data[key] = value.strip()

    return data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))

        while True:
            client.sendall(b'currentsong\n')
            response = client.recv(1024).decode()

            current_track = mpd_parse_response(response)

            print(f"Artista: {current_track.get('Artist', 'Desconocido')}")
            print(f"Album: {current_track.get('Album', 'Desconocido')}")
            print(f"Titulo: {current_track.get('Title', 'Desconocido')}")
            print("="*30)
            sleep(1)

    except Exception as error:
        print(error)
