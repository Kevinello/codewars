from typing import List
from functools import reduce


def create_phone_number(n: List[int]):
    join = lambda x, y: x+str(y)
    return f'({reduce(join, n[0:3], "")}) {reduce(join, n[3:6], "")}-{reduce(join, n[6:], "")}'