from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from collections import Counter
from rcr import RCRS

from store import COMMANDS_STORE
app = FastAPI()

class CommandEnum(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    DROP = "DROP"
    GRAB = "GRAB"


class CommandsModel(BaseModel):
    commands: list[CommandEnum]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "commands": ["UP", "UP", "UP", "UP", 
                                 "DOWN", "DOWN", "DOWN",
                                 "RIGHT", "RIGHT", "RIGHT", "RIGHT", "RIGHT", "RIGHT",
                                 "GRAB", "GRAB"]
                }
            ]
        }
    }



@app.post('/commands/', status_code=200)
def add_commands(commands: CommandsModel):
    for command in commands.commands:
        COMMANDS_STORE['commands'].append(command)
    return "Commands Added!"


@app.get('/rcrs/{command}')
def get_rcr_for_command(command: CommandEnum):
    rcrs = RCRS()
    rcrs.create()
    rcr = rcrs.get_rcr_for(command)
    return {'rcr': rcr}