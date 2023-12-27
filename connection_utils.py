import socket


class SocketClient:

    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_address, self.server_port))

    def close(self):
        if self.socket:
            self.socket.close()

    def send_data(self, data):
        if not self.socket:
            raise ValueError("Socket not connected.")
        self.socket.sendall(bytes.fromhex(data))

    def receive_data(self, buffer_size=1024):
        if not self.socket:
            raise ValueError("Socket not connected. Call connect() first.")
        try:
            data = self.socket.recv(buffer_size)
            if not data:
                return None
            return data.decode('utf-8')
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None
