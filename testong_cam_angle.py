import cv2
WM_VALUE = 10
pwm_speed = 1
last_pwm = 0
position='S'
arr = []

def test_movement_of_raspberry_pi_bot(img):
    """Test movement of raspberry pi camera
    This will help to get parameter for bot movement"""
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
    ret, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    h, w = gray.shape
    left_img=gray[int(h/2):,:int(w/2)]
    right_img=gray[int(h/2):,int(w/2):w]
    left_view, right_view = sum(sum(left_img))/len(left_img), sum(sum(right_img))/len(right_img)
    avg = left_view - right_view
    ssum = left_view + right_view
    limit = 50
    limit_darkness = 100
    limit_brightness = 400
    print('avg',avg, "sum: ", ssum, 'position=',position)
    if limit_darkness< ssum and ssum<limit_brightness:
        pwm_speed = ((abs(avg)-limit)//10)
        pwm_speed = 2 if pwm_speed<=2 else pwm_speed
        pwm_speed = 9 if pwm_speed>9 else pwm_speed
        if -1*limit <avg and avg< limit and position!='F':
            print('Stright')
            position = 'F'
            #forword()        
        elif avg>limit and position!='R' and last_pwm != pwm_speed:
            print('Right', pwm_speed)
            position = 'R'
            print(pwm_speed, right_view)
            last_pwm = pwm_speed
        elif avg < -1*limit and position!='L' and last_pwm != pwm_speed:
            print('Left')
            position = 'L'
            print(pwm_speed, left_view)
            #left(pwm_speed)
            last_pwm = pwm_speed
    elif position!='S':
        print('Stop')
        position = 'S'
        #stop()
    return avg, ssum, left_img, right_img
    
def start_bot():
    """start bot
    1. stat camera and get image
    2. process image and decide movement of bot"""
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    global position
    position = 'S'
    while True:
        _, image = video.read()
        avg, ssum, left_img,  right_img= test_movement_of_raspberry_pi_bot(image)
        cv2.imshow('real',image[int(240/2):,:,:])
        cv2.imshow('left',left_img)
        cv2.imshow('right',right_img)
        #print(avg, "sum= ", ssum)
        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
if __name__=="__main__":
    start_bot()
