from typing import Tuple, List
from collections import Counter


def get_input(data_file: str) -> Tuple[List, List]:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = f.read()
        numbers, *grids = raw.split("\n\n")
        draws = [int(number) for number in numbers.split(',')]
        players = [player.split('\n') for player in grids]
        clean_players = []
        for player in players:
            clean_rows = []
            for row in player:
                cr = [int(x.strip()) for x in row.strip().split()]
                clean_rows.append(cr)
            clean_players.append(clean_rows)
        return draws, clean_players


class Player:
    def __init__(self, uid, grid):
        self.uid: int = uid
        self.grid: List[List] = grid
        self.matches: int = 0  # number of times player marks a draw
        self.correct_rows = Counter()
        self.correct_cols = Counter()
        self.marked_sum: int = 0

    def process_draw(self, draw):
        """Process a draw."""
        for row_no, row in enumerate(self.grid):
            if draw in row:
                col_no = row.index(draw)
                self.matches += 1
                self.correct_rows[row_no] += 1
                self.correct_cols[col_no] += 1
                self.marked_sum += draw

    @property
    def bingo(self):
        """Return True if player has bingo"""
        if self.matches < 5:
            return False
        if self.correct_rows.most_common(1)[0][1] == 5:
            return True
        if self.correct_cols.most_common(1)[0][1] == 5:
            return True
        return False

    @property
    def unmarked_sum(self):
        """Calculate the sum of all unmarked numbers"""
        grid_sum = sum([sum(row) for row in self.grid])
        return grid_sum - self.marked_sum

    def __repr__(self):
        display = ""
        for row in self.grid:
            display += ", ".join([str(n) for n in row]) + "\n"
        return display


def compute_p1(draws, player_grids):
    players = [Player(i, grid) for i, grid in enumerate(player_grids)]
    for draw in draws:
        for player in players:
            player.process_draw(draw)
            if player.bingo:
                return player.unmarked_sum * draw
    return "No bingo"


def compute_p2(draws, player_grids):
    players = [Player(i, grid) for i, grid in enumerate(player_grids)]
    winners = set()
    for draw in draws:
        for player in players:
            player.process_draw(draw)
            if player.bingo:
                last_sum = player.unmarked_sum * draw
                winners.add(player.uid)
                if len(winners) == len(player_grids):
                    return last_sum
    return "Not everybody wins"


if __name__ == '__main__':
    e1_draws, e1_players = get_input("examples/e2021_04.txt")
    assert compute_p1(e1_draws, e1_players) == 4512
    assert compute_p2(e1_draws, e1_players) == 1924

    day4_draws, day4_players = get_input("inputs/2021_04.txt")
    print("part 1 =", compute_p1(day4_draws, day4_players))
    print("part 2 =", compute_p2(day4_draws, day4_players))
