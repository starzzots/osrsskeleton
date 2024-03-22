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
rockobs = Vision('images\\rock.jpg')


pos1=(0,0,1)
pos2=(0,0,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,5)
pos6=(0,0,6)


yellow = (255,255,0)
red = (255,0,0)
bagslotcolor = (62,53,41)
miningrockcolor = (0,241,255)
bankcheckc = (73,64,52)

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
    playerup=(w1,h1-8)
    return playerleft,playerbottom,playerright,playerup,playercenter

def findobjat(objsRGBVal):
    flag=0
    wincap = WindowCapture('RuneLite')
    screenshot=pg.screenshot('test.png',region=(wincap.coords[0],wincap.coords[1],1080,670))
    objsRGBVal=miningrockcolor
    width, height = screenshot.size
    
    for y in range(0, 670, 2):
        for x in range(0, 1080, 2):
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return new_x,new_y
            

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

class Locate():
    def __init__(self, deltax, deltay):
        self.deltax=deltax
        self.deltay=deltay
        self.locationc = wincap.coords[2]-self.deltax,wincap.coords[3]-self.deltay
    def item(self):
        location = (self.locationc[0],self.locationc[0],self.locationc[1],self.locationc[1])
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

count=0
bankcounts=0
logcounter=0

"""while start == True:
    if datetime.now().second == 50:
        print('rock depleted')
    else:
        print('mining...')"""
        
