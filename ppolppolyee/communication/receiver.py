import socket
import pickle

class ReceiverSocket:
    PORT = 14529
    BUFFER_SIZE = 512
    
    def __init__(self, ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, self.PORT))

    def receive(self):
        res = self.sock.recv(self.BUFFER_SIZE)
        if len(res) == 0:
            return None
        return pickle.loads(res)

class ControlReceiver:

    def __init__(self, ip):
        self.socket = ReceiverSocket(ip)
