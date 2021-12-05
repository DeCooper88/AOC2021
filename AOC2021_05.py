from typing import List, Counter
from collections import Counter


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = [x.strip() for x in f.readlines()]
        lines = []
        for entry in raw:
            left, right = entry.split(" -> ")
            lc, lr = left.split(",")
            rc, rr = right.split(",")
            lines.append(((int(lc), int(lr)), (int(rc), int(rr))))
    return lines


def compute(data: List, count_diagonals=False) -> int:
    """
    Return number  of line crossing > 1. By default the function ignores
    diagonals, which is the answer for part 1. To get the answer for part
    set count_diagonals to True.
    """
    doubles: Counter = Counter()
    for lines in data:
        left, right = lines
        lc, lr = left
        rc, rr = right

        if lc == rc:
            sp = min(lr, rr)
            ep = max(lr, rr) + 1
            for i in range(sp, ep):
                doubles[(lc, i)] += 1

        elif lr == rr:
            sp = min(lc, rc)
            ep = max(lc, rc) + 1
            for i in range(sp, ep):
                doubles[(i, lr)] += 1

        else:
            if not count_diagonals:
                continue
            col_step = 1 if lc < rc else -1
            row_step = 1 if lr < rr else -1
            cols = range(lc, rc + col_step, col_step)
            rows = range(lr, rr + row_step, row_step)
            points = [(col, row) for col, row in zip(cols, rows)]
            for point in points:
                doubles[point] += 1

    crossings = [1 for x in doubles.values() if x > 1]
    return sum(crossings)


if __name__ == "__main__":
    e1 = get_input("examples/e2021_05.txt")
    assert compute(e1) == 5
    assert compute(e1, count_diagonals=True) == 12

    day5 = get_input("inputs/2021_05.txt")
    print("answer part 1 =", compute(day5))
    print("answer part 2 =", compute(day5, count_diagonals=True))
