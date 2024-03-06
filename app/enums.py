from enum import Enum


class CommandEnum(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    DROP = "DROP"
    GRAB = "GRAB"
