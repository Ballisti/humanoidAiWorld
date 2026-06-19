import os
from dotenv import load_dotenv
from anthropic import Anthropic

print(load_dotenv(".env"))
client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
systemPrompt="""You are an agent in a grid world. On each turn you will receive 
    an observation and must output exactly ONE action in this format:

    ACTION: up
    REASON: The key is to my north and I need it to unlock the door.

    Valid actions: up, down, left, right, 

    A is your current position, G is the goal position, | and _ are walls, and . are empty spaces.
    You can move up, down, left, or right.
    You can wrap around the edges of the world, but you cannot move through walls.
    Do not output anything else. You must always output a valid action.
"""
def sendWorldState(world_state=""):
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": systemPrompt + "\n" + world_state,
            }
        ],
        model="claude-sonnet-4-6",
    )
    print(message.content)
    return str(message.content)