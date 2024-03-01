from skeletoncode.clicks import *
import sys
import keyboard
import time

class Login:
    #logout
    logout_button = (3598,3624 ,2042 ,2073)
    clicK_here_to_logout = (3519, 3700, 1971, 1993)

    #check login page
    login_page = (1889, 509)
    login_page_color = (74,76,85)
    log_in = (1752, 2032, 397,452)
    click_here_play = (1741, 2045, 490, 587)

    #Hopping worlds
    click_switch_worlds = (1343, 1459, 742, 766)
    world_421 = (1977, 2085,345, 358)
    world_353 = (1695,1810,176,192 )
    world_339 = (1560, 1674,465,479)
    world_374 = (1841, 1953,91,104 )
    world_348 = (1561,1671 ,717,732 )
    world_list = [world_421, world_353, world_339, world_374, world_348]

    def hop_worlds(self):
        Randomize(self.click_switch_worlds).randleft()
        selected_world = random.choice(self.world_list)
        Randomize(selected_world).randleft()

    def login(self):
        Randomize(self.log_in).randleft()
        time.sleep(15)
        Randomize(self.click_here_play).randleft()
        time.sleep(15)



    def check_login(self):
        login_page_expected_colors = pg.pixel(self.login_page[0], self.login_page[1])
        if login_page_expected_colors == self.login_page_color:
            self.hop_worlds()
            


    def log_out(self):
        time.sleep(15)
        Randomize(self.logout_button).randleft()
        Randomize(self.clicK_here_to_logout).randleft()
        self.laps = 0