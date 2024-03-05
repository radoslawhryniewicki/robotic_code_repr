from fastapi import HTTPException
from store import COMMANDS_STORE
from collections import Counter


class RCRS():
    def __init__(self) -> None:
        self._rcrs = None

    @staticmethod
    def _get_commands_counter() -> Counter:
        counter = Counter(COMMANDS_STORE['commands'])
        print(f"{counter = }")
        sorted_counter = sorted(counter, key=counter.get)
        print(f"{sorted_counter = }")
        return sorted_counter
    
    @staticmethod
    def _insert_new_rcrs(sublist: list[str]) -> list[str]:
        shortest_rcr = min(sublist, key=len)
        shortest_rcr_index = sublist.index(shortest_rcr)

        sublist.pop(shortest_rcr_index)
        sublist.insert(shortest_rcr_index, f'{shortest_rcr}0')
        sublist.insert(shortest_rcr_index + 1, f'{shortest_rcr}1')
        return sublist

    def create(self):
        commands_counter = self._get_commands_counter()
        counter_length = len(commands_counter)
        all_rcrs = ["0","1"]

        if counter_length < 2:
            raise HTTPException(status_code=400, detail="You must provide at least 2 unique commands to generate RCRs")
        else:
            while counter_length != len(all_rcrs):
                half = len(all_rcrs) // 2
                if len(all_rcrs) % 2 == 0: 
                    left_rcrs = all_rcrs[:half] 
                    right_rcrs = all_rcrs[half:] 
                    left_rcrs = self._insert_new_rcrs(left_rcrs)
                else:
                    left_rcrs = all_rcrs[:half+1]
                    right_rcrs = all_rcrs[half+1:]
                    right_rcrs = self._insert_new_rcrs(right_rcrs)

                all_rcrs = left_rcrs + right_rcrs
        self._rcrs = all_rcrs

    
    def get_rcr_for(self, command: str) -> str:
        commands_counter = self._get_commands_counter()
        assigned_rcrs = dict(zip(commands_counter, self._rcrs))
        try:
            return assigned_rcrs[command]
        except KeyError:
            raise HTTPException(status_code=404, detail='No such command in commands')
