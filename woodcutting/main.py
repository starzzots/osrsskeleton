import sys
sys.path.insert(0,'c:\\Users\\Kyle\\Documents\\skeletoncode')
from tools.windowcapture import WindowCapture
from tools.clicks import *
from time import time, sleep
from tools.tools import *



woodcutting=locate(68,59)
woodcuttingcolor=(0,255,0)
white=(255,255,255)
purple=(114,16,160)
tree_color=(255,115,0)
num=2
logout=20

def alching():
    num=2
    for _ in range(25):
        Randomize(bagslot["alch"]).randleft()
        sleep(1.2)
        Randomize(bagslotclicks[num]).randleft()
        sleep(1.2)
        num+=1

def findtree():
    try:
        tree=findobjat(tree_color,delta1x=15,delta2x=30,delta1y=15,delta2y=30)
        print(tree)
        Randomize(tree).randleft()
    except:
        print('no trees')

def fletching():
    num=2
    
    for i in range(25):
        sleep(2)
        if pg.pixel(bagslot[num][0],bagslot[num][-1]) != white:
            num+=1
        else:
            return num
    num=2
    return num

def worldhopper():
    keyboard.press('pageup')# hotkey to switch worlds
    sleep(5)
    keyboard.release('pageup')# release the key presss
    sleep(7.5)
    keyboard.press('x')# bag hotkey ppress
    sleep(1)
    keyboard.release('x')#bag hotkey release
    sleep(2.5)
    return 0

def main():
    bagcheck=pg.pixel(bagslot[26][0],bagslot[26][-1])
    woodcuttingcheck=pg.pixel(woodcutting[0],woodcutting[-1])
    #print(bagcheck)
    if woodcuttingcheck == woodcuttingcolor:
        sleep(1)
        return 0

    elif bagcheck == white:
        print('bag is full start fletching...')
        Randomize(bagslot[1]).randleft()
        sleep(1)
        Randomize(bagslot[num]).randleft()
        sleep(1)
        keyboard.press_and_release("space")
        sleep(1)
        num=fletching()
        sleep(1)
        return 0
        
    elif bagcheck == purple:
        print('start alching...')
        Randomize(bagslot["magebook"]).randleft()
        sleep(1)
        alching()
        num = 2
        Randomize(bagslot["bagicon"]).randleft()
        return 1
    else:
        print('looking for tree')
        findtree()
        sleep(2)
        return 0



while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    
    elif logout >= 20:
        print("hopping worlds...")
        logout=worldhopper()
        logout=0
        print(logout)

    temp=main()
    
    logout = logout + temp

    

    
    
        