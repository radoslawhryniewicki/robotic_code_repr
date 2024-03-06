from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.models import RoboticCode
from app.store import COMMANDS_STORE

test_client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_commands_store():
    COMMANDS_STORE["commands"] = []
    yield


def test_add_command_at_start():
    test_client.post("/commands/", json={"commands": ["UP"]})

    assert len(COMMANDS_STORE["commands"]) == 1


def test_add_multiple_commands_at_start():
    test_client.post("/commands/", json={"commands": ["UP", "UP", "DOWN", "LEFT"]})

    assert len(COMMANDS_STORE["commands"]) == 4


def test_add_multiple_commands_in_session():
    test_client.post("/commands/", json={"commands": ["UP", "UP", "DOWN", "LEFT"]})
    test_client.post("/commands/", json={"commands": ["UP", "UP", "DOWN", "LEFT"]})

    assert len(COMMANDS_STORE["commands"]) == 8


def test_get_code_raise_404_when_proper_command_not_exist_in_store():
    test_client.post("/commands/", json={"commands": ["UP", "RIGHT", "LEFT"]})

    response = test_client.get("/rcrs/DOWN")

    assert response.status_code == 404
    assert response.json() == {"detail": "No such command in commands"}


def test_get_code_raise_422_when_invalid_command():
    test_client.post("/commands/", json={"commands": ["UP", "RIGHT", "LEFT"]})

    response = test_client.get("/rcrs/STH")

    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Input should be 'UP', 'DOWN', 'RIGHT', 'LEFT', 'DROP' or 'GRAB'"
    )


@pytest.mark.parametrize("commands", [[], ["UP"]])
def test_get_code_raise_400_when_added_only_single_command(commands):
    test_client.post("/commands/", json={"commands": commands})

    response = test_client.get("/rcrs/DOWN")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "You must provide at least 2 unique commands to generate RCRs"
    }


def test_get_code():
    commands = ["UP", "UP", "UP", "DOWN", "DOWN", "RIGHT", "DROP", "GRAB"]
    test_client.post("/commands/", json={"commands": commands})

    response = test_client.get("/rcrs/DOWN")

    assert response.status_code == 200
    assert response.json() == {"rcr": "10"}
