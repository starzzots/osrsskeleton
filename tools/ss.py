from windowcapture import WindowCapture
from time import time
import cv2 as cv

# initialize the WindowCapture class
wincap = WindowCapture('RuneLite')
#paydirt= Vision('images\paydirt.jpg')
#miningspot=Vision('images\miningspot.jpg')
num =0
loop_time = time()
while(True):
    # get an updated image of the game
    if num <= 500:
        screenshot = wincap.get_screenshot(num)
        cv.imshow('Computer Vision', screenshot)
        # do object detection
        #points = paydirt.find(screenshot, 0.5, 'rectangles')
        #Randomize(points[0]).move()
        num+=1
        #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        cv.waitKey(100)
    else:
        break
print('Done.')