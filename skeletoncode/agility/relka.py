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
finish_color = (0, 0, 5)
finsih_start_color = (0, 0, 6)

fail1_center_color = (15, 15, 15)
fail2_center_color = (10, 10, 10)

# Obstacle jump ~~ after we find our location we determine where to click to jump using the below cords
first_jump = (1778, 1859, 1165, 1225)
second_jump = (1906, 1930, 1283, 1311)
third_jump = (1930, 2025, 993, 1019)
fourth_jump = (1978, 2028, 1006, 1039)
fifth_jump = (1981, 1999, 910, 928)
finsih = (1840, 1903, 879, 945)
finsih_start = (1261, 1283, 1043, 1044)

fail1_start = (1922, 1930, 543, 567)
fail2_start = (1701, 1710, 577, 596)

# token 1st
token_1st_grab = (1842, 1854, 1080, 1091)
token_1st_jump = (1837, 1901, 1144, 1217)
token_1st_location = (1849, 1086)
token_1st_color = (7, 7, 7)

# token 3rd
token_3rd_grab = (1914, 1924, 1105, 1114)
token_3rd_jump = (1907, 2000, 935, 974)
token_3rd_location = (1921, 1108)
token_3rd_color = (7, 7, 7)

token_3rd_grab2 = (1937, 1949, 1082, 1093)
token_3rd_jump2 = (1888, 1969, 965, 997)
token_3rd_location2 = (1943, 1082)
token_3rd_color2 = (7, 7, 7)

# token 4th
token_4th_grab = (1963, 1975, 1103, 1114)
token_4th_jump = (1909, 1945, 964, 1002)
token_4th_location = (1973, 1108)
token_4th_color = (7, 7, 7)

token_4th_grab2 = (1936, 1947, 1130, 1143)
token_4th_jump2 = (1932, 1969, 941, 978)
token_4th_location2 = (1938, 1132)
token_4th_color2 = (7, 7, 7)

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
    if current_center == first_jump_center_color:
        next_jump = token_check(token_1st_location, token_1st_grab, token_1st_jump, token_1st_color)
    elif current_center == third_jump_center_color:
        next_jump = token_check(token_3rd_location, token_3rd_grab, token_3rd_jump, token_3rd_color) or token_check(token_3rd_location2, token_3rd_grab2, token_3rd_jump2, token_3rd_color2)
    elif current_center == fourth_jump_center_color:
       next_jump = token_check(token_4th_location, token_4th_grab, token_4th_jump, token_4th_color) or token_check(token_4th_location2, token_4th_grab2, token_4th_jump2, token_4th_color2)
    return next_jump


def course():
    global laps
    current_center = pg.pixel(center[0], center[1])
    if current_center == first_jump_center_color:
        time.sleep(random.choice(range(7,10))/10)
        if not check_token_on_course():
            Randomize(first_jump).randleft()
    elif current_center == second_jump_center_color:
        Randomize(second_jump).randleft()
    elif current_center == third_jump_center_color:
        time.sleep(random.choice(range(7,10))/10)
        if not check_token_on_course():
            Randomize(third_jump).randleft()
    elif current_center == fourth_jump_center_color:
        time.sleep(random.choice(range(7,10))/10)
        if not check_token_on_course():
            Randomize(fourth_jump).randleft()
    elif current_center == fifth_jump_center_color:
        Randomize(fifth_jump).randleft()
    elif current_center == finish_color:
        Randomize(finsih).randleft()
        laps = laps + 1
    elif current_center == finsih_start_color:
        Randomize(finsih_start).randleft()
    elif current_center == fail1_center_color:
        Randomize(fail1_start).randleft()
    elif current_center == fail2_center_color:
        Randomize(fail2_start).randleft()



while not running:
    check_login()
    course()
    time.sleep(random.choice(range(7, 10)) / 10)
    if laps == random.choice(range(80,120)):
       log_out()

    