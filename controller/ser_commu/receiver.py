import serial

ser = serial.Serial('/dev/ttyACM0',9600)

def serial_communicater():
    datas = {'X': 1, 'Y' : 1, 'Btn' : 1}
    
    while True:
        for key in datas.keys():
            temp = ser.readline()
          #  temp = temp[:-2]
            temp = temp.decode('UTF-8')
		
            datas[key] = int(temp)
       
        yield datas

if __name__ == '__main__':
    a = serial_communicater()
    while True:
        print(next(a))
