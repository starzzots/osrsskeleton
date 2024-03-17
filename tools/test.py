import cv2 as cv
import numpy as np

from windowcapture import WindowCapture
from vision import Vision
from clicks import *
from time import time
"""
type settings in plugin on RuneLite to get to these settings
set runelite settings show display name in title off or uncheck the box
while there set game size to 800*640 and check the lock window size in settings
"""

# initialize the WindowCapture class
wincap = WindowCapture('RuneLite')

ss = wincap.get_screenshot()
#paydirt= Vision('images\paydirt.jpg')
#miningspot=Vision('images\miningspot.jpg')
loop_time = time()




#threshhold .78 when mining
delta = 3
delta2=9# double this for 3842*2160
delta3=677# double this for 3842*2160
delta4=323# double this for 3842*2160

x,y,w,h = wincap.window_rect[0]+delta2, wincap.window_rect[1],wincap.window_rect[2]-delta2, wincap.window_rect[3]-delta2

#gets players x,y coord on screen
w1,h1 = wincap.window_rect[2]-delta3-delta2, wincap.window_rect[3]-delta4-delta2

#formats to cords for Randomize class
player = (w1,w1,h1,h1)

test='teak' # used for testing change to your {insert your name of ss taken}.jpg file name

#get Vision of image with Vision class hand grab screenshot of item to find
testimg=Vision(f'images\\{test}.jpg') #grabs from images dir in tools folder make sure to save jpg to images folder in tools to test

#create rectangle box for items
testrectangles= testimg.find(ss,0.99,debug_mode="rectangles")# you can go into the Visions.find() in visions.py and uncomment out the debug mode to see what pc sees

#get points for items
testpoints= wincap.get_screen_position(testrectangles[0])


#randomize clicks with randomize class made delta is for cropping the extra none visual boarders wincap grabs
#for 3842*2160 may need to double delta var at top
#if you just wanna one poition uncomment this below and comment the for loop out
#Randomize((testpoints[0]-delta,testpoints[0]+delta, testpoints[1]-delta,testpoints[1]+delta)).move()

#loops through rect list and gets points then moves mouse over each item for testing get teak logs out of bank to test
for i in range(len(testrectangles)):
    testpoints= wincap.get_screen_position(testrectangles[i])
    Randomize((testpoints[0]-delta,testpoints[0]+delta, testpoints[1]-delta,testpoints[1]+delta)).move()



### will come back to this later got tired
"""for i in range(len(miningrectangles)):
    miningpoints=wincap.get_screen_position(miningrectangles[i])
    Randomize((miningpoints[0]-delta,miningpoints[0]+delta, miningpoints[1]-delta,miningpoints[1]+delta)).move()"""

"""while(True):
    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    cv.imshow('Computer Vision', screenshot)

    # do object detection
    #points = paydirt.find(screenshot, 0.5, 'rectangles')
    #Randomize(points[0]).move()
    
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')"""


"""paydirt= Vision('images\paydirt.jpg')
rectangles = paydirt.find(ss, 0.8, debug_mode="rectangles")
points=wincap.get_screen_position(rectangles[0])"""

""""miningspot=Vision('images\\rock.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\topladder.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\deposit.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\collect.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\ore.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\bank_deposit.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\bankscreen.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\depositbutton.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\exitbutton.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\collect.jpg')
miningrectangles= miningspot.find(ss,0.50,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\rockfromladder.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""

"""miningspot=Vision('images\\mininglocation.jpg')
miningrectangles= miningspot.find(ss,0.90,debug_mode="rectangles")
miningpoints= wincap.get_screen_position(miningrectangles[0])"""