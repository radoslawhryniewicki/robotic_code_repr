from pydantic import BaseModel


class Commands(BaseModel):
    commands: list[str]

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
