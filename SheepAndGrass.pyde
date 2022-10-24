from random import choice

WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
colorList = [WHITE,RED,YELLOW,PURPLE]

class Sheep:
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.sz = 10
        self.energy = 20
        self.col = col
        self.age = 1
        
    def update(self):
        move = 8
        self.energy -= 1
        if self.energy >=50:
            self.energy -=30
            sheepList.append(self)
        if self.age >=5000:
            sheepList.remove(self)
        self.x += random(-move, move)
        self.y += random(-move, move)
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %=height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        xscl=int(self.x / patchSize)
        yscl=int(self.y / patchSize)
        grass=grassList[xscl * rows_of_grass+yscl]
        if not grass.eaten:
            self.energy += grass.energy
            self.age += grass.energy
            grass.eaten = True
         
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz)
        
class Grass:
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 50
        self.eaten = False
        self.sz = sz
        
    def update(self):
        if self.eaten:
            if random(100) < 5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)

sheepList = []
grassList = []
patchSize = 10

def setup():
    global rows_of_grass
    size (600,600)
    rows_of_grass = height/patchSize
    noStroke()
    for i in range(20):
        sheepList.append(Sheep(random(width),
                               random(height),
                               choice(colorList)))
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
    
def draw():
    background(WHITE)
    for grass in grassList:
        grass.update()
    for sheep in sheepList:
        sheep.update()
