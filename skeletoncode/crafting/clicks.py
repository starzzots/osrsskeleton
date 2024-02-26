import pyautogui as pg
import mouse
import time
import random
import win32con, win32api
import keyboard
from win32gui import FindWindow, GetWindowRect



class Bag():
    def __init__(self):
        self.bag=[
            (1461,765),(1504,765),(1548,765),(1590,765),
            (1461,803),(1504,803),(1548,803),(1590,803),
            (1461,839),(1504,839),(1548,839),(1590,839),
            (1461,875),(1504,875),(1548,875),(1590,875),
            (1461,911),(1504,911),(1548,911),(1590,911),
            (1461,949),(1504,949),(1548,949),(1590,949),
            (1461,984),(1504,984),(1548,984),(1590,984)
        ]
    
    def bagcheck(self, rgb):
        for i in self.bag:
             if pg.pixel(i[0],i[1]) == rgb:
                  return True
        return False
    
    def crafting(self, rgb):
        count = 0
        ticks=1.8
        for i in self.bag:
            if pg.pixel(i[0],i[1]) == rgb:
                count+=1
                temp=i
        pg.leftClick(self.bag[1],duration=.3)
        time.sleep(.8)
        pg.leftClick(temp, duration=.3)
        time.sleep(1)
        keyboard.press_and_release('space')
        time.sleep(ticks*(count+1))
        keyboard.press('pageup')
        time.sleep(5)
        keyboard.release('pageup')
        time.sleep(7.5)
        keyboard.press('x')
        time.sleep(1)
        keyboard.release('x')
        time.sleep(2.5)


          
     
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
        pg.moveTo(self.new_x,self.new_y, duration=.25)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.08)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep2)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
    
    
    def randleft(self):
        pg.moveTo(self.new_x,self.new_y, duration=.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.03)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        pg.moveTo(x, y, duration=.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(.1)
       

def findobj(objsRGBVal):
        flag=0
        
        screen=pg.screenshot(region=(0,0,1920,1080))
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