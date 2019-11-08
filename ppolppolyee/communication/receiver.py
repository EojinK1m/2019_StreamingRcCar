import socket
import string

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
        return res.decode()


class ControlData():
    def __init__(self, led_on_off, xposition, yposition):
        self.led_on_off = led_on_off
        self.xposition = xposition
        self.yposition = yposition


class StringConverter():
    @staticmethod
    def to_control_data(datas):
        data = "adfs"
        #data.split('/')
        

# class ControlReceive():

#     def __init__(self):
