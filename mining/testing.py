def findobjat(objsRGBVal,coords=(0,0,1080,670)):#topleftx, toplefty, bottomrightx, bottomrighty
    flag=0
    wincap = WindowCapture('RuneLite')
    screenshot=pg.screenshot('test.png',region=(wincap.coords[0],wincap.coords[1],coords[2],coords[3]))
    
    
    for y in range(coords[1], coords[3], 2):#1,3
        for x in range(coords[0], coords[2], 2):#0,2
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return new_x,new_y
