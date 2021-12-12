from typing import List, Tuple


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = [x.strip() for x in f.readlines()]
        grid = []
        for line in raw:
            row = [int(x) for x in line]
            grid.append(row)
    return grid


class Octopuses:
    successors = ((0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1))

    def __init__(self, grid: List):
        self.grid = grid
        self.east_edge = len(grid[0])
        self.south_edge = len(grid)

    def get_neighbours(self, location: Tuple) -> List:
        """
        Return all neighbours that are to the E, SE, S, SW, W, NW, N, NE of
        the location.
        """
        neighbours = []
        row, col = location
        for direction in self.successors:
            ns, ew = direction
            new_row = row + ns
            new_col = col + ew
            if 0 <= new_row < self.south_edge and 0 <= new_col < self.east_edge:
                neighbours.append((new_row, new_col))
        return neighbours

    def increase_energy_all(self):
        for row in range(self.south_edge):
            for col in range(self.east_edge):
                self.grid[row][col] += 1

    def increase_energy(self, locations):
        for loc in locations:
            row, col = loc
            self.grid[row][col] += 1

    def flash_locations(self):
        locations = []
        for row_no, row in enumerate(self.grid):
            locs = [(row_no, col) for col, val in enumerate(row) if val == 10]
            locations.extend(locs)
        return locations

    @property
    def count_flashes(self):
        flashes = 0
        for row in self.grid:
            flashes += sum([1 for x in row if x > 9])
        return flashes

    def process_round(self):
        flashes = 0
        self.increase_energy_all()
        has_flashed = set()
        for x in range(99):
            flash_locs = self.flash_locations()
            print(x, flash_locs)
            print(self.grid)
            if not flash_locs:
                break
            all_neighbours = []
            for loc in flash_locs:
                # has_flashed.add(loc)
                nbs = self.get_neighbours(loc)
                # all_neighbours.extend(nbs)
                for nb in nbs:
                    if nb not in has_flashed:
                        all_neighbours.append(nb)
            self.increase_energy(all_neighbours)
        return self.count_flashes

    def play_round(self):
        # increase energy full grid by 1
        self.increase_energy_all()
        # find all locations that flash
        self.flash_locations()
        return self.flash_locations()


# e1 = get_input("examples/e2021_11a.txt")
# ex1 = Octopuses(e1)
# print(ex1.grid)
# print()
# # print(ex1.successors)
# # print(ex1.get_neighbours((3, 3)))
# ex1.increase_energy_all()
# ex1.increase_energy_all()
# print(ex1.grid)
# print(ex1.count_flashes)
# print(ex1.flash_locations())


e1b = get_input('examples/e2021_11b.txt')
ex2 = Octopuses(e1b)
# print(ex2.grid)
# ex2.increase_energy_all()
# print(ex2.grid)
print(ex2.play_round())
print(ex2.grid)
