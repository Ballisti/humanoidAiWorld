from numpy.random import choice,randint
keyFound="not found"

red="\033[31m"
green="\033[32m"
blue="\033[34m"
colClear="\033[0m"

horizWall=red+"_"+colClear
vertWall=red+"|"+colClear
agent=blue+"A"+colClear
goal=green+"G"+colClear

def createWorld(width=10, height=10):
    global world
    #generates empty world
    world= [[""]*width for i in range(height)]

    #adds object to world
    for y in range(height):
        for x in range(width):
            world[y][x] = choice(
                [".",(horizWall,vertWall)[y!=0 and y!=height-1]],
                p=[0.8,0.2]
            )
    
    #ensures start, goal and key points are not same
    xS=xG=yS=yG=xK=yK=0
    while xS==xG and yS==yG and xS==xK and yS==yK and xG==xK and yG==yK:
        xS,xG,xK=randint(0,width),randint(0,width),randint(0,width)
        yS,yG,yK=randint(0,height),randint(0,height),randint(0,height)
        
    
    world[yG][xG]=goal  
    world[yS][xS]=agent
    world[yK][xK]="K"

    #makes sure that the start and goal points are not surrounded by walls
    for i in [xG,xS,xK]:
        if world[yG][(i+1)%len(world[0])]==vertWall or world[yG][(i+1)%len(world[0])]==horizWall:
            world[yG][(i+1)%len(world[0])]="."
        if world[yG][(i-1)%len(world[0])]==vertWall or world[yG][(i-1)%len(world[0])]==horizWall:
            world[yG][(i-1)%len(world[0])]="."
    for i in [yG,yS,yK]:
        if world[(i+1)%len(world)][xG]==vertWall or world[(i+1)%len(world)][xG]==horizWall:
            world[(i+1)%len(world)][xG]="."
        if world[(i-1)%len(world)][xG]==vertWall or world[(i-1)%len(world)][xG]==horizWall:
            world[(i-1)%len(world)][xG]="."
   
def displayWorld():
    displayText=""
    for row in world:
        for value in row:
            displayText += value + " "
        displayText += "\n "
    displayText+="key: "+keyFound+"\n"
    return displayText.strip()

def moveAgent(action):
    global keyFound
    #find current position of agent and remove it from the world
    agentX=agentY=0
    for y in range(len(world)):
        for x in range(len(world[y])):
            if world[y][x]==agent:
                if keyFound=="onKey":
                    world[y][x]="K"
                world[y][x]="."
                agentX,agentY=x,y
    
    #move agent in the specified direction and wrap around if necessary
    if action=="up" and world[(agentY-1)%len(world)][agentX]!="|" and world[(agentY-1)%len(world)][agentX]!="_":
        agentY=(agentY-1)%len(world)
    elif action=="down" and world[(agentY+1)%len(world)][agentX]!="|" and world[(agentY+1)%len(world)][agentX]!="_": 
        agentY=(agentY+1)%len(world)
    elif action=="left" and world[agentY][(agentX-1)%len(world[0])]!="|" and world[agentY][(agentX-1)%len(world[0])]!="_":
        agentX=(agentX-1)%len(world[0])
    elif action=="right" and world[agentY][(agentX+1)%len(world[0])]!="|" and world[agentY][(agentX+1)%len(world[0])]!="_":
        agentX=(agentX+1)%len(world[0])
    
    if keyFound=="onKey" and action=="pick_up":
        keyFound="found"
        print("Agent has the key")
    if world[agentY][agentX]=="K":
        keyFound="onKey"
    elif keyFound!="found":
        keyFound="not found"
    
    if world[agentY][agentX]==goal and keyFound=="found":
        print("Agent has reached the goal!")
        world[agentY][agentX]=agent
        return True
    world[agentY][agentX]=agent
    return False


def parseResponse(response):
    if "ACTION:" in response:
        action=response.split("ACTION:")[1].split("\\")[0].strip()
        print(f"{green}Agent action:{blue}{action}\033[0m")
        return moveAgent(action)
    