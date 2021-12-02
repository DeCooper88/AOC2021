from typing import List, Tuple


def get_input(data_file: str) -> List[Tuple]:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [tuple(x.strip().split()) for x in f.readlines()]


def compute_p1(data: List[Tuple]) -> int:
    """
    Calculate position and depth based on list of instructions.
    Return product of position and depth. Solution for part 1.
    """
    position = depth = 0
    for instruction in data:
        move, value = instruction
        if move == "forward":
            position += int(value)
        elif move == "down":
            depth += int(value)
        elif move == "up":
            depth -= int(value)
    return position * depth


def compute_p2(data: List[Tuple]) -> int:
    """
    Calculate position and depth based on list of instructions.
    Return product of position and depth. Solution for part 2.
    """
    aim = position = depth = 0
    for instruction in data:
        move, value = instruction
        if move == "forward":
            position += int(value)
            depth += int(value) * aim
        elif move == "down":
            aim += int(value)
        elif move == "up":
            aim -= int(value)
    return position * depth


if __name__ == "__main__":
    e1 = get_input("examples/e2021_02.txt")
    assert compute_p1(e1) == 150
    assert compute_p2(e1) == 900

    day2 = get_input("inputs/2021_02.txt")
    print("solution part 1 =", compute_p1(day2))
    print("solution part 2 =", compute_p2(day2))
