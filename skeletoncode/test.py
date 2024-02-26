from win32gui import FindWindow, GetWindowRect
import win32gui
import pyautogui as pg
from clicks import *

#zoom set to 100 limit game client layout fixed classic layout
black=(0,3,0)
hwnd = win32gui.FindWindow(None, 'RuneLite')
top_left = win32gui.GetWindowRect(hwnd)

#set runelite to 760 x 500
bottom_right=(772,510)
screen=(top_left[0]+10, top_left[1]+25,bottom_right[0], bottom_right[1]) 
cords=(top_left[0]+10, top_left[1]+25,top_left[0]+760, top_left[1]+500)
#game play screen coords
game_bottom_right=(520,345)
gameplay=(top_left[0]+10, top_left[1]+25,game_bottom_right[0], game_bottom_right[1])
#pg.screenshot('gameplay.png', gameplay) 

#chat box
chat_bottom_right=(523,527)
chatbox=(top_left[0]+10,top_left[1]+370,chat_bottom_right[0],chat_bottom_right[1]-370)
#pg.screenshot('chatbox.png', chatbox)

#map area
map_bottom_right=(768,197)
mapbox=(top_left[0]+532,top_left[1]+30,map_bottom_right[0]-532,map_bottom_right[1]-30)
#pg.screenshot('mapbox.png', mapbox)

#inventory area
inventory_bottom_right=(769,531)
inventory=(top_left[0]+538,top_left[1]+194, inventory_bottom_right[0]-538,inventory_bottom_right[1]-194)
#pg.screenshot('inventory.png', inventory)

# runelite plug-in screen stuff
runelite_plugin_bottom_right=(1047,535)
runelite_plugin=(top_left[0]+780,top_left[1]+30,runelite_plugin_bottom_right[0]-780,runelite_plugin_bottom_right[1]-30)
#pg.screenshot('runelite_plugin.png', runelite_plugin)
scroll = 45
shop=(255,0,255)
glasscolor=(53,87,255)
green=(0,255,0)
n=25
crafting=False
flag=0
bag=Bag()

while True:
    if keyboard.is_pressed('q'):
        break
    if bag.bagcheck(glasscolor) == True:
        bag.crafting(glasscolor)
    elif pg.pixel(1184,505) == (134,20,20) and flag == 0:
        Randomize((454,522,490,511)).randleft()
        time.sleep(1.7)
        Randomize((888,940,234,240)).randleft()
        time.sleep(1.7)
        Randomize((775,859,269,293)).randleft()
        time.sleep(9)
        Randomize((765,869,336,372)).randleft()
        time.sleep(1.7)
        keyboard.press_and_release('x')
        time.sleep(1)
        Randomize((1520,1528,1013,1027)).randleft()
        time.sleep(1)
        Randomize((1491,1555,915,923)).randleft()
        time.sleep(1)
        Randomize((1463,1489,972,980)).randleft()
        time.sleep(9)
        keyboard.press_and_release('x')
        time.sleep(1)
        flag = 1
    elif pg.pixel(1184,505) == (134,20,20) and flag == 1:
        Randomize((454,522,490,511)).randleft()
        time.sleep(2)
        Randomize((888,940,234,240)).randleft()
        time.sleep(1.7)
        Randomize((780,856,329,339)).randleft()
        time.sleep(1.7)
        Randomize((775,859,269,293)).randleft()
        time.sleep(9)
        Randomize((765,869,336,372)).randleft()
        time.sleep(1.7)
        keyboard.press_and_release('x')
        time.sleep(1)
        Randomize((1520,1528,1013,1027)).randleft()
        time.sleep(1)
        Randomize((1491,1555,915,923)).randleft()
        time.sleep(1)
        Randomize((1485,1505,989,993)).randleft()
        time.sleep(9)
        keyboard.press_and_release('x')
        time.sleep(1)
        flag = 0
    else:
        try:
            loc=findobj(shop)
            Randomize((loc[0]+2,loc[0]+3,loc[1]+8,loc[1]+8)).randleft()
            time.sleep(2)
        except:
            'oops couldnt find color'
        if pg.pixel(897,553) == (70,61,50):
            pg.leftClick(bag.bag[2], duration=.3)
            time.sleep(.8)
            Randomize((713,721,443,445)).randleft()
            time.sleep(.8)
            Randomize((760,768,445,455)).randleft()
            time.sleep(.8)
            Randomize((918,930,314,322)).randleft()
            time.sleep(.8)
            keyboard.press_and_release('v')
            time.sleep(.8)
            Randomize((1521,1529,849,863)).randleft()
            time.sleep(1.8)
            keyboard.press_and_release('x')
       




"""while True:
    if keyboard.is_pressed('q'):
        break
    if pg.pixel(897,553) == (70,61,50):
        Randomize((713,721,443,445)).randleft()
        time.sleep(.3)
        Randomize((760,768,445,455)).randleft()
        time.sleep(.3)
        Randomize((918,930,314,322)).randleft()
        time.sleep(.3)
        keyboard.press_and_release('v')
        time.sleep(.1)
        Randomize((1521,1529,849,863)).randleft()
        time.sleep(1.5)
        keyboard.press_and_release('x')
        Randomize((1521,1529,849,863)).randleft()
    try:
        loc=findobj(shop)
        pg.leftClick(loc[0]-1,loc[1]+11)
        time.sleep(1.8)
    except:
        'oops couldnt find color'"""
