from clicks import *
import sys
import keyboard
import time


# Stops the program
running = False

center = (1885, 1079)

#Obstacle colors ~~ We use this to determine the players location.
first_jump_center_color = (0, 0, 0)
second_jump_center_color = (0, 0, 1)
third_jump_center_color = (5, 5, 5)
fourth_jump_center_color = (0, 0, 3)
fifth_jump_center_color = (0, 0, 4)
finish_color = (10, 10, 10)
finsih_start_color = (0, 0, 6)

random_color_spot_on_fifth = (30, 30, 30)
random_color_spot_on_fifth2 = (50, 50, 50)

fail1_center_color = (25, 25, 25)
fail2_center_color = (20, 20, 20)

# Obstacle jump ~~ after we find our location we determine where to click to jump using the below cords
first_jump = (1876, 1891, 768, 808 )
second_jump = (1791, 1812, 1058, 1063)
third_jump = (1809, 1833, 1050, 1089)
fourth_jump = (1883, 1902, 1166, 1213)
fifth_jump = (1959, 1970, 1260 , 1279)

finsih = (1899, 1915, 1063, 1104)
finsih_start = (2004, 2020, 1034, 1043)

random_jump_spot_on_fifth = (1956,1975,1144,1161)
random_jump_spot_on_fifth2 = (1907,1926,1053,1065)

fail1_start = (2392, 2408, 1504, 1513)
fail2_start = (2056, 2077, 1369, 1380)

# token 1st
token_1st_grab = (1915, 1924, 1058, 1064)
token_1st_jump = (1809, 1833, 1050, 1089)
token_1st_location = (1920, 1059)
token_1st_color = (7, 7, 7)

# logout
logout_button = (3598, 3624, 2042, 2073)
clicK_here_to_logout = (3519, 3700, 1971, 1993)

# check login page
login_page = (1889, 509)
login_page_color = (74, 76, 85)
log_in = (1752, 2032, 397, 452)
click_here_play = (1741, 2045, 490, 587)

# Hopping worlds
click_switch_worlds = (1343, 1459, 742, 766)
world_421 = (1977, 2085, 345, 358)
world_353 = (1695, 1810, 176, 192)
world_339 = (1560, 1674, 465, 479)
world_374 = (1841, 1953, 91, 104)
world_348 = (1561, 1671, 717, 732)
world_list = [world_421, world_353, world_339, world_374, world_348]

# laps
laps = 0
time_sleep = 1

next_jump = False


def quit():
    global running
    running = True


# set hotkey to stop the program
keyboard.add_hotkey('q', lambda: quit())


def hop_worlds():
    Randomize(click_switch_worlds).randleft()
    selected_world = random.choice(world_list)
    Randomize(selected_world).randleft()


def login():
    Randomize(log_in).randleft()
    time.sleep(15)
    Randomize(click_here_play).randleft()
    time.sleep(5)


def check_login():
    login_page_expected_colors = pg.pixel(login_page[0], login_page[1])
    if login_page_expected_colors == login_page_color:
        hop_worlds()
        time.sleep(1)
        login()


def log_out():
    time.sleep(15)
    Randomize(logout_button).randleft()
    Randomize(clicK_here_to_logout).randleft()
    global laps
    laps = 0


def token_check(location, token_click, jump, color):
    global next_jump
    next_jump = False
    token = pg.pixel(location[0], location[1])
    if token == color:
        Randomize(token_click).randleft()
        time.sleep(random.choice(range(5, 10)) / 10)
        Randomize(jump).randleft()
        time.sleep(random.choice(range(5, 10)) / 10)
        next_jump = True
        return next_jump
    return next_jump


def check_token_on_course():
    current_center = pg.pixel(center[0], center[1])
    global next_jump
    if current_center == third_jump_center_color:
        next_jump = token_check(token_1st_location, token_1st_grab, token_1st_jump, token_1st_color)
    return next_jump


def course():
    global laps
    current_center = pg.pixel(center[0], center[1])
    if current_center == first_jump_center_color:
        Randomize(first_jump).randleft()
    elif current_center == second_jump_center_color:
        Randomize(second_jump).randleft()
    elif current_center == third_jump_center_color:
        time.sleep(random.choice(range(7,10))/10)
        if not check_token_on_course():
            Randomize(third_jump).randleft()
    elif current_center == fourth_jump_center_color:
        Randomize(fourth_jump).randleft()
    elif current_center == fifth_jump_center_color:
        Randomize(fifth_jump).randleft()
        time.sleep(3)
    elif current_center == finish_color:
        Randomize(finsih).randleft()
        laps = laps + 1
    elif current_center == finsih_start_color:
        Randomize(finsih_start).randleft()
    elif current_center == fail1_center_color:
        Randomize(fail1_start).randleft()
    elif current_center == fail2_center_color:
        Randomize(fail2_start).randleft()
    elif current_center == random_color_spot_on_fifth:
        Randomize(random_jump_spot_on_fifth).randleft()
    elif current_center == random_color_spot_on_fifth2:
        Randomize(random_jump_spot_on_fifth2).randleft()


while not running:
    time.sleep(random.choice(range(1,11)) / 10)
    check_login()
    course()
    time.sleep(random.choice(range(8,11)) / 10)
    if laps == random.choice(range(80,120)):
       log_out()
