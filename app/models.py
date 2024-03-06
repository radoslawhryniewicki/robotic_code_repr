from pydantic import BaseModel


from app.enums import CommandEnum


class Commands(BaseModel):
    commands: list[CommandEnum]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "commands": [
                        "UP",
                        "UP",
                        "UP",
                        "UP",
                        "DOWN",
                        "DOWN",
                        "DOWN",
                        "RIGHT",
                        "RIGHT",
                        "RIGHT",
                        "RIGHT",
                        "RIGHT",
                        "RIGHT",
                        "GRAB",
                        "GRAB",
                    ]
                }
            ]
        }
    }


class RoboticCode(BaseModel):
    rcr: str
