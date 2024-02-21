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
#pg.screenshot('runelite.png', screen) #taking screen shot and saves it so you can see applys for all pg.screenshot

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





"""try: 
    fishing=findobj(purple, gameplay)
except:
    pass
fishing=(fishing[0]+10,fishing[1]+10)
pg.moveTo(fishing)"""