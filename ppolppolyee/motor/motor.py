import wiringpi

xpos = 800
ypos = 800

state = 1

STOP = 0
FORWARD = 1
BACKWARD = 2

CH1 = 0 
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0

ENA = 25
ENB = 30

IN1 = 24
IN2 = 23
IN3 = 22
IN4 = 21

def setPinConfig(EN, INA , INB):
    wiringpi.pinMode(EN, OUTPUT)
    wiringpi.pinMode(INA, OUTPUT)
    wiringpi.pinMode(INB, OUTPUT)
    wiringpi.softPwmCreate(EN, 0, 255)
def setMotorContorl(PWM, INA, INB, speed, stat):
    wiringpi.softPwmWrite(PWM, speed)

    if stat == FORWARD:
        wiringpi.digitalWrite(INA, HIGH)
        wiringpi.digitalWrite(INB , LOW)
    elif stat == BACKWARD:
        wiringpi.digitalWrite(INA, LOW)
        wiringpi.digitalWrite(INB, HIGH)
    elif stat == STOP:
        wiringpi.digitalWrite(INA, LOW)
        wiringpi.digitalWrite(INB, LOW)
def setMotor(chh, speed, stat):
    if ch == CH1:
        setMotorControl(ENA, IN1, IN2, speed, stat)
    else:
        setMotorControl(ENB, IN3, IN4, speed, stat)

wiringpi.wiringPiSetup()
speed1 = 150
speed2 = 150

setPinConfig(ENA, IN1, IN2)
setPinConfig(ENB, IN3, IN4)

while True:
    setMotor(CH1, speed1, FORWARD)
    setMotor(CH2, speed1, FORWARD)


    if xpos < 600 and xpos > 500 and ypos < 600 and ypos > 500:
        setMotor(CH1, speed1, STOP)
        setMotor(CH1, speed1, STOP)

    if ypos > 700:
        if xpos < 400:
            speed1 = int(speed1 + (-100 + xpos /20))
            setMotor(CH1, speed1, FORWARD)
            setMotor(CH1, speed2, FORWARD)
    else:
        speed1 = int(speed1 + xpos /20)
        setMotor(CH1, speed1, FORWARD)
        setMotor(CH2, speed2, FORWARD)
    if ypos < 400:
        if xpos < 400:
            speed1 = int(speed1 + (-100 + xpos /20))
            setMotor(CH1, speed1, BACKWARD)
            setMotor(CH1, speed2, BACKWARD)
    else:
        speed1 = int(speed1 + xpos /20)
        setMotor(CH1, speed1, BACKWARD)
        setMotor(CH2, speed2, BACKWARD)



