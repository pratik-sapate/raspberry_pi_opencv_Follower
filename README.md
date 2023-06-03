# raspberry_pi_opencv_Follower

---

Lane follower botwe will need hardware follow as,<br> 
Raspberry pi 4b - https://robu.in/product/raspberry-pi-4-model-b-with-4-gb-ram/ <br>
DC-DC 4.5–40V To 5V 3A USB Charger Step down - https://robu.in/product/dc-dc-4-5-40v-5v-2a-usb-charger-step-converter-voltmeter-modul/<br>
4 motor bot chassis https://robu.in/product/longer-version-4-wd-double-layer-smart-car-chassis/<br>
2 X 2500mAh 3S 3C(11.1 v) Lithium Polymer Battery Pack - https://robu.in/product/orange-transmitter-tx-11-1v-2500mah-3s-3c-lipo-battery-pack-xt60-connector/<br>
Motor Drive Shield Expansion Board L293D - https://robu.in/product/mini-4-channel-motor-drive-shield-expansion-board-l293d-module-high-voltage-current-module-for-arduino-uno-mega-2560-mega2560/<br>
USB camera - https://robu.in/product/1-4-cmos-640x480-usb-camera-with-collapsible-cable-for-raspberry-pi-3/ ( you can we non usb camra also)<br>
Battery Charger - https://www.amazon.in/Lithium-Polymer-B3-Battery-Charger/dp/B08QGVH5LX/ref=asc_df_B08QGVH5LX/?tag=googleshopdes-21&linkCode=df0&hvadid=397082326460&hvpos=&hvnetw=g&hvrand=902828606805744270&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062111&hvtargid=pla-1359407778933&psc=1&ext_vrnc=hi<br>
2 X connectors https://robu.in/product/male-xt60-connectors-1pcs-genuine/<br>
Acrylic sheet – https://www.amazon.in/BIGMALL-Acrylic-Plexiglass-Opaque-Projects/dp/B074ZLMPQV/ref=asc_df_B074ZLMPQV/?tag=googleshopdes-21&linkCode=df0&hvadid=397006705630&hvpos=&hvnetw=g&hvrand=10422285636649685215&hvpone=&hvptwo=&hvqmt=&hvdev=t&hvdvcmdl=&hvlocint=&hvlocphy=9062111&hvtargid=pla-406070324831&psc=1&ext_vrnc=hi<br>
On/Off switch to operate battery<br>
Jumper wires mostly f to f<br>
USB to C-Type small cable to connect raspberry pi<br>
Screw driver for mounting components.
Black paper path (any black path)
build your bot with circuit diagram.
Circuit DiagramSteps:
1. Connect chassis motors with motor driving shield (l293d) and mount this shield on it.
2. Connect a switch to battery. This battery will use for chassis motor.
2. Connect a battery to both motor driving shield.
3. Connect step down usb to another battery.
This battery will use for raspberry pi. But raspberry pi needs 3 ampere 5 volt current and our step down USB gives output as 2 Ampere 5 volt, so we will get warning on raspberry pi screen. This warning will not affect project.

4. Mount raspberry pi, step down USB on chassis.
5. Connect step down USB and raspberry pi using c type cable
6. Cut Acrylic sheet such that a we can mount camera over it.( note camera should be downward(45 degrees). you can use gimbal but I don't want use.)
7. Mount camera and connect connect it with raspberry pi.
For initial setup of raspberry pi, Please follow steps.
[Eng][RPi] Remote Desktop Access to the Raspberry Pi via RDP with 5 platforms
medium.com

---

Now we are ready for coding.
Clone a code from,
https://github.com/pratik-sapate/raspberry_pi_opencv_Follower.git
For our project will need opencv.
Please follow https://robu.in/installing-opencv-using-cmake-in-raspberry-pi/
Form our code run testing_raspberry_pi_motors.py
Python testing_raspberry_pi_motors
Press
8 for forword
2 for reverse
4 for left.
6 for right

If raspberry is not moving as per direction interchange its connections.
Now we are ready to use bot on path.

---

Code Explanation:
Raspberry pi pin connection initialisation.
```python
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
  Raspberry pi pin Function initialisation:
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
      global position

      PWM_RIGHT_BOTTOM_GND = GPIO.PWM(PIN_RIGHT_BOTTOM_GND,  PWM_VALUE)
      PWM_RIGHT_BOTTOM_5VE = GPIO.PWM(PIN_RIGHT_BOTTOM_5VE,  PWM_VALUE)
      PWM_LEFT_BOTTOM_GND = GPIO.PWM(PIN_LEFT_BOTTOM_GND, PWM_VALUE)
      PWM_LEFT_BOTTOM_5VE = GPIO.PWM(PIN_LEFT_BOTTOM_5VE, PWM_VALUE)
      PWM_LEFT_TOP_GND =    GPIO.PWM(PIN_LEFT_TOP_GND, PWM_VALUE)
      PWM_LEFT_TOP_5VE =    GPIO.PWM(PIN_LEFT_TOP_5VE, PWM_VALUE)
      PWM_RIGHT_TOP_GND =   GPIO.PWM(PIN_RIGHT_TOP_GND, PWM_VALUE)
      PWM_RIGHT_TOP_5VE =   GPIO.PWM(PIN_RIGHT_TOP_5VE, PWM_VALUE)
  Code for raspberry pi bot movement.
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

  def right(pwm_speed):
      """Move raspberry pi bot to right"""
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
      """Move raspberry pi bot to left"""
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
```
After getting an image from camera, we will convert an image to grayscale. We know That our lane is black and floor is white. So I observed each pixel of grayscale image and give static value for image thresholding. But light is not constant for entire day. This logic will fails.
So Better way to find thresholding is create array window for 10 consequent images.
```python
	 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pixel_sum = sum(sum(gray))/len(gray)
    if len(arr)>=10:
        arr.append(pixel_sum)
        arr=arr[1:-1]
    else:
        arr.append(pixel_sum)
    pixel_sum = (sum(arr)//len(arr))-20
    ret, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
```
So now our approach is to read image, do some operation. And decide what to do, should we move to left, right or straight. If lane does not found then bot should stop.<br>
(I was trying with maxpooling. but skip in between, because following idea came in my mind.)<br>
after lot of observation I found that,  If left image contain maximum black pixel then bot should move left size. and for my case only bottom half is important to me.<br>
So I divide grabbed Image in two parts.<br>
calculate average value of left image and right image. also create new variable as avg, this avg value will store normalized value from left image and right value.<br>
with this solution I notice that if grabbed image having maximum black pixel at left side. then constant negative value is displaying. and for right side positive<br>
for left side avg will is showing 0 to -20<br>
for right side avg will is showing 0 to 20<br>
so for safer side will take limit as 35. <br>
we can say that ,<br>
for straight path avg value will between 35 to -35<br>
for left side path avg will show less than -35<br>
for right side path avg will show less than 35<br>
also will need find when our bot should stop. and it is not quite tricky. just find left image value and right image value. and use static value to detect. non lane region. as shown in code.<br>
```python
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
```
And Yes our bot is ready to run. I tried will multiple path. our bot detects angle and follow lane. 

but I have found limitation that it is not moving if there is turning with 90 degree. so we can change bot (front wheel movable) and logic will change slightly. will implement it next toutorials.
