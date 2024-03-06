import pytest
from app.exceptions import InsufficientCounterLength
from app.robotic_code_repr_service import RoboticCodeReprService
from app.store import COMMANDS_STORE


@pytest.fixture(scope="function", autouse=True)
def robotic_code_repr_service():
    yield RoboticCodeReprService()


class TestRoboticCodeReprService:

    @pytest.mark.parametrize("commands", [["UP"], []])
    def test_raise_exc_when_counter_length_insufficient(
        self, commands, robotic_code_repr_service
    ):
        COMMANDS_STORE["commands"] = commands

        with pytest.raises(InsufficientCounterLength):
            robotic_code_repr_service.create_codes_from_commands()

    def test_create_codes_from_many_commands(self, robotic_code_repr_service):
        COMMANDS_STORE["commands"] = [
            "UP",
            "DOWN",
            "RIGHT",
            "LEFT",
            "DROP",
            "GRAB",
            "MOVE",
            "TALK",
            "HANG",
            "TURNOFF",
        ]

        robotic_code_repr_service.create_codes_from_commands()

        assert robotic_code_repr_service.codes == [
            "0000",
            "0001",
            "0010",
            "0011",
            "010",
            "011",
            "100",
            "101",
            "110",
            "111",
        ]

    def test_get_code_when_many_exercises_commands_insert(
        self, robotic_code_repr_service
    ):
        COMMANDS_STORE["commands"] = ["UP", "UP", "UP", "DOWN", "DOWN", "RIGHT"]
        robotic_code_repr_service.create_codes_from_commands()
        assert robotic_code_repr_service.get_code("RIGHT") == "00"

        COMMANDS_STORE["commands"] += ["DOWN", "DOWN", "RIGHT", "GRAB"]
        robotic_code_repr_service.create_codes_from_commands()
        assert robotic_code_repr_service.get_code("RIGHT") == "01"

        COMMANDS_STORE["commands"] += ["LEFT", "LEFT", "DROP"]
        robotic_code_repr_service.create_codes_from_commands()
        assert robotic_code_repr_service.get_code("RIGHT") == "010"
