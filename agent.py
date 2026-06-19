import os
from dotenv import load_dotenv
from anthropic import Anthropic

print(load_dotenv("keys.env"))
client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": 
            """You are an agent in a grid world. On each turn you will receive 
an observation and must output exactly ONE action in this format:

ACTION: move_north
REASON: The key is to my north and I need it to unlock the door.

Valid actions: move_north, move_south, move_east, move_west, 
               pick_up [item], use [item] on [target], look, think [text]

Do not output anything else.""",
        }
    ],
    model="claude-sonnet-4-6",
)
print(message.content)