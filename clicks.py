import pyautogui as pg
import time
import random
import win32con, win32api
import keyboard
    
     
class Randomize():
    def __init__(self,minMaxs):
        self.minMaxs = [minMaxs] # (min_x, max_x, min_y, max_y)
        self.x_min = minMaxs[0]
        self.x_max = minMaxs[1]
        self.y_min = minMaxs[2]
        self.y_max = minMaxs[3]
        self.random_pix_move_y = random.randrange(25,27,1)
        self.random_pix_move_x = random.randrange(-40,40,1)

        self.random_multi = random.randrange(30,50,1)/100

        self.random_sleep= random.randrange(30,40,1)/100
        self.random_sleep2= random.randrange(10,30,1)/100
        self.random_sleep3= random.randrange(30,50,1)/1000
        self.random_long_sleep = random.randrange(20,50,1)/100
        self.new_x = random.randrange(self.x_min, self.x_max+1)
        self.new_y = random.randrange(self.y_min, self.y_max+1)

    def shiftclick(self):
        keyboard.press('shift')
        pg.moveTo(self.new_x,self.new_y, duration=.08)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.08)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep2)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.03)
    
    
    def randleft(self):
        pg.moveTo(self.new_x,self.new_y, duration=.125)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.09)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.03)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        pg.moveTo(x, y, duration=.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(.1)
       
class Bag():
    def __init__(self):
        self.slot=[
            (1461,765),(1504,765),(1544,765),(1588,765),
            (1461,803),(1504,803),(1544,803),(1588,803),
            (1461,839),(1504,839),(1544,837),(1587,839),
            (1461,875),(1504,875),(1544,875),(1588,875),
            (1461,911),(1504,911),(1544,911),(1588,911),
            (1461,949),(1504,949),(1544,949),(1588,949),
            (1461,984),(1504,984),(1544,984),(1588,984)
        ]
    
    def drop(self,rgb):
        for i in self.slot:
            if pg.pixel(i[0],i[1]) == rgb:
                Randomize((i[0]-3,i[0]+3,i[1]-3,i[1]+3)).shiftclick()
    
    def bagcheck(self, rgb):
        for i in self.slot:
             if pg.pixel(i[0],i[1]) == rgb:
                  return True
        return False
    
    def eating(self,rgb):
        for i in self.slot:
            if pg.pixel(i[0],i[1]) == rgb:
                temp=i
        Randomize((temp[0]-5,temp[0]+5,temp[1]-5,temp[1]+5)).randleft()
        time.sleep(1.3)
    
    

    def slotcheck(self, bagslot):
        return pg.pixel(self.slot[int(bagslot)][0],self.slot[int(bagslot)][1])
    
    def crafting(self, rgb):
        count = 0
        ticks=1.8
        for i in self.slot:
            if pg.pixel(i[0],i[1]) == rgb:
                count+=1
                temp=i
        pg.leftClick(self.slot[1],duration=.3)#clicks bag slot 3
        time.sleep(.8)
        pg.leftClick(temp, duration=.3)#clicks the last item found with rgb color and clicks that spot
        time.sleep(1)
        keyboard.press_and_release('space') #have to manaully in osrs first craft the item you want then the hotkey will be space for it
        time.sleep(ticks*(count+2))# counts how many of the objs are in inv and sleeps according to how many items are there. For waiting time for evewrything to be crafted
        keyboard.press('pageup')# hotkey to switch worlds
        time.sleep(5)
        keyboard.release('pageup')# release the key presss
        time.sleep(7.5)
        keyboard.press('x')# bag hotkey ppress
        time.sleep(1)
        keyboard.release('x')#bag hotkey release
        time.sleep(2.5)

def findobj(objsRGBVal):
        flag=0
        
        screen=pg.screenshot(region=(0,0,1800,1080))
        width, height = screen.size
        for y in range(0, height, 2):
            for x in range(0, width-446, 2):
                rgb = screen.getpixel((x, y))
                if rgb==objsRGBVal:
                    flag = 1
                    new_x= x
                    new_y= y
                    time.sleep(0.05)
                    break
                            
            if flag == 1:
                    return new_x,new_y