#334,63 from bottom right when paneel open in osrs thats the click distance to get to last slot 
while True:
    
    ss = wincap.get_screenshot()
    #print(wincap.coords)

    #paydirt= Vision('images\paydirt.jpg')
    #miningspot=Vision('images\miningspot.jpg')
    loop_time = time()
    inventory=['paydirt','sapphire','emerald','ruby','diamond'] 
    # used for testing change to your {insert your name of ss taken}.jpg file name
    
    #print(lastslot())
    #pg.moveTo(wincap.coords[2],wincap.coords[3])
    #pg.moveTo(lastslot())
    lastslot=Locate(334,63).item()
    collector=Locate(694,110).item()
    hopper=Locate(795,325).item()
    bank=Locate(508,409).item()
    ladderfrombank=Locate(729,487).item()
    rockfromladdercheck=Locate(548,202).item()
    rock_in_my_way=Locate(557,206).item()
    miningspotfromladder=Locate(560,43).item()
    miningspotfromrock = Locate(661,159).item()
    fromrocktoladder = Locate(790,437).item()
    ladderfromhopper = Locate(571,348).item()
    depositbutton = Locate(727,307).item()
    exitbutton = Locate(592,526).item()
    ladderfrombank = Locate(730,489).item()
    collectorfrombank = Locate(842,241).item()
    #print(lastslotcheck)
    #-8 x for checkingleft while mining for color change
    left=player()[0]
    down=player()[1]
    right=player()[2]
    up=player()[3]
    center=player()[-1]
    checkrock=pg.pixel(rockfromladdercheck[0],rockfromladdercheck[-1])
    lastslotcheck=pg.pixel(lastslot[0],lastslot[-1])

    leftcheck=pg.pixel(left[0],left[1])
    downcheck=pg.pixel(down[0],down[1])
    rightcheck=pg.pixel(right[0],right[1])
    upcheck=pg.pixel(up[0],up[1])
    centercheck=pg.pixel(center[0],center[1])


    #print(wincap.coords)
    #print(upcheck)
    #Randomize((center[0],center[0],center[1],center[1])).move()
    
    
    #pg.moveTo(down)
    #pg.moveTo(left)
    #pg.moveTo(down)
    #pg.moveTo(right)
    #pg.moveTo(center)
    #print(lastslotcheck)
    #Randomize(lastslot).move()
    #print(wincap.coords)
    
    #Randomize((collectorfromdeposit()[0],collectorfromdeposit()[0],collectorfromdeposit()[1],collectorfromdeposit()[1])).move()
    #print(time_passed(loop_time,45))
    #print(loop_time)
    
    if upstairs == True:
        if lastslotcheck == bagslotcolor:
            if upcheck == pos6:
                if checkrock == red:
                    print('Gay ass bitch ass rock in my way go mine that gay boy')
                    Randomize(rock_in_my_way).randleft()
                    sleep(7)
                    Randomize(miningspotfromrock).randleft()
                    sleep(7)
                   
                else:
                    print('no rock in the way get to mining tubby')
                    Randomize(miningspotfromladder).randleft()
                    sleep(12)
                       
            elif upcheck == pos2:
                Randomize(ladderfromhopper).randleft()
                sleep(6)
            elif lastslotcheck != bagslotcolor:
                print('bag full')
                try:
                    rockrect = rockobs.find(ss,0.50,debug_mode="rectangles")
                    rockpoints = wincap.get_screen_position(rockrect[0])
                    Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-5,rockpoints[1]-5)).randleft()
                    sleep(9)
                except:
                    rockrect = rockobs.find(ss,0.40,debug_mode="rectangles")
                    rockpoints = wincap.get_screen_position(rockrect[0])
                    Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-5,rockpoints[1]-5)).randleft()
                    sleep(9)

            else:
                if datetime.now().second == 45:
                    try:
                        miningspot=findobjat(miningrockcolor)
                        Randomize((miningspot[0]+4,miningspot[0]+8,miningspot[1]+6,miningspot[1]+8)).randleft()
                        sleep(1)
                    except:
                        print('oops')
        else:
            print('bagfull')
            try:
                rockrect = rockobs.find(ss,0.50,debug_mode="rectangles")
                rockpoints = wincap.get_screen_position(rockrect[0])
                Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-5,rockpoints[1]-5)).randleft()
                sleep(9)
            except:
                rockrect = rockobs.find(ss,0.40,debug_mode="rectangles")
                rockpoints = wincap.get_screen_position(rockrect[0])
                Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-5,rockpoints[1]-5)).randleft()
                sleep(9)
            Randomize(fromrocktoladder).randleft()
            upstairs=False
            logcounter+=1
            count+=1
            sleep(10)
       
    elif upstairs == False:
        print('downstairs')
        if upcheck == pos1:
            if logcounter == 30:
                keyboard.press('pageup')# hotkey to switch worlds
                sleep(5)
                keyboard.release('pageup')# release the key presss
                sleep(7.5)
                keyboard.press('x')# bag hotkey ppress
                sleep(1)
                keyboard.release('x')#bag hotkey release
                sleep(2.5)
            elif count != 2:
                upstairs = True
                Randomize(hopper).randleft()
                sleep(4)
                keyboard.press_and_release('space')
            else:
                upstairs = False
                Randomize(hopper).randleft()
                sleep(4)
                keyboard.press_and_release('space')
        
        elif upcheck == pos2:
            if count != 2:
                upstairs = True
                Randomize(ladderfromhopper).randleft()
                sleep(8)
                
            keyboard.press_and_release('space')
            Randomize(collector).randleft()
            count = 0
            sleep(6)
            
        elif upcheck == pos3:
            Randomize(bank).randleft()
            sleep(7.5)
        elif centercheck == bankcheckc:
        
            Randomize(depositbutton).randleft()
            sleep(1.6)
            Randomize(exitbutton).randleft()
            sleep(1.6)
            bankcounts+=1
        elif upcheck == pos4: 
            if bankcounts != 2:
                Randomize(collectorfrombank).randleft()
                sleep(4)
            else:
                Randomize(ladderfrombank).randleft()
                bankcounts = 0
                sleep(8)
                upstairs = True
                
        else:
            print('oops')
            
    else:
        print('I dont know what to do')
        break
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
    print('oops')
    
    
    
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
            logcounter+=1
            

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
        
            elif downcheck != yellow and upstairs == True and logcounter != 15:
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
            elif downcheck != yellow and upstairs == True and logcounter == 15:
                
                keyboard.press('pageup')# hotkey to switch worlds
                sleep(5)
                keyboard.release('pageup')# release the key presss
                sleep(7.5)
                keyboard.press('x')# bag hotkey ppress
                sleep(1)
                keyboard.release('x')#bag hotkey release
                logcounter = 0
                sleep(2.5)
                
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
            
            rockrect = rockobs.find(ss,0.40,debug_mode="rectangles")
            rockpoints = wincap.get_screen_position(rockrect[0])
            Randomize((rockpoints[0]+5,rockpoints[0]+5,rockpoints[1]-10,rockpoints[1]-10)).randleft()
            sleep(9)    
    
    
    
    """