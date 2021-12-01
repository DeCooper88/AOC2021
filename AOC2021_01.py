from typing import List


def get_input(data_file: str) -> List[int]:
    """Read data file and return as list of integers."""
    with open(data_file) as f:
        return [int(x.strip()) for x in f.readlines()]


def compute(data: List, sample_size: int = 1) -> int:
    deeper = 0
    for depth in range(sample_size, len(data)):
        if data[depth - sample_size] < data[depth]:
            deeper += 1
    return deeper


e1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
day1 = get_input("inputs/2021_01.txt")

print("test p1 =", compute(e1))
print("test p2 =", compute(e1, sample_size=3))
print("answer p1 =", compute(day1))
print("answer p2 =", compute(day1, sample_size=3))
