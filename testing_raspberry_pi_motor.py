import RPi.GPIO as GPIO

PIN_RIGHT_BOTTOM_GND = 5
PIN_RIGHT_BOTTOM_5VE = 6
PIN_LEFT_BOTTOM_GND = 12
PIN_LEFT_BOTTOM_5VE = 25
PIN_LEFT_TOP_GND = 23
PIN_LEFT_TOP_5VE = 24
PIN_RIGHT_TOP_GND = 27
PIN_RIGHT_TOP_5VE = 22
PWM_VALUE = 20

PWM_RIGHT_BOTTOM_GND = None
PWM_RIGHT_BOTTOM_5VE = None
PWM_LEFT_BOTTOM_GND = None
PWM_LEFT_BOTTOM_5VE = None
PWM_LEFT_TOP_GND = None
PWM_LEFT_TOP_5VE = None
PWM_RIGHT_TOP_GND = None
PWM_RIGHT_TOP_5VE = None

def init_rpi():
    """initialize raspberry pi pins
    mode : BCM"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_RIGHT_BOTTOM_GND, GPIO.OUT)
    GPIO.setup(PIN_RIGHT_BOTTOM_5VE, GPIO.OUT)
    GPIO.setup(PIN_LEFT_BOTTOM_GND, GPIO.OUT)
    GPIO.setup(PIN_LEFT_BOTTOM_5VE, GPIO.OUT)
    GPIO.setup(PIN_LEFT_TOP_GND, GPIO.OUT)
    GPIO.setup(PIN_LEFT_TOP_5VE, GPIO.OUT)
    GPIO.setup(PIN_RIGHT_TOP_GND, GPIO.OUT)
    GPIO.setup(PIN_RIGHT_TOP_5VE, GPIO.OUT)
    global PWM_RIGHT_BOTTOM_GND
    global PWM_RIGHT_BOTTOM_5VE
    global PWM_LEFT_BOTTOM_GND
    global PWM_LEFT_BOTTOM_5VE
    global PWM_LEFT_TOP_GND
    global PWM_LEFT_TOP_5VE
    global PWM_RIGHT_TOP_GND
    global PWM_RIGHT_TOP_5VE


    PWM_RIGHT_BOTTOM_GND = GPIO.PWM(PIN_RIGHT_BOTTOM_GND,  PWM_VALUE)
    PWM_RIGHT_BOTTOM_5VE = GPIO.PWM(PIN_RIGHT_BOTTOM_5VE,  PWM_VALUE)
    PWM_LEFT_BOTTOM_GND = GPIO.PWM(PIN_LEFT_BOTTOM_GND, PWM_VALUE)
    PWM_LEFT_BOTTOM_5VE = GPIO.PWM(PIN_LEFT_BOTTOM_5VE, PWM_VALUE)
    PWM_LEFT_TOP_GND =    GPIO.PWM(PIN_LEFT_TOP_GND, PWM_VALUE)
    PWM_LEFT_TOP_5VE =    GPIO.PWM(PIN_LEFT_TOP_5VE, PWM_VALUE)
    PWM_RIGHT_TOP_GND =   GPIO.PWM(PIN_RIGHT_TOP_GND, PWM_VALUE)
    PWM_RIGHT_TOP_5VE =   GPIO.PWM(PIN_RIGHT_TOP_5VE, PWM_VALUE)

def forword():
    """Move raspberry pi bot forward"""
    PWM_RIGHT_TOP_5VE.start(PWM_VALUE)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(PWM_VALUE)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(PWM_VALUE)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(PWM_VALUE)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)

def stop():
    """Stop raspberry pi"""
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.LOW)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.LOW)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.LOW)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.LOW)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_TOP_5VE.stop()
    PWM_RIGHT_TOP_GND.stop()
    PWM_LEFT_TOP_5VE.stop()
    PWM_LEFT_TOP_GND.stop()
    PWM_LEFT_BOTTOM_5VE.stop()
    PWM_LEFT_BOTTOM_GND.stop()
    PWM_RIGHT_BOTTOM_5VE.stop()
    PWM_RIGHT_BOTTOM_GND.stop()
    
def reverse():
    """Move raspberry pi bot reverse"""
    PWM_RIGHT_TOP_5VE.stop()
    PWM_RIGHT_TOP_GND.start(PWM_VALUE)
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.LOW)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.HIGH)
    
    PWM_LEFT_TOP_5VE.stop()
    PWM_LEFT_TOP_GND.start(PWM_VALUE)
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.LOW)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.HIGH)
    
    PWM_LEFT_BOTTOM_5VE.stop()
    PWM_LEFT_BOTTOM_GND.start(PWM_VALUE)
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.LOW)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.HIGH)
    
    PWM_RIGHT_BOTTOM_5VE.stop()
    PWM_RIGHT_BOTTOM_GND.start(PWM_VALUE)
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.LOW)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.HIGH)
    
def right():
    """Move raspberry pi bot to right"""
    PWM_RIGHT_TOP_5VE.start(5)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(50)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(5)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(50)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)  
      
def left():
    """Move raspberry pi bot to left"""
    PWM_RIGHT_TOP_5VE.start(50)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(5)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(50)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(5)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)

if __name__=="__main__":
    init_rpi()
    stop()
    try:
        while True:
            print('8. forword')
            print('2. reverse')
            print('4. left')
            print('6. right')
            print('5. stop')
            inpu = int(input('please press'))
            if inpu==1:
                forword()
            elif inpu==2:
                reverse()
            elif inpu==6:
                right()
            elif inpu==4:
                left()
            else:
                stop()
    except KeyboardInterrupt:
        stop()
        print('exit')
        GPIO.cleanup()
