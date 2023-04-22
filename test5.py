import cv2
import numpy as np
import math
import RPi.GPIO as GPIO
import time
import threading
import sys, os
import test

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
PWM_VALUE = 10
pwm_speed = 1
last_pwm = 0
position='S'
arr = []

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
    global position

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
    
def right(pwm_speed):
    PWM_RIGHT_TOP_5VE.start(1)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(pwm_speed)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(1)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(pwm_speed)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)  
      
def left(pwm_speed):
    PWM_RIGHT_TOP_5VE.start(pwm_speed)
    PWM_RIGHT_TOP_GND.stop()
    GPIO.output(PIN_RIGHT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_TOP_GND, GPIO.LOW)

    PWM_LEFT_TOP_5VE.start(1)
    PWM_LEFT_TOP_GND.stop()
    GPIO.output(PIN_LEFT_TOP_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_TOP_GND, GPIO.LOW)
    
    PWM_LEFT_BOTTOM_5VE.start(pwm_speed)
    PWM_LEFT_BOTTOM_GND.stop()
    GPIO.output(PIN_LEFT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_LEFT_BOTTOM_GND, GPIO.LOW)

    PWM_RIGHT_BOTTOM_5VE.start(1)
    PWM_RIGHT_BOTTOM_GND.stop()
    GPIO.output(PIN_RIGHT_BOTTOM_5VE, GPIO.HIGH)
    GPIO.output(PIN_RIGHT_BOTTOM_GND, GPIO.LOW)

  
def get_two_side_view(img):
    global position
    global pwm_speed
    global last_pwm
    global arr
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pixel_sum = sum(sum(gray))/len(gray)
    if len(arr)>=10:
        arr.append(pixel_sum)
        arr=arr[1:-1]
    else:
        arr.append(pixel_sum)
    pixel_sum = (sum(arr)//len(arr))-20
    ret, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    h, w = gray.shape
    bottom_half = gray[int(h/2):,:]
    left_img=bottom_half[:,:int(w/2)]
    right_img=bottom_half[:,int(w/2):w]
    left_view, right_view = sum(left_img.ravel())/(left_img.shape[0]*left_img.shape[1]), sum(right_img.ravel())/(right_img.shape[0]*right_img.shape[1])
    avg = left_view - right_view
    limit = 35
    limit_darkness = 50
    limit_brightness = 170
    data={"avg": avg, "left_view": left_view, "right_view": right_view, "position":position}
    print(data)
    
    if ((limit_darkness> left_view and limit_darkness> right_view ) or (left_view>limit_brightness and right_view>limit_brightness)):
        position = 'S'
        stop()
    else:    
        pwm_speed = int(PWM_VALUE*(abs(avg)-limit)/8)
        pwm_speed = 11 if pwm_speed<=11 else pwm_speed
        pwm_speed = 99 if pwm_speed>99 else pwm_speed
        if -1*limit <avg and avg< limit and position!='F':
            print('Stright')
            position = 'F'
            forword()        
        elif avg>limit:
            position = 'R'
            print(pwm_speed, right_view)
            right(pwm_speed)
            last_pwm = pwm_speed
        elif avg < -1*limit:
            position = 'L'
            print(pwm_speed, left_view)
            left(pwm_speed)
            last_pwm = pwm_speed
        
    return data, bottom_half
    

def webcam_operation():
    global position
    init_rpi()
    stop()
    position = None
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    i = 1
    while True:
        _, image = video.read()
        data, bottom_half = get_two_side_view(image)
        cv2.imwrite('lane_images/'+str(i)+'_'+str(data)+'.jpg', bottom_half)
        cv2.imshow('bottom half', bottom_half)
        i+=1
        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
if __name__=="__main__":
    for file in os.listdir('lane_images/'):
        os.remove('lane_images/'+file)
    webcam_operation()

