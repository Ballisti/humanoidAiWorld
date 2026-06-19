import os
from dotenv import load_dotenv
from anthropic import Anthropic

chatHistory="""You are an agent in a grid world. On each turn you will receive 
    an observation and must output exactly ONE action in this format:

    ACTION: up
    REASON: The key is to my north and I need it to unlock the door.

    Valid actions: up, down, left, right, pick_up

    A is your current position, G is the goal position, K is a key , | and _ are walls, and . are empty spaces.
    You can move up, down, left, or right and pick up the key.
    You can wrap around the edges of the world, but you cannot move onto a square containing a wall.
    You must pick up the key by standing on its square and using pick_ip action before going to the goal
    Do not output anything else. You must always output a valid action.
"""

load_dotenv(".env")
client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def sendWorldState(world_state=""):
    global chatHistory
    chatHistory+="\n"+world_state
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": chatHistory,
            }
        ],
        model="claude-sonnet-4-6",
    )
    chatHistory+=str(message.content)
    print(message.content)
    return str(message.content)