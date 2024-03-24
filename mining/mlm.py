import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\skeletoncode')
import cv2 as cv
import numpy as np

from tools.windowcapture import WindowCapture
from tools.vision import Vision
from tools.clicks import *
from time import time, sleep



# initialize the WindowCapture class
wincap = WindowCapture('RuneLite')




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

def findobjat(objsRGBVal,coords=(0,0,1080,670),stepleftright=1,stepupdown=1,delta1x=0,delta2y=0,delta3x=0,delta4y=0):#topleftx, toplefty, bottomrightx, bottomrighty
    flag=0
    wincap = WindowCapture('RuneLite')
    screenshot=pg.screenshot(region=(wincap.coords[0],wincap.coords[1],coords[2],coords[3]))

    
    for y in range(coords[1], coords[3], stepupdown):#1,3
        for x in range(coords[0], coords[2], stepleftright):#0,2
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return (new_x+delta1x,new_x+delta2y,new_y+delta3x,new_y+delta4y) #new_x,new_y imma reformate for us
                    
            





class Locate():
    def __init__(self, deltax, deltay,x1=0,x2=0,y1=0,y2=0):
        self.deltax=deltax
        self.deltay=deltay
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        self.locationc = wincap.coords[0]+self.deltax,wincap.coords[1]+self.deltay
    def item(self):
        location = (self.locationc[0]+self.x1,self.locationc[0]+self.x2,self.locationc[1]+self.y1,self.locationc[1]+self.y2)
        return location




def miningcheck(timer=45,miningcheck='miningcolorcheck',a='lastslotcheck',b=0):# color check and speed limit
    yellow=(255,255,0)
    flag=0
    lastslotcheck=a#pg.pixel(lastslot[0],lastslot[-1])

    
    print(f'{lastslotcheck}')

    if miningcheck == yellow:
        flag=1
    
    elif lastslotcheck != (62,53,41):
        flag=2
        
    else:
        if b >= timer:
            flag=3#need to pass if 3
        else:
            flag=4# sleeping till 3 will add one to counter when flag 4
    return flag 





test=(114,16,160)
miningchecklocation=(74,84,553,609)
rockobslocation=(227,178,532,517)
gameplaylocation=(29,71,561,618)
banklocation=(498,195,661,328)
failchecklocation=(28,445,562,643)

baglocation=(558,326,804,665)
chatlocation=(3,502,525,664)
aroundplayerlocation=(292,235,557,486)

pos1=(0,0,1)
pos2=(0,0,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,6)
pos6=(0,0,7)
pos7=(0,0,8)
pos8=(0,0,9)


hopperc=(24,44,125)
yellow = (255,255,0)
red = (255,0,0)
topladderc=(144,255,0)
bottomladderc=(63,0,79)
bagslotcolor = (62,53,41)
miningrockcolor = (0,241,255)
bankcheckc = (73,64,52)#(300,368)(73,64,52)
bankc = (255,115,0)


count=0
sleepcount=0
logcounter=10  
bankcount=0


