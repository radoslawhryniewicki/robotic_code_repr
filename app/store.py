from collections import Counter


COMMANDS_STORE = {"commands": []}


def get_sorted_commands_counter() -> Counter:
    counter = Counter(COMMANDS_STORE["commands"])
    return sorted(counter, key=counter.get)
