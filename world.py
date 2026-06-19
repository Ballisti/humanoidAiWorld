from numpy.random import choice,randint
def createWorld(width=10, height=10):
    global world

    #generates empty world
    world= [[""]*height for i in range(width)]

    #adds object to world
    for y in range(width):
        for x in range(height):
            world[y][x] = choice(
                [".","|"],
                p=[0.8,0.2]
            )
    
    #ensures start and goal points are not same
    xS=xG=yS=yG=0
    while xS==xG and yS==yG:
        xS,xG=randint(0,width),randint(0,width)
        yS,yG=randint(0,height),randint(0,height)
    
    world[randint(0,height)][randint(0,width)]="G"    
    world[randint(0,height)][randint(0,width)]="A"    

createWorld()
for row in world:
    for value in row:
        print(value,end=" ")
    print()