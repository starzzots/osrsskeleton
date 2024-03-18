import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\skeletoncode')
import cv2 as cv
import numpy as np

from tools.windowcapture import WindowCapture
from tools.vision import Vision
from tools.clicks import *
from time import time, sleep
from datetime import datetime


# initialize the WindowCapture class
wincap = WindowCapture('RuneLite')
rockobs = Vision('images\\rock3.jpg')
miningspot=Vision('images\\miningicon.jpg')
topladder=Vision('images\\topladder.jpg')
hopper=Vision('images\\deposit.jpg')
bottomladder=Vision('images\\bottomladder.jpg')
bottomladder2=Vision('images\\bottomladder2.jpg')
bankdeposit=Vision('images\\bank_deposit.jpg')
depositbutton=Vision('images\\depositbutton.jpg')
exitbutton=Vision('images\\exitbutton.jpg')
rock2 = Vision('images\\rockfromladder.jpg')


yellow=(255,255,0)

obstcale= True # if obstcale == true then start check for yellow down else check from left
upstairs=True #helps me figure out where i am in game
def player():
    #threshhold .78 when mining
    delta2=9# double this for 3842*2160
    delta3=677# double this for 3842*2160
    delta4=323# double this for 3842*2160

    x,y,w,h = wincap.window_rect[0]+delta2, wincap.window_rect[1],wincap.window_rect[2]-delta2, wincap.window_rect[3]-delta2

    #gets players x,y coord on screen
    w1,h1 = wincap.window_rect[2]-delta3-delta2, wincap.window_rect[3]-delta4-delta2

    #formats to cords for Randomize class
    #may need to double the offests where ints are shown for 3840*2160
    playerleft = (w1-20,h1)
    playerbottom =(w1,h1+8)
    playercenter=(w1,h1)
    playerright=(w1+8,h1)
    playerup=(w1,h1-6)
    return playerleft,playerbottom,playerright,playerup,playercenter


def createcoords(coords):
    #coords coming in must be a tuple (x,y)
    delta = 3
    new = (coords[0] - delta,coords[0] + delta, coords[1] - delta, coords[1] + delta)
    return new

def checkbag(inventory,ss):
    #get Vision of image with Vision class hand grab screenshot of item to find
    total = 0
    #get Vision of image with Vision class hand grab screenshot of item to find
    img=Vision(f'images\\{inventory}.jpg') #grabs from images dir in tools folder make sure to save jpg to images folder in tools to test
    #create rectangle box for items
    rectangles= img.find(ss,0.90)# you can go into the Visions.find() in visions.py and uncomment out the debug mode to see what pc sees
    total = len(rectangles)
    return total
def lastslot():
    #takes x,y tuple () the x and y find with the pixel finder tool and plug in the x y for ogj on screen you wanna get
    #may need to double the delta1 and 2 for 3840*2160
    delta1=334
    delta2=63
    location = wincap.coords[2]-delta1,wincap.coords[3]-delta2
    return location
def collector():
    #444,613
    #may need to double the delta1 and 2 for 3840*2160
    delta1=694
    delta2=110
    location=wincap.coords[2]-delta1,wincap.coords[3]-delta2
    return location
def collectorfromdeposit():
    #296,483
    #may need to double the delta1 and 2 for 3840*2160
    delta1=842
    delta2=240
    location=wincap.coords[2]-delta1,wincap.coords[3]-delta2
    return location

def time_passed(current_time, secs):
    return time() - current_time >= secs
i=0
j=0
count=0
bankcounts=0



