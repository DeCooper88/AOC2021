from typing import Deque, List, Tuple
from collections import deque
import math

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # East, South, West, North


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        grid = []
        for line in f.readlines():
            row = [int(x) for x in line.strip()]
            grid.append(row)
    return grid


class LavaCave:
    def __init__(self, grid: List):
        self.grid = grid
        self.east_edge = len(grid[0])
        self.south_edge = len(grid)

    def get_neighbours(self, location: Tuple) -> List:
        """
        Return all neighbours that are to the east, south, north or west of
        the location.
        """
        neighbours = []
        row, col = location
        for direction in DIRECTIONS:
            ns, ew = direction
            new_row = row + ns
            new_col = col + ew
            if 0 <= new_row < self.south_edge and 0 <= new_col < self.east_edge:
                neighbours.append((new_row, new_col))
        return neighbours

    @property
    def low_points(self) -> List:
        """
        Return all low points. These are locations that are lower than any of
        its adjacent locations.
        """
        low_points = []
        for row in range(self.south_edge):
            for col in range(self.east_edge):
                height = self.grid[row][col]
                neighbours = self.get_neighbours((row, col))
                heights = [self.grid[r][c] for r, c in neighbours]
                if height < min(heights):
                    low_points.append((row, col))
        return low_points

    def size_basin(self, low_point: Tuple) -> int:
        """
        Return size of basin. Uses breadth first search to determine the size
        of the basin.
        """
        basin = 0
        frontier: Deque = deque()
        frontier.append(low_point)
        seen = {low_point}
        while frontier:
            location = frontier.popleft()
            row, col = location
            if self.grid[row][col] < 9:
                basin += 1
            neighbours = self.get_neighbours(location)
            for nb in neighbours:
                if nb in seen:
                    continue
                r, c = nb
                if self.grid[r][c] < 9:
                    frontier.append(nb)
                    seen.add(nb)
        return basin

    def compute_p1(self) -> int:
        """
        Return the sum of the risk levels of all low points. Risk level is
        height + 1. Answer part 1.
        """
        all_lows = [self.grid[row][col] for row, col in self.low_points]
        return sum(all_lows) + (len(all_lows) * 1)

    def compute_p2(self) -> int:
        """
        Return the product of the sizes of the largest 3 basins. Answer
        part 2.
        """
        basins = []
        for low in self.low_points:
            basins.append(self.size_basin(low))
        largest = sorted(basins, reverse=True)[:3]
        return math.prod(largest)


if __name__ == "__main__":
    e1 = get_input("examples/e2021_09.txt")
    t1 = LavaCave(e1)
    assert t1.compute_p1() == 15
    assert t1.compute_p2() == 1134

    day9 = get_input("inputs/2021_09.txt")
    d1 = LavaCave(day9)
    print("day 9 part 1 =", d1.compute_p1())
    print("day 9 part 2 =", d1.compute_p2())
