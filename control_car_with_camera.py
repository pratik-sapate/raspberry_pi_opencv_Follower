import RPi.GPIO as GPIO
import time
import cv2
import threading
import sys
import test
import numpy as np

PIN_RIGHT_BOTTOM_GND = 5
PIN_RIGHT_BOTTOM_5VE = 6
PIN_LEFT_BOTTOM_GND = 12
PIN_LEFT_BOTTOM_5VE = 25
PIN_LEFT_TOP_GND = 23
PIN_LEFT_TOP_5VE = 24
PIN_RIGHT_TOP_GND = 27
PIN_RIGHT_TOP_5VE = 22

PWM_RIGHT_BOTTOM_GND = None
PWM_RIGHT_BOTTOM_5VE = None
PWM_LEFT_BOTTOM_GND = None
PWM_LEFT_BOTTOM_5VE = None
PWM_LEFT_TOP_GND = None
PWM_LEFT_TOP_5VE = None
PWM_RIGHT_TOP_GND = None
PWM_RIGHT_TOP_5VE = None
PWM_VALUE = 20

def roi(image):
    width, height= image.shape
    # triangle = np.array([(0, width), (0, int(3*width/4)), (int(height/2), int(width/2)), (height, int(3*width/4)), (height, width)])
    half = np.array([(0, width), (0, int(width / 2)), (height, int(width / 2)), (height, width)])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, np.int32([half]), (255, 0, 0), 255)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    return masked_image

def webcam_operation():
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        _, image = video.read()
        #ray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        #image = roi(thresh1)    
        # print(angle)
        cv2.imshow('Image', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
            
def init_rpi():
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
    PWM_RIGHT_TOP_5VE.start(1)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(PWM_VALUE*2)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(1)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(PWM_VALUE*2)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)  
      
def left():
    PWM_RIGHT_TOP_5VE.start(PWM_VALUE*2)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(1)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(PWM_VALUE*2)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(1)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)

if __name__=="__main__":
    cam_thread = threading.Thread(target=webcam_operation, )
    cam_thread.start()
    init_rpi()
    stop()

    while True:
        print('8. forword')
        print('2. reverse')
        print('4. left')
        print('6. right')
        print('5. stop')
        inpu = input('please press')
        if inpu==8:
            forword()
        elif inpu==2:
            reverse()
        elif inpu==6:
            right()
        elif inpu==4:
            left()
        else:
            print("wrong input", inpu)
            stop()
            cam_thread.join()
            print('exit')
            GPIO.cleanup()
            exit(1)
                
