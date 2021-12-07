from typing import List


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [int(x.strip()) for x in f.read().split(",")]


def compute_p1(data: List) -> int:
    """Solution part 1."""
    least_fuel = sum(data) * 1000
    for i, base in enumerate(data):
        fuel_cost = 0
        for pos in data:
            fuel_cost += abs(base - pos)
        if fuel_cost < least_fuel:
            least_fuel = fuel_cost
    return least_fuel


def compute_p2(data: List) -> int:
    """Solution part 2."""
    least_fuel = sum(data) * 1000
    smallest = min(data)
    biggest = max(data)
    for position in range(smallest, biggest + 1):
        fuel_cost = 0
        for crab in data:
            if fuel_cost > least_fuel:
                break
            distance = abs(crab - position)
            start = 1
            end = distance + 1
            fuel_cost += sum(range(start, end))
        if fuel_cost < least_fuel:
            least_fuel = fuel_cost
    return least_fuel


if __name__ == "__main__":
    e1 = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert compute_p1(e1) == 37
    assert compute_p2(e1) == 168

    day7 = get_input("inputs/2021_07.txt")
    print("day 7 part 1 =", compute_p1(day7))
    print("day 7 part 2 =", compute_p2(day7))
