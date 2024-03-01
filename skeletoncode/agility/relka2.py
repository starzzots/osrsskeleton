from clicks import *
import sys
import keyboard
import time
from skeletoncode.universal.login import Login

class RelkaBot:
    #Stops the program
    running = False

    center = (1885, 1079)


    #Obstalce Color Detection ~~ this is how we determine our location
    first_jump_center_color= (0,0,0)
    second_jump_center_color= (0,0,1)
    third_jump_center_color= (5,5,5)
    fourth_jump_center_color= (0,0,3)
    fifth_jump_center_color= (0,0,4)
    finish_color= (0,0,5)
    finsih_start_color= (0,0,6)

    fail1_center_color = (15,15,15)
    fail2_center_color = (10,10,10)

    #Obstacle jump ~~ after we find our location we determine where to click to jump using the below cords
    first_jump = (1778,1859, 1165, 1225)
    second_jump = (1906,1930,1283 ,1311)
    third_jump = (1930,2025,993 ,1019)
    fourth_jump = (1978,2028,1006 ,1039)
    fifth_jump = (1981,1999,910,928)
    finsih = (1829,1906,877,945)
    finsih_start = (1253,1294,1041,1044)


    fail1_start = (1922,1930,543 ,567)
    fail2_start = (1701,1710,577,596)


    #token 1st
    token_1st_grab = (1842,1854,1080,1091)
    token_1st_jump = (1837,1901,1144,1217)
    token_1st_location = (1849,1086)
    token_1st_color = (7,7,7)

    #token 3rd
    token_3rd_grab = (1914,1924,1105,1114)
    token_3rd_jump = (1907,2000,935,974)
    token_3rd_location = (1921,1108)
    token_3rd_color = (7,7,7)

    token_3rd_grab2 = (1937,1949,1082,1093)
    token_3rd_jump2 = (1888,1969,965,997)
    token_3rd_location2 = (1943,1082)
    token_3rd_color2 = (7,7,7)

    #token 4th
    token_4th_grab = (1963,1975,1103,1114)
    token_4th_jump = (1909,1945,964,1002)
    token_4th_location = (1973,1108)
    token_4th_color = (7,7,7)

    token_4th_grab2 = (1936,1947,1130,1143)
    token_4th_jump2 = (1932,1969,941,978)
    token_4th_location2 = (1938,1132)
    token_4th_color2 = (7,7,7)

    #laps
    laps = 0
    time_sleep = 1


    def __init__(self):
        self.laps = 0
    def quit():
        global running
        running = True
    #set hotkey to quit
    keyboard.add_hotkey('q',lambda:quit())


    def token_check(self,location,token_click, jump, color):
        next_jump = False
        token = pg.pixel(location[0],location[1])
        if token == color:
            Randomize(token_click).randleft()
            time.sleep(random.choice(range(5,10))/10)
            Randomize(jump).randleft()
            time.sleep(random.choice(range(5,10))/10)
            next_jump = True
            return next_jump
        return next_jump


    def check_token_on_course(self):
        current_center = pg.pixel(self.center[0],self.center[1])  
        if current_center == self.first_jump_center_color: 
            next_jump = self.token_check(self.token_1st_location, self.token_1st_grab, self.token_1st_jump, self.token_1st_color)
        elif current_center == self.third_jump_center_color:
            if self.token_check(self.token_3rd_location, self.token_3rd_grab, self.token_3rd_jump, self.token_3rd_color) or self.token_check(self.token_3rd_location2, self.token_3rd_grab2, self.token_3rd_jump2, self.token_3rd_color2):
                next_jump = True
            else:
                next_jump = False
        elif current_center == self.fourth_jump_center_color:
            if self.token_check(self.token_4th_location, self.token_4th_grab, self.token_4th_jump, self.token_4th_color) or self.token_check(self.token_4th_location2, self.token_4th_grab2, self.token_4th_jump2, self.token_4th_color2):
                next_jump = True
            else:
                next_jump = False
        return next_jump


    def course(self):
        current_center = pg.pixel(self.center[0],self.center[1])  
        if current_center == self.first_jump_center_color:
            if not self.check_token_on_course():
                Randomize(self.first_jump).randleft()
        elif current_center == self.second_jump_center_color:
            Randomize(self.second_jump).randleft()
        elif current_center == self.third_jump_center_color:
            if not self.check_token_on_course():
                Randomize(self.third_jump).randleft()
        elif current_center == self.fourth_jump_center_color:
            if not self.check_token_on_course():
                Randomize(self.fourth_jump).randleft()
        elif current_center == self.fifth_jump_center_color:
            Randomize(self.fifth_jump).randleft()
        elif current_center == self.finish_color:
            Randomize(self.finsih).randleft()
        elif current_center == self.finsih_start_color:
            Randomize(self.finsih_start).randleft()
        elif current_center == self.fail1_center_color:
            Randomize(self.fail1_start).randleft()
        elif current_center == self.fail2_center_color:
            Randomize(self.fail2_start).randleft()
        self.laps += 1

relka = RelkaBot()
login = Login()

while not running:
    login.check_login()
    relka.course()
    time.sleep(random.choice(range(7,10))/10)
    if relka.laps == 10:
       login.log_out()

    #range(80,120)