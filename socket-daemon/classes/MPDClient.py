import socket

class MPDClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def toggle_play_pause(self, state):
        self.client.sendall(f'{state}\n'.encode())

    def next(self):
        self.client.sendall(f'next\n'.encode())

    def previous(self):
        self.client.sendall(f'previous\n'.encode())

    def get_status(self):
        response = self._send_command('status')
        return self._parse_response(response)

    def get_track_info(self):
        response = self._send_command('currentsong')
        return self._parse_response(response)

    def _send_command(self, command):
        self.client.sendall(f'{command}\n'.encode())
        return self._read_response()

    def _read_response(self):
        response = b''

        while True:
            data = self.client.recv(4096)
            response += data

            if b'\nOK\n' in response:
                break

        return response.decode()

    def _parse_response(self, response):
        data = {}
        for line in response.splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                data[key] = value.strip()

        return data