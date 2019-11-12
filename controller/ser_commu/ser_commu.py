import serial

ser = serial.Serial('/dev/ttyACM0',9600)

def serial_communicating():
    data = {'X': 1 , 'Y' : 1, 'Z' : 1}
    while 1 :
        for i in range(0,3):
            data[chr(88+i)]= ser.readline()
            print(data[chr(88+i)])
if _name_ == '_main_':
    serial_communicating()