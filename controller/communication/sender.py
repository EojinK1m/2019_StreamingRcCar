from socket import *


class ControlDataSender:
    PORT = 14529

    def __init__(self):
        self.server_sock = socket(AF_INET, SOCK_STREAM)
        self.server_sock.bind(('localhost', self.PORT))
        self.server_sock.listen(1)

    def WaitConnection(self):
        self.connect_sock, self.cl_addr = self.server_sock.accept()

    def SendControlData(self, datas):
        send_data = f'{datas[x]}/{datas[y]}/{datas[led_on_off]}'
        self.connect_sock.send(send_data.encode('UTF-8'))

