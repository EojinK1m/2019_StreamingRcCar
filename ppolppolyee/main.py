from motor import motor_RGB
from rev_commu import receiver
from Video_Stream import videostream


IP = "0.0.0.0"

videostream.VideoStreamingStart()

motor_RGB.setupMotor()
control_receiver = receiver.ControlReceiver(IP)


while True:
    control_data= control_receiver.getData()
    motor_RGB.runMotor(control_data)



