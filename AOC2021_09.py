from typing import List, Tuple
from collections import deque
import math

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def get_input(data_file: str) -> List:
    with open(data_file) as f:
        grid = []
        for line in f.readlines():
            row = [int(x) for x in line.strip()]
            grid.append(row)
    return grid


class LavaCave:
    def __init__(self, map):
        self.map = map
        self.east_edge = len(map[0])
        self.south_edge = len(map)

    def lowest_neighbour(self, location: Tuple) -> int:
        """Find neighbour with lowest height."""
        row, col = location
        height = self.map[row][col]
        neighbours = []
        for direction in DIRECTIONS:
            ns, ew = direction
            new_row = row + ns
            new_col = col + ew
            if 0 <= new_row < self.south_edge and 0 <= new_col < self.east_edge:
                neighbours.append(self.map[new_row][new_col])
        return height < min(neighbours)

    @property
    def low_points(self):
        low_points = []
        for row in range(self.south_edge):
            for col in range(self.east_edge):
                if self.lowest_neighbour((row, col)):
                    low_points.append((row, col))
        return low_points

    def compute_p1(self):
        lowest = [self.map[row][col] for row, col in self.low_points]
        return sum(lowest) + (len(lowest) * 1)

    def get_neighbours(self, location):
        neighbours = []
        row, col = location
        for direction in DIRECTIONS:
            ns, ew = direction
            new_row = row + ns
            new_col = col + ew
            if 0 <= new_row < self.south_edge and 0 <= new_col < self.east_edge:
                neighbours.append((new_row, new_col))
        return neighbours

    def size_basin(self, location):
        basin = 0
        frontier = deque()
        frontier.append(location)
        seen = set()
        while frontier:
            cur_loc = frontier.popleft()
            row, col = cur_loc
            seen.add(cur_loc)
            if self.map[row][col] < 9:
                basin += 1
            neighbours = self.get_neighbours(cur_loc)
            for nb in neighbours:
                if nb in seen:
                    continue
                r, c = nb
                if self.map[r][c] < 9:
                    frontier.append(nb)
                    seen.add(nb)
        return basin

    def compute_p2(self):
        basins = []
        for low in self.low_points:
            basins.append(self.size_basin(low))
        largest = sorted(basins, reverse=True)[:3]
        return math.prod(largest)


e1 = get_input("examples/e2021_09.txt")
t1 = LavaCave(e1)
assert t1.compute_p1() == 15
assert t1.compute_p2() == 1134

day9 = get_input("inputs/2021_09.txt")
# print(day9)
d1 = LavaCave(day9)
print("day 9 part 1 =", d1.compute_p1())
print("day 9 part 2 =", d1.compute_p2())
