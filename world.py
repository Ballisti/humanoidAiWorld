from numpy.random import choice,randint

def createWorld(width=10, height=10):
    global world
    #generates empty world
    world= [[""]*width for i in range(height)]

    #adds object to world
    for y in range(height):
        for x in range(width):
            world[y][x] = choice(
                [".",("_","|")[y!=0 and y!=height-1]],
                p=[0.8,0.2]
            )
    
    #ensures start and goal points are not same
    xS=xG=yS=yG=0
    while xS==xG and yS==yG:
        xS,xG=randint(0,width),randint(0,width)
        yS,yG=randint(0,height),randint(0,height)
    
    world[yG][xG]="G"    
    world[yS][xS]="A"

    #makes sure that the start and goal points are not surrounded by walls
    if world[yG][(xG+1)%len(world[0])]=="|" or world[yG][(xG+1)%len(world[0])]=="_":
        world[yG][(xG+1)%len(world[0])]="."
    if world[yG][(xG-1)%len(world[0])]=="|" or world[yG][(xG-1)%len(world[0])]=="_":
        world[yG][(xG-1)%len(world[0])]="."
    if world[(yG+1)%len(world)][xG]=="|" or world[(yG+1)%len(world)][xG]=="_":
        world[(yG+1)%len(world)][xG]="."
    if world[(yG-1)%len(world)][xG]=="|" or world[(yG-1)%len(world)][xG]=="_":
        world[(yG-1)%len(world)][xG]="."
   
def displayWorld():
    for row in world:
        for value in row:
            if value=="A":
                print("\033[34mA\033[0m",end=" ")
            elif value=="G":
                print("\033[32mG\033[0m",end=" ")
            elif value=="|" or value=="_":
                print("\033[31m" + value + "\033[0m",end=" ")
            else:
                print(value,end=" ")
        print()

def moveAgent(direction):
    #find current position of agent and remove it from the world
    agentX=agentY=0
    for y in range(len(world)):
        for x in range(len(world[y])):
            if world[y][x]=="A":
                world[y][x]="."
                agentX,agentY=x,y
    
    #move agent in the specified direction and wrap around if necessary
    if direction=="up" and (agentY-1)%len(world)!="|" and (agentY-1)%len(world)!="_":
        agentY=(agentY-1)%len(world)
    elif direction=="down" and (agentY+1)%len(world)!="|" and (agentY+1)%len(world)!="_": 
        agentY=(agentY+1)%len(world)
    elif direction=="left" and (agentX-1)%len(world[0])!="|" and (agentX-1)%len(world[0])!="_":
        agentX=(agentX-1)%len(world[0])
    elif direction=="right" and (agentX+1)%len(world[0])!="|" and (agentX+1)%len(world[0])!="_":
        agentX=(agentX+1)%len(world[0])
    world[agentY][agentX]="A"
    if world[agentY][agentX]=="G":
        print("Agent has reached the goal!")
    displayWorld()


    