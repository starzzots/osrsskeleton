from clicks import *
dropc = (255,0,0)
color=(0,0,3)
bank=(255,115,0)
door1=(25,255,0)
door2=(53,255,0)
farmer=(200,0,250)
foodcheck=(255,250,0)

health=(1419,942)#color = (122,27,8)  21 hp level for now till i level up maybe

bag=Bag()

theiving=True
banking=False
eating=False
count=0


while True:
    slot1 = bag.slotcheck(0)
    healthcheck=pg.pixel(health[0],health[1])
    #print(healthcheck)
    if theiving == True:
        if healthcheck!=(122,27,8):
            #print('need food...')
            if bag.slotcheck(0) == foodcheck:
                #print('You have food you can eat')
                bag.eating(foodcheck)
        elif pg.pixel(1499,875) == dropc or pg.pixel(1503,877) == dropc or pg.pixel(1517,869) == dropc or pg.pixel(1507,864) == dropc:
            bag.drop(dropc)
        elif pg.pixel(1462,766) != foodcheck:
            bag.drop(dropc)
            time.sleep(.25)
            try:
                bankloc=findobj(bank)
                Randomize((bankloc[0]+15,bankloc[0]+20,bankloc[1]+18,bankloc[1]+25)).randleft()
                time.sleep(10)
            except:
                print('ooioofofoofofof')
        if count == 5:
            keyboard.press('pageup')
            time.sleep(5)
            keyboard.release('pageup')
            time.sleep(6.5)
            keyboard.press('x')
            time.sleep(1)
            keyboard.release('x')
            time.sleep(.5)
            count = 0
            time.sleep(2)
       
        elif pg.pixel(474,497) == (73,64,52):
            Randomize((519,529,138,149)).randleft()#food
            time.sleep(.5)
            Randomize((918,928,63,70)).randleft()#exit
            time.sleep(.5)
            count+=1
        
        else:
            try:
                loc=findobj(farmer)# looks for shop color and returns its x and y
                Randomize((loc[0]+2,loc[0]+3,loc[1]+15,loc[1]+15)).randleftspeed()
            except:
                middle=findobj(color)
                Randomize((middle[0]+5,middle[0]+10,middle[1]+5, middle[1]+10)).randleft()
                time.sleep(3)
            