#334,63 from bottom right when paneel open in osrs thats the click distance to get to last slot 
while True:
    ss = wincap.get_screenshot()
    #paydirt= Vision('images\paydirt.jpg')
    #miningspot=Vision('images\miningspot.jpg')
    loop_time = time()
    inventory=['paydirt','sapphire','emerald','ruby','diamond'] 
    # used for testing change to your {insert your name of ss taken}.jpg file name
    
    #print(lastslot())
    #pg.moveTo(wincap.coords[2],wincap.coords[3])
    #pg.moveTo(lastslot())
    lastslotcheck=pg.pixel(lastslot()[0],lastslot()[1])
    collectorclick=(collector()[0],collector()[0],collector()[1],collector()[1])
    #print(lastslotcheck)
    #-7 x for checkingleft while mining for color change
    left=player()[0]
    down=player()[1]
    right=player()[2]
    up=player()[3]
    center=player()[-1]
    
    leftcheck=pg.pixel(left[0],left[1])
    downcheck=pg.pixel(down[0],down[1])
    rightcheck=pg.pixel(right[0],right[1])
    upcheck=pg.pixel(up[0],up[1])
    centercheck=pg.pixel(center[0],center[1])
    #pg.moveTo(down)
    #pg.moveTo(left)
    #pg.moveTo(down)
    #pg.moveTo(right)
    #pg.moveTo(center)
    #print(centercheck)
    #print(wincap.coords)
    #Randomize((collectorfromdeposit()[0],collectorfromdeposit()[0],collectorfromdeposit()[1],collectorfromdeposit()[1])).move()
    #print(time_passed(loop_time,45))
    #print(loop_time)
    if count == 2:
        if downcheck == (0,0,2):
            keyboard.press_and_release('space')
            sleep(2)
            Randomize(collectorclick).randleft()#collector click
            sleep(8)
        elif downcheck == (0,0,5):
            print('click bank')
            try:
                bankdepositrect = bankdeposit.find(ss,0.50,debug_mode="rectangles")
                bankdepositpoints = wincap.get_screen_position(bankdepositrect[0])
                Randomize((bankdepositpoints[0],bankdepositpoints[0],bankdepositpoints[1],bankdepositpoints[1])).randleft()
                sleep(7)
            except:
                print('rr1')
        elif centercheck == (73,64,52):
            try:
                depositbuttonrect = depositbutton.find(ss, 0.50,debug_mode="rectangles")
                depositbuttonpoints = wincap.get_screen_position(depositbuttonrect[0])
                Randomize((depositbuttonpoints[0],depositbuttonpoints[0],depositbuttonpoints[1],depositbuttonpoints[1])).randleft()
                sleep(1.6)
                
                exitbuttonrect = exitbutton.find(ss, 0.50,debug_mode="rectangles")
                exitbuttonpoints = wincap.get_screen_position(exitbuttonrect[0])
                Randomize((exitbuttonpoints[0],exitbuttonpoints[0],exitbuttonpoints[1],exitbuttonpoints[1])).randleft()
                bankcounts+=1
                sleep(1.6)
            except:
                print("reee2") 
             
        elif downcheck == (0,0,6) and bankcounts !=  2:
            print('thinking')
            Randomize((collectorfromdeposit()[0],collectorfromdeposit()[0],collectorfromdeposit()[1],collectorfromdeposit()[1])).randleft()
            sleep(5)
        else:
            print('lastset maybe')
            bottomladder2rect = bottomladder2.find(ss,0.50,debug_mode="rectangles")
            bottomladder2points = wincap.get_screen_position(bottomladder2rect[0])
            Randomize((bottomladder2points[0],bottomladder2points[0],bottomladder2points[1],bottomladder2points[1])).randleft()
            bankcounts = 0
            count = 0

            print(bankcounts,  count)
            sleep(8)
    elif lastslotcheck == (62, 53, 41):
        #print('bag not full')
        if obstcale == True:
            
            if rightcheck == (0,0,3) and upstairs == False:
                print('switch to upstair after looking to see if obs there or not')
                try:
                    rock2rect = rock2.find(ss,0.50,debug_mode="rectangles")
                    rock2points = wincap.get_screen_position(rock2rect[0])
                    Randomize((rock2points[0]+5,rock2points[0]+5,rock2points[1]-10,rock2points[1]-10)).randleft()
                    upstairs = True
                    sleep(7.5)
                except:
            
                    obstcale = False
            elif rightcheck == (0,0,4) and upstairs == True:
                try:
                    miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
                    miningpoints= wincap.get_screen_position(miningrectangles[-1])
                    Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
                    upstairs=True
                    sleep(5)
                except:
                    print('oops7sdfsdfsdf')    
            elif downcheck == (0,0,2) and upstairs == False:
                try:
                    bottomladderrect = bottomladder.find(ss,0.50,debug_mode="rectangles")
                    bottomladderpoints = wincap.get_screen_position(bottomladderrect[0])
                    Randomize((bottomladderpoints[0],bottomladderpoints[0],bottomladderpoints[1],bottomladderpoints[1])).randleft()
                    sleep(8)
                except:
                    print('asdfaewaf')
        
            elif downcheck != yellow and upstairs == True:
                print('mining...')
                if datetime.now().second == 45:
                    try:
                        miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
                        miningpoints= wincap.get_screen_position(miningrectangles[-1])
                        Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
                        obstcale=True
                        upstairs=True
                        sleep(8)
                    except:
                        print('couldnt find mining spt after waiting 45 secs')

            else:
                print('looking for spot to mine')
                try:
                    miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
                    miningpoints= wincap.get_screen_position(miningrectangles[-1])
                    Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
                    upstairs=True
                    sleep(8)
                except:
                    print('oops5')
        else:
            if downcheck == (0,0,2) and upstairs == False:
                try:
                    bottomladderrect = bottomladder.find(ss,0.50,debug_mode="rectangles")
                    bottomladderpoints = wincap.get_screen_position(bottomladderrect[0])
                    Randomize((bottomladderpoints[0],bottomladderpoints[0],bottomladderpoints[1],bottomladderpoints[1])).randleft()
                    sleep(8)
                except:
                    print('wut do?')
            elif rightcheck == (0,0,3) and upstairs == False:
                print('switch to upstair after looking to see if obs there or not')
                try:
                    rockrect = rockobs.find(ss,0.50,debug_mode="rectangles")
                    rockpoints = wincap.get_screen_position(rockrect[0])
                    Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-10,rockpoints[1]-10)).randleft()
                    sleep(2)
                except:
                    #print('start check with left wait till ')
                    obstcale=True
                    miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
                    miningpoints= wincap.get_screen_position(miningrectangles[-1])
                    Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
                    sleep(8)
                upstairs = True
            
            if leftcheck != yellow:
                # check
                print('mining...')
                if datetime.now().second == 45:
                    try:
                        miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
                        miningpoints= wincap.get_screen_position(miningrectangles[-1])
                        Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
                        obstcale=True
                        upstairs=True
                        sleep(8)
                    except:
                        print('couldnt find mining spt after waiting 45 secs')
            else:
                obstcale=True
                print(obstcale)     
            
    else:
        #print('bag full')
        
        
        if upcheck == (0,0,7):
            
            try:
                topladderrect = topladder.find(ss,0.50,debug_mode="rectangles")
                topladderpoints = wincap.get_screen_position(topladderrect[0])
                Randomize((topladderpoints[0],topladderpoints[0],topladderpoints[1],topladderpoints[1])).randleft()
                sleep(8)
            except:
                print('oops3')
            
        elif downcheck == (0,0,1):
            count+=1
            upstairs = False
            try:
                hopperrect = hopper.find(ss,0.50,debug_mode="rectangles")
                hopperpoints = wincap.get_screen_position(hopperrect[0])
                Randomize((hopperpoints[0],hopperpoints[0],hopperpoints[1],hopperpoints[1])).randleft()
                sleep(8)

            except:
                print('oops4')
            print(f"deposits = {count}")
            
        try:
            rockrect = rockobs.find(ss,0.50,debug_mode="rectangles")
            rockpoints = wincap.get_screen_position(rockrect[0])
            Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-10,rockpoints[1]-10)).randleft()
            sleep(9)
        except:
            print('go go go')
            
            
            
            """try:
                hopperrect = hopper.find(ss,0.50,debug_mode="rectangles")
                hopperpoints = wincap.get_screen_position(hopperrect[0])
                Randomize((hopperpoints[0],hopperpoints[0],hopperpoints[1],hopperpoints[1])).randleft()
                sleep(8)
            except:
                print('oops3')
            break"""
#randomize clicks with randomize class made delta is for cropping the extra none visual boarders wincap grabs
#for 3842*2160 may need to double delta var at top
#if you just wanna one poition uncomment this below and comment the for loop out
#

"""#loops through rect list and gets points then moves mouse over each item for testing get teak logs out of bank to test
for i in range(len(testrectangles)):
    testpoints= wincap.get_screen_position(testrectangles[i])
    Randomize((testpoints[0]-delta,testpoints[0]+delta, testpoints[1]-delta,testpoints[1]+delta)).move()"""

"""
try:
    rockrect = rockobs.find(ss,0.50,debug_mode="rectangles")
    rockpoints = wincap.get_screen_position(rockrect[0])
    Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-10,rockpoints[1]-10)).randleft()
    sleep(2)
            
    miningrectangles= miningspot.find(ss,0.70,debug_mode="rectangles")
    miningpoints= wincap.get_screen_position(miningrectangles[-1])
    Randomize((miningpoints[0],miningpoints[0],miningpoints[1],miningpoints[1])).randleft()
except:
    print('oops')"""