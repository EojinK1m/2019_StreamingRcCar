import wiringpi
import neopixel
import board


pixels = neopixel.NeoPixel(board.D18, 30)

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

B_1 = False
B_2 = False
L = False

speed1 = 150
speed2 = 150


def RGB(B_1):
    global B_2
    if B_2 == False and B_1 == True:
        L = not L
    B_2 = B_1
    return L

def light(B):
    pixels.fill = (100 * B, 100 * B, 100 * B)

def setPinConfig(EN, INA , INB):
    wiringpi.pinMode(EN, OUTPUT)
    wiringpi.pinMode(INA, OUTPUT)
    wiringpi.pinMode(INB, OUTPUT)
    wiringpi.softPwmCreate(EN, 0, 255)


def setMotorControl(PWM, INA, INB, speed, stat):
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

def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorControl(ENA, IN1, IN2, speed, stat)
    else:
        setMotorControl(ENB, IN3, IN4, speed, stat)






#this function call only one in main
def setupMotor():
    global speed1
    global speed2
    wiringpi.wiringPiSetup()
    speed1 = 150
    speed2 = 150

    setPinConfig(ENA, IN1, IN2)
    setPinConfig(ENB, IN3, IN4)


def runMotor(control_data):
    if control_data == None:
        return

    global FORWARD
    global BACKWARD
    global STOP

    global CH1
    global CH2
    
    global speed1
    global speed2

    xpos = control_data['X']
    ypos = control_data['Y']

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



