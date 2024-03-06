from fastapi import FastAPI, HTTPException
from app.enums import CommandEnum
from app.exceptions import InsufficientCounterLength
from app.models import RoboticCode, Commands
from app.robotic_code_repr_service import RoboticCodeReprService
from app.store import COMMANDS_STORE

app = FastAPI()


@app.post("/commands/", status_code=200)
def add_commands(commands: Commands):
    for command in commands.commands:
        COMMANDS_STORE["commands"].append(command)
    return "Commands Added!"


@app.get("/rcrs/{command}", response_model=RoboticCode, status_code=200)
def get_code(command: CommandEnum):
    try:
        robotic_code_repr_service = RoboticCodeReprService()
        robotic_code_repr_service.create_codes_from_commands()
        return RoboticCode(rcr=robotic_code_repr_service.get_code(command))
    except KeyError:
        raise HTTPException(status_code=404, detail="No such command in commands")
    except InsufficientCounterLength:
        raise HTTPException(
            status_code=400,
            detail="You must provide at least 2 unique commands to generate RCRs",
        )
