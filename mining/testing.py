
def findobjat(objsRGBVal,coords=(0,0,1080,670),stepleftright=1,stepupdown=1):#topleftx, toplefty, bottomrightx, bottomrighty
    flag=0
    wincap = WindowCapture('RuneLite')
    screenshot=pg.screenshot('test.png',region=(wincap.coords[0],wincap.coords[1],coords[2],coords[3]))
    
    
    for y in range(coords[1], coords[3], stepupdown):#1,3
        for x in range(coords[0], coords[2], stepleftright):#0,2
            rgb = screenshot.getpixel((x, y))
            if rgb==objsRGBVal:
                flag = 1
                new_x= x+wincap.coords[0]
                new_y= y+wincap.coords[1]
                sleep(0.05)
                break
                            
        if flag == 1:
                return new_x,new_y

class Locate():
    def __init__(self, deltax, deltay,x1=0,x2=0,y1=0,y2=0):
        self.deltax=deltax
        self.deltay=deltay
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.locationc = wincap.coords[0]+self.deltax,wincap.coords[1]+self.deltay
        
    def item(self):
        location = (self.locationc[0]+self.x1,self.locationc[0]+self.x2,self.locationc[1]+self.y1,self.locationc[1]+self.y2)
        return location
