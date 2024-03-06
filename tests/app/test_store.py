from app.store import COMMANDS_STORE, get_sorted_commands_counter


def test_get_commands_counter_empty_commands():
    COMMANDS_STORE["commands"] = []

    sorted_counter = get_sorted_commands_counter()

    assert sorted_counter == []


def test_get_sorted_commands_counter_single_command():
    COMMANDS_STORE["commands"] = ["UP"]

    sorted_counter = get_sorted_commands_counter()
    assert sorted_counter == ["UP"]


def test_get_sorted_commands_counter_multiple_same_commands():
    COMMANDS_STORE["commands"] = ["UP", "UP", "UP", "UP"]

    sorted_counter = get_sorted_commands_counter()

    assert sorted_counter == ["UP"]


def test_get_sorted_commands_counter_multiple_different_commands():
    COMMANDS_STORE["commands"] = ["UP", "UP", "UP", "LEFT", "DOWN", "DOWN"]

    sorted_counter = get_sorted_commands_counter()

    assert sorted_counter == ["LEFT", "DOWN", "UP"]
