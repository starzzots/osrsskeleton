import pyautogui as pg
import keyboard


def print_cords():
    x, y = pg.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(f"\nCords")
    print("----")
    print(positionStr, end='')
    print("\n----")

def refresh():
    print("===========================================")
    print("===========================================")
    print("===========================================")
    print("===========================================")

keyboard.add_hotkey('i',lambda:print_cords())

keyboard.add_hotkey('r',lambda: refresh())
#pg.moveTo(0,1)
keyboard.add_hotkey('n',lambda:pg.displayMousePosition())
#120,0,139
#255,3,25
cords = False
def quit():
    global cords
    cords = True
#set hotkey to quit
keyboard.add_hotkey('e',lambda:quit())

while not cords:
    pass
