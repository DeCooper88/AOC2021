from typing import List


def get_input(data_file: str) -> List[int]:
    """Read data file and return as list of integers."""
    with open(data_file) as f:
        return [int(x.strip()) for x in f.readlines()]


def compute(data: List, sample_size: int = 1) -> int:
    """
    Return number of times an observation is bigger than preceding observation.
    If sample_size > 1 it will compare groups of observations. When comparing
    groups (abc vs bcd) some observations (bc) will overlap and therefore only the
    non-overlapping observations (a and d) need to be compared.
    """
    bigger = 0
    for depth in range(sample_size, len(data)):
        if data[depth - sample_size] < data[depth]:
            bigger += 1
    return bigger


if __name__ == "__main__":
    e1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert compute(e1) == 7
    assert compute(e1, sample_size=3) == 5

    day1 = get_input("inputs/2021_01.txt")
    print("answer part 1 =", compute(day1))
    print("answer part 2 =", compute(day1, sample_size=3))