while True:
    
    ss = wincap.get_screenshot()
    
    lastslot=Locate(745,608).item()
    ladderclick1=Locate(510,321).item()

    mining1checkl=Locate(386,342).item()
    mining2checkl=Locate(386,347).item()
    mining3checkl=Locate(404,361).item()
    

    mining1checkc=pg.pixel(mining1checkl[0],mining1checkl[-1])
    mining2checkc=pg.pixel(mining2checkl[0],mining2checkl[-1])
    mining3checkc=pg.pixel(mining3checkl[0],mining3checkl[-1])
    lastslotcheck=pg.pixel(lastslot[0],lastslot[-1])
    #print(lastslotcheck)


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
    
    bankcheck=Locate(300,368).item()

    
    collectorhardcode=Locate(383,561).item()
    collectorfrombank=Locate(239,429).item()

    depositbutton=Locate(355,373).item()
    exitbuttion=Locate(485,143).item()
    topladder=Locate(292,237).item()
    
    miningspot4=Locate(521,634).item()
    miningspot3=Locate(401,361).item()
    miningspot1=Locate(419,513).item()

    bankcheckstatement=pg.pixel(bankcheck[0],bankcheck[-1])

    topladder2=findobjat(topladderc,gameplaylocation,delta3x=8,delta4y=8)
    rockobj=findobjat(red,gameplaylocation,delta3x=8,delta4y=8)
    miningspot42=findobjat(miningrockcolor,miningchecklocation,stepupdown=4,delta1x=0,delta2y=0,delta3x=5,delta4y=5)
    miningspot2=findobjat(miningrockcolor,failchecklocation,delta1x=8,delta2y=8,delta3x=8,delta4y=8)
    hopper=findobjat(hopperc, gameplaylocation,delta1x=5,delta2y=5,delta3x=7,delta4y=7)
    bottomladder=findobjat(bottomladderc,gameplaylocation,delta1x=8,delta2y=8,delta3x=8,delta4y=8)
    bank=findobjat(bankc,banklocation,delta1x=-2,delta2y=-2,delta3x=8,delta4y=8)
    #print(wincap.coords)
    #Randomize(miningspot3).move()
    #print(lastslotcheck)
    
 
    
    #print(collector1)
    

    #print(upcheck)
    #print(lastslotcheck)
    #print(wincap.coords)
    #Randomize(lastslot).move()
    #teststuff=findobjat(red,gameplaylocation,stepupdown=5)
    #Randomize((teststuff[0]+5,teststuff[0]+5,teststuff[1]+5,teststuff[1]+5)).move()
    if upcheck == pos1:
        print('1')
        if logcounter >= 30:
            keyboard.press('pageup')# hotkey to switch worlds
            sleep(5)
            keyboard.release('pageup')# release the key presss
            sleep(7.5)
            keyboard.press('x')# bag hotkey ppress
            sleep(1)
            keyboard.release('x')#bag hotkey release
            sleep(2.5)
            logcounter = 0
            print(f'logcounter= {logcounter}, depositcount= {count}')
        Randomize(hopper).randleft()
        count+=1
        print(f'logcounter= {logcounter}, depositcount= {count}')
        sleep(6)
    
    elif upcheck == pos2:
        print('2')
        keyboard.press_and_release('space')
        if lastslotcheck != bagslotcolor:
            keyboard.press_and_release('space')
            sleep(.75)
            Randomize(hopper).randleft()
            sleep(1)
        elif lastslotcheck == bagslotcolor and count >= 3:
            keyboard.press_and_release('space')
            sleep(.75)
            Randomize(collectorhardcode).randleft()
            count = 0
            sleep(7)
        elif count <= 3:
            keyboard.press_and_release('space')
            sleep(.75)
            Randomize(ladderclick1).randleft()
            sleep(8)
        #Randomize(bottomladder).randleft()
        #sleep(10)
                
    elif upcheck == pos3:
        print('3')
        Randomize(bank).randleft()
        sleep(7)
    
    elif upcheck == pos4:
        #print('4')
        if bankcount >= 3:
            #print(f'{bankcount} go to ladder')
            bankcount=0
            Randomize(bottomladder).randleft()
            sleep(7)
        else:
            print(f'{bankcount}')
            Randomize(collectorfrombank).randleft()
            sleep(6)
        
    elif upcheck == pos5:
        #print('5')
        try:
            Randomize(rockobj).randleft()
            sleep(9)
            Randomize(miningspot1).randleft()
            sleep(7)
            
        except:
            Randomize(miningspot4).randleft()
            sleep(11)
            
    
    elif upcheck == pos6:
        #print('6 mining')
        x=miningcheck(timer=45,miningcheck=mining1checkc,a=lastslotcheck,b=sleepcount)
        new=x
        print(f'done1. new={new}')
        if new == 2:#bag full
            try:
                Randomize(rockobj).randleft()
                sleep(8)
                Randomize(topladder).randleft()
                logcounter+=1
                sleepcount=0
                sleep(11)
            except:
                Randomize(topladder2).randleft()
                logcounter+=1
                sleepcount=0
                sleep(14)
        elif new == 1:# mining spot == yellow
            Randomize(miningspot42).randleft()
            sleepcount=0
            sleep(2)
        elif new == 3:
            Randomize(miningspot42).randleft()
            sleepcount=0
            sleep(2)
        elif new == 4:
            sleepcount+=1
            print(sleepcount)
            sleep(1)
        pass
            
    

    elif bankcheckstatement == bankcheckc:
        #print('bag')
        Randomize(depositbutton).randleft()
        sleep(.6)
        Randomize(exitbuttion).randleft()
        sleep(.6)
        bankcount+=1
        
    #print('')
    pass