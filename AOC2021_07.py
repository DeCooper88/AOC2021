from typing import List


def get_input(crabs_file: str) -> List[int]:
    """Read crabs file and return as list."""
    with open(crabs_file) as f:
        return [int(x.strip()) for x in f.read().split(",")]


def compute_p1(crabs: List) -> int:
    """
    Find the horizontal position that the crabs can align to using the least
    fuel possible. Return the amount of fuel needed. Solution for part 1.
    """
    lowest_fuel = sum(crabs) * max(crabs)
    for position in crabs:
        fuel = 0
        for crab in crabs:
            fuel += abs(position - crab)
        if fuel < lowest_fuel:
            lowest_fuel = fuel
    return lowest_fuel


def compute_p2(crabs: List) -> int:
    """
    Find the horizontal position that the crabs can align to using the least
    fuel possible. The fuel consumption increases by 1 every step. Return
    the amount of fuel needed. The algorithm uses Gauss formula for calculating
    the sum of consecutive numbers. Solution for part 2.
    """
    lowest_fuel = sum(crabs) * max(crabs)
    start, end = min(crabs), max(crabs) + 1
    for position in range(start, end):
        fuel = 0
        for crab in crabs:
            if fuel > lowest_fuel:
                break
            steps = abs(crab - position)
            fuel += (steps / 2) * (1 + steps)  # Gauss sum consecutive numbers
        if fuel < lowest_fuel:
            lowest_fuel = fuel
    return int(lowest_fuel)


if __name__ == "__main__":
    e1 = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert compute_p1(e1) == 37
    assert compute_p2(e1) == 168

    day7 = get_input("inputs/2021_07.txt")
    print("day 7 part 1 =", compute_p1(day7))
    print("day 7 part 2 =", compute_p2(day7))
