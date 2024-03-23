def findobjat(objsRGBVal,topleftx=0,toplefty=0,bottomx=1080,bottomy=670):
    flag=0
    wincap = WindowCapture('RuneLite')
    screenshot=pg.screenshot('test.png',region=(wincap.coords[0],wincap.coords[1],bottomx,bottomy))
    
    
    for y in range(toplefty, bottomy, 2):
        for x in range(topleftx, bottomx, 2):
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return new_x,new_y
