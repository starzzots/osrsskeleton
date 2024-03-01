from win32gui import FindWindow, GetWindowRect
import win32gui
import pyautogui as pg
from clicks import *


shop=(255,0,255)
glasscolor=(53,87,255)
flag=0
bag=Bag()

while True:
    if keyboard.is_pressed('q'):
        break
    if bag.bagcheck(glasscolor) == True: #checks at the begining of loop if there is any molten glass
        bag.crafting(glasscolor)
    elif pg.pixel(1184,505) == (134,20,20) and flag == 0: # checks to see if ive logged out if True flag 0 is for switching from clicking first fav world or second for randomness
        Randomize((454,522,490,511)).randleft()#world select in sign in
        time.sleep(2)
        Randomize((888,940,234,240)).randleft()#world 420 
        time.sleep(1.7)
        Randomize((780,856,329,339)).randleft()# clicks the try again
        time.sleep(1.7)
        Randomize((775,859,269,293)).randleft()#clicks the log in bottom 
        time.sleep(9)
        Randomize((765,869,336,372)).randleft()# logged into game continue screen click
        time.sleep(1.7)
        keyboard.press_and_release('x')
        time.sleep(1)
        Randomize((1520,1528,1013,1027)).randleft()# world hop button in bag
        time.sleep(2)
        Randomize((1485,1505,971,981)).randleft()# click first favorite world slot
        time.sleep(9)
        keyboard.press_and_release('x')
        time.sleep(1)
        flag = 1
    elif pg.pixel(1184,505) == (134,20,20) and flag == 1:
        Randomize((454,522,490,511)).randleft()#world select in sign in
        time.sleep(2)
        Randomize((888,940,234,240)).randleft()#world 420 
        time.sleep(1.7)
        Randomize((780,856,329,339)).randleft()# clicks the try again
        time.sleep(1.7)
        Randomize((775,859,269,293)).randleft()#clicks the log in bottom 
        time.sleep(9)
        Randomize((765,869,336,372)).randleft()# logged into game continue screen click
        time.sleep(1.7)
        keyboard.press_and_release('x')
        time.sleep(1)
        Randomize((1520,1528,1013,1027)).randleft()# world hop button in bag
        time.sleep(2)
        Randomize((1485,1505,989,993)).randleft()# click seccond favorite world slot
        time.sleep(9)
        keyboard.press_and_release('x')
        time.sleep(1)
        flag = 0
    else:
        try:
            loc=findobj(shop)# looks for shop color and returns its x and y
            Randomize((loc[0]+2,loc[0]+3,loc[1]+8,loc[1]+8)).randleft()#randomly click the shopkeeper
            time.sleep(2)# sleep is for if click misses it can try again
        except:
            'oops couldnt find color'
        if pg.pixel(897,553) == (70,61,50):# color check of shop panel
            pg.leftClick(bag.bag[2], duration=.3) #sells crafted item to store
            time.sleep(.8)
            Randomize((713,721,443,445)).randleft()#clicks sand
            time.sleep(.8)
            Randomize((760,768,445,455)).randleft()#clicks seawead
            time.sleep(.8)
            Randomize((918,930,314,322)).randleft()#clicks exit button
            time.sleep(.8)
            keyboard.press_and_release('v')# hotkey for switch to mage book
            time.sleep(.8)
            Randomize((1521,1529,849,863)).randleft()# clicks glassmake filters for mage book need to be on to only show home tele and glassmake
            time.sleep(1.8)
            keyboard.press_and_release('x')#hotkey for bag switcj