import serial

ser = serial.Serial('/dev/ttyACM0',9600)

def serial_communicating():
    datas = {'X': 1, 'Y' : 1, 'Btn' : 1}
    
    while True:
        for key in datas.keys():
            datas[key]= ser.readline()

        yield datas

if __name__ == '__main__':
    serial_communicating()