from numpy.random import choice,randint
keyFound="not found"
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
    
    #ensures start, goal and key points are not same
    xS=xG=yS=yG=xK=yK=0
    while xS==xG and yS==yG and xS==xK and yS==yK and xG==xK and yG==yK:
        xS,xG,xK=randint(0,width),randint(0,width),randint(0,width)
        yS,yG,yK=randint(0,height),randint(0,height),randint(0,height)
        
    
    world[yG][xG]="G"    
    world[yS][xS]="A"
    world[yK][xK]="K"

    #makes sure that the start and goal points are not surrounded by walls
    for i in [xG,xS,xK]:
        if world[yG][(i+1)%len(world[0])]=="|" or world[yG][(i+1)%len(world[0])]=="_":
            world[yG][(i+1)%len(world[0])]="."
        if world[yG][(i-1)%len(world[0])]=="|" or world[yG][(i-1)%len(world[0])]=="_":
            world[yG][(i-1)%len(world[0])]="."
    for i in [yG,yS,yK]:
        if world[(i+1)%len(world)][xG]=="|" or world[(i+1)%len(world)][xG]=="_":
            world[(i+1)%len(world)][xG]="."
        if world[(i-1)%len(world)][xG]=="|" or world[(i-1)%len(world)][xG]=="_":
            world[(i-1)%len(world)][xG]="."
   
def displayWorld():
    displayText=""
    for row in world:
        for value in row:
            if value=="A":
                displayText += "\033[34mA\033[0m "
            elif value=="G":
                displayText += "\033[32mG\033[0m "
            elif value=="|" or value=="_":
                displayText += "\033[31m" + value + "\033[0m "
            else:
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
            if world[y][x]=="A":
                if keyFound=="onKey":
                    world[y][x]="K"
                world[y][x]="."
                agentX,agentY=x,y
    
    #move agent in the specified direction and wrap around if necessary
    if action=="up" and (agentY-1)%len(world)!="\033[31m|\033[0m" and (agentY-1)%len(world)!="\033[31m_\033[0m":
        agentY=(agentY-1)%len(world)
    elif action=="down" and (agentY+1)%len(world)!="\033[31m|\033[0m" and (agentY+1)%len(world)!="\033[31m_\033[0m": 
        agentY=(agentY+1)%len(world)
    elif action=="left" and (agentX-1)%len(world[0])!="\033[31m|\033[0m" and (agentX-1)%len(world[0])!="\033[31m_\033[0m":
        agentX=(agentX-1)%len(world[0])
    elif action=="right" and (agentX+1)%len(world[0])!="\033[31m|\033[0m" and (agentX+1)%len(world[0])!="\033[31m_\033[0m":
        agentX=(agentX+1)%len(world[0])
    
    if keyFound=="onKey" and action=="pick_up":
        keyFound="found"
        print("Agent has the key")
    if world[agentY][agentX]=="K":
        keyFound="onKey"
    elif keyFound!="found":
        keyFound="not found"
    
    if world[agentY][agentX]=="G" and keyFound=="found":
        print("Agent has reached the goal!")
        world[agentY][agentX]="A"
        return True
    world[agentY][agentX]="A"
    return False


def parseResponse(response):
    if "ACTION:" in response:
        action=response.split("ACTION:")[1].split("\\")[0].strip()
        print(f"\033[32mAgent action:\033[34m{action}\033[0m")
        return moveAgent(action)
    