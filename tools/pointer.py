import pyautogui as pg
import keyboard
import time
import sys
import os
from clicks import *

bag=Bag()
    
while True:
    if keyboard.is_pressed('1'):
        top_left=pg.position()
        time.sleep(1)
    elif keyboard.is_pressed('2'):
        bottom_right=pg.position()
        time.sleep(1)
    elif keyboard.is_pressed('3'):
        print(f"{top_left[0]},{top_left[1]}\n{bottom_right[0]},{bottom_right[1]}")
        time.sleep(1)
    elif keyboard.is_pressed('p'):
        try:
            print(f"Randomize(({top_left[0]},{bottom_right[0]},{top_left[1]},{bottom_right[1]})).randleft()")
        except:
            print("oof try to get coords first with '1' and '2'")
        time.sleep(1)
    elif keyboard.is_pressed('='):
        pg.displayMousePosition()
    elif keyboard.is_pressed('-'):
        os.system('cls')
    elif keyboard.is_pressed('b'):
        time.sleep(1)
        x=input('What bag slot do you wanna get click cords for? 1-28 \n')
        print(f"Randomize(({bag.slot[int(x)][0]-5},{bag.slot[int(x)][0]+5},{bag.slot[int(x)][1]-5},{bag.slot[int(x)][1]+5})).randleft()")

    elif keyboard.is_pressed('delete'):
        break

#120,0,139
#255,3,255