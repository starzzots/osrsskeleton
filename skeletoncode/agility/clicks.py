import random
import time
import keyboard
import pyautogui as pg
import win32api
import win32con


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
        self.click_random_sec = random.choice(range(3, 10))/10
        self.duration_time = random.choice(range(1,2))

    def shiftclick(self):
        keyboard.press('shift')
        pg.moveTo(self.new_x,self.new_y, duration=.25)
        time.sleep(self.click_random_sec)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep2)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
    
    
    def randleft(self):
        time.sleep(self.click_random_sec)
        pg.moveTo(self.new_x,self.new_y, duration=.45)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.click_random_sec)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(self.click_random_sec)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        pg.moveTo(x, y, duration=.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(self.click_random_sec)

def findobj(self, objsRGBVal,screen):
        flag=0
        #screen shots location cords passed
        ss = pg.screenshot(region=screen)
        #loops through screen shot region from left to right by 5 pixel increments
        for y in range(screen[1], screen[3], 5):
            for x in range(screen[0], screen[2], 5):
                #red, green, blue at each x,y cord
                rgb = ss.getpixel((x, y))
                #checks if rbg value == the color rgb value passed through
                if rgb==objsRGBVal:
                    flag = 1
                    new_x= x
                    new_y= y
                    time.sleep(self.click_random_sec)
                    break
            #if rgb found save x,y cords and send back                
            if flag == 1:
                    return new_x,new_y