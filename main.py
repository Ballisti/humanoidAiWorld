import world
import agent

world.createWorld(10, 10)
print(world.displayWorld())

foundGoal=False
while not foundGoal:
    foundGoal=world.parseResponse(agent.sendWorldState(world.displayWorld()))
    print(world.displayWorld())