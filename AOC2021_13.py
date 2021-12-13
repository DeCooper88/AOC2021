from typing import List, Tuple


def get_input(data_file: str) -> Tuple:
    """Read data file and return as list."""
    with open(data_file) as f:
        d, f = f.read().split("\n\n")
        dots = []
        for x in d.split():
            x, y = x.split(',')
            dots.append((int(x), int(y)))
        folds = []
        for y in f.split('\n'):
            w1, w2, fold = y.split()
            axis, value = fold.split('=')
            folds.append((axis, int(value)))
        return dots, folds


class Origami:
    def __init__(self, dots, folds):
        self.dots = {(row, col) for col, row in dots}
        self.folds = folds
        self.folds_made = 0

    def fold_up(self, fold_line):
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

    def fold_left(self, fold_line):
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

    def fold_once(self):
        cur_fold = self.folds[self.folds_made]
        axis, line = cur_fold
        if axis == 'y':
            self.fold_up(line)
        else:
            self.fold_left(line)
        self.folds_made += 1

    def fold_all(self):
        for fold in self.folds:
            axis, line = fold
            if axis == 'y':
                self.fold_up(line)
            else:
                self.fold_left(line)

    def grid_size(self):
        max_row = 0
        max_col = 0
        for dot in self.dots:
            row, col = dot
            if row > max_row:
                max_row = row
            if col > max_col:
                max_col = col
        return max_row + 1, max_col + 1

    def display(self):
        rows, cols = self.grid_size()
        row = ['.' for _ in range(cols)]
        grid = [row.copy() for _ in range(rows)]
        for dot in self.dots:

            row, col = dot
            grid[row][col] = '#'
        display = ""
        for row in grid:
            line = "".join(row) + "\n"
            display += line
        return display


e1 = get_input('examples/e2021_13.txt')
# print(e1)
e1d, e1f = e1
ex1 = Origami(e1d, e1f)
# print(ex1)
# print(ex1.dots)
# print(ex1.folds)

# ex1.fold_once()
# print(ex1.grid_size())
# print()
ex1.fold_all()
print(ex1.display())
# print('example =', len(ex1.dots))


d13 = get_input('inputs/2021_13.txt')
day13_dots, day13_folds = d13
day13 = Origami(day13_dots, day13_folds)
# day13.fold_once()
# print('part 1 =', len(day13.dots))
day13.fold_all()
print(day13.display())
