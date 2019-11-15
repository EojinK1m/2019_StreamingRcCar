from ser_commu import receiver
from tcp_commu import sender


controll_data_stream = receiver.serial_communicater()
data_sender = sender.ControlDataSender()

data_sender.WaitConnection()
print('good!')

while True:
    data_sender.SendControlData(next(controll_data_stream))
