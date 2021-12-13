from typing import Deque, List, Tuple
from collections import deque


def get_input(data_file: str) -> Tuple:
    """Read data file and return as list."""
    with open(data_file) as f:
        d, f = f.read().split("\n\n")
        dots = []
        for x in d.split():
            x, y = x.split(",")
            dots.append((int(x), int(y)))
        folds = []
        for y in f.split("\n"):
            w1, w2, fold = y.split()
            axis, value = fold.split("=")
            folds.append((axis, int(value)))
        return dots, folds


class Origami:
    def __init__(self, dots: List, folds: List):
        self.dots = {(row, col) for col, row in dots}
        self.folds: Deque = deque(folds)

    def fold_up(self, fold_line: int):
        new_paper = set()
        for dot in self.dots:
            row, col = dot
            if row < fold_line:
                new_paper.add(dot)
            elif row > fold_line:
                new_row = (fold_line * 2) - row
                new_dot = (new_row, col)
                new_paper.add(new_dot)
        self.dots = new_paper

    def fold_left(self, fold_line: int):
        # TODO: merge this method and fold_up method
        new_paper = set()
        for dot in self.dots:
            row, col = dot
            if col < fold_line:
                new_paper.add(dot)
            elif col > fold_line:
                new_col = (fold_line * 2) - col
                new_dot = (row, new_col)
                new_paper.add(new_dot)
        self.dots = new_paper

    def make_folds(self, fold_one=False):
        """
        Adjust dots for every fold. Processes all folds by default, but only
        one if fold_one is set to True. Set fold_one to True to calculate the
        answer for part 1. Method will only process the remaining folds.
        """
        folds = 1 if fold_one else len(self.folds)
        for fold in range(folds):
            axis, line = self.folds.popleft()
            if axis == "y":
                self.fold_up(line)
            else:
                self.fold_left(line)

    @property
    def grid_size(self) -> Tuple:
        """Return grid size required to hold all dots."""
        max_row = 0
        max_col = 0
        for dot in self.dots:
            row, col = dot
            if row > max_row:
                max_row = row
            if col > max_col:
                max_col = col
        return max_row + 1, max_col + 1

    def display(self) -> str:
        """Return visualization of Origami."""
        rows, cols = self.grid_size
        row = [" " for _ in range(cols)]
        grid = [row.copy() for _ in range(rows)]
        for dot in self.dots:
            row, col = dot
            grid[row][col] = "#"
        display = ""
        for row in grid:
            line = "".join(row) + "\n"
            display += line
        return display


e1 = get_input("examples/e2021_13.txt")
e1d, e1f = e1
ex1 = Origami(e1d, e1f)
ex1.make_folds(fold_one=True)
ex1_p1 = len(ex1.dots)
ex1.make_folds()

d13 = get_input("inputs/2021_13.txt")
day13_dots, day13_folds = d13
day13 = Origami(day13_dots, day13_folds)
day13.make_folds(fold_one=True)
day13_p1 = len(day13.dots)
day13.make_folds()

print("example =", ex1_p1)
print("part 1 =", day13_p1)
print()
print(ex1.display())
print(day13.display())
