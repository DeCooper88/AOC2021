from typing import List


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [list(x.strip()) for x in f.readlines()]


def compute_p1(data: List) -> int:
    t = [list(i) for i in zip(*data)]
    most = ""
    least = ""
    for x in t:
        zeros = x.count("0")
        ones = x.count("1")
        if zeros > ones:
            most += "0"
            least += "1"
        elif zeros < ones:
            most += "1"
            least += "0"
        else:
            most += "666"
            least += "666"
    return int(most, 2) * int(least, 2)


def oxygen_generator(data: List) -> int:
    all_rows = [x for x in range(len(data))]
    remaining = all_rows
    col = 0
    while len(remaining) > 1:
        # print("col = ", col)
        # print("remaining = ", remaining)
        cur_col = [data[row][col] if row in remaining else "X" for row in all_rows]
        zeros = [i for i, x in enumerate(cur_col) if x == "0"]
        ones = [i for i, x in enumerate(cur_col) if x == "1"]
        # print("zeros = ", zeros)
        # print("ones = ", ones)
        if len(zeros) > len(ones):
            remaining = zeros
        else:
            remaining = ones
        col += 1
    return int("".join(data[remaining[0]]), 2)


def carbon_scrubber(data: List) -> int:
    all_rows = [x for x in range(len(data))]
    remaining = all_rows
    col = 0
    while len(remaining) > 1:
        # print("col = ", col)
        # print("remaining = ", remaining)
        cur_col = [data[row][col] if row in remaining else "X" for row in all_rows]
        zeros = [i for i, x in enumerate(cur_col) if x == "0"]
        ones = [i for i, x in enumerate(cur_col) if x == "1"]
        # print("zeros = ", zeros)
        # print("ones = ", ones)
        if len(ones) < len(zeros):
            remaining = ones
        else:
            remaining = zeros
        col += 1
    return int("".join(data[remaining[0]]), 2)


def compute_p2(data: List) -> int:
    oxygen = oxygen_generator(data)
    carbon = carbon_scrubber(data)
    return oxygen * carbon


e1 = get_input("examples/e2021_03.txt")
assert compute_p1(e1) == 198
assert compute_p2(e1) == 230

day3 = get_input("inputs/2021_03.txt")
p1 = compute_p1(day3)
p2 = compute_p2(day3)
print("answer part 1 = ", p1)
print("answer part 2 = ", p2)
