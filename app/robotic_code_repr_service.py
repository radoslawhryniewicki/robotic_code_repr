from app.exceptions import InsufficientCounterLength
from app.store import get_sorted_commands_counter


class RoboticCodeReprService:
    def __init__(self) -> None:
        self.codes = []

    @property
    def sorted_commands_counter(self):
        return get_sorted_commands_counter()

    @staticmethod
    def _insert_new_codes(temp_list: list[str]) -> list[str]:
        shortest_code = min(temp_list, key=len)
        shortest_code_index = temp_list.index(shortest_code)
        temp_list.pop(shortest_code_index)
        temp_list.insert(shortest_code_index, f"{shortest_code}0")
        temp_list.insert(shortest_code_index + 1, f"{shortest_code}1")
        return temp_list

    @staticmethod
    def _codes_lists_have_different_length(
        left_codes: list[str], right_codes: list[str]
    ) -> bool:
        return len(left_codes) != len(right_codes)

    @staticmethod
    def _all_codes_have_same_length_in(left_codes: list[str]) -> bool:
        return all(len(code) == len(left_codes[0]) for code in left_codes)

    def create_codes_from_commands(self) -> None:
        counter_length = len(self.sorted_commands_counter)

        if counter_length <= 1:
            raise InsufficientCounterLength()

        left_codes = ["0"]
        right_codes = ["1"]

        while len(self.codes) < counter_length:
            if self._codes_lists_have_different_length(
                left_codes, right_codes
            ) and self._all_codes_have_same_length_in(left_codes):
                right_codes = self._insert_new_codes(right_codes)
            else:
                left_codes = self._insert_new_codes(left_codes)

            self.codes = left_codes + right_codes

    def get_code(self, command: str) -> str:
        assigned_codes = dict(zip(self.sorted_commands_counter, self.codes))
        return assigned_codes[command]
