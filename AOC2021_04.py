from typing import Tuple, List, Set
from collections import Counter


def get_input(data_file: str) -> Tuple[List, List]:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = f.read()
        numbers, *grids = raw.split("\n\n")
        draws = [int(number) for number in numbers.split(",")]
        players = [player.split("\n") for player in grids]
        clean_players = []
        for player in players:
            clean_rows = []
            for row in player:
                cr = [int(x.strip()) for x in row.strip().split()]
                clean_rows.append(cr)
            clean_players.append(clean_rows)
        return draws, clean_players


class Card:
    def __init__(self, uid, grid):
        self.uid: int = uid
        self.grid: List[List] = grid
        self.matches: int = 0  # number of times the card has a draw
        self.correct_rows = Counter()
        self.correct_cols = Counter()
        self.marked_sum: int = 0  # sum of all numbers that are marked

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
        """Return True if card has bingo."""
        if self.matches < 5:
            return False
        if self.correct_rows.most_common(1)[0][1] == 5:
            return True
        if self.correct_cols.most_common(1)[0][1] == 5:
            return True
        return False

    @property
    def unmarked_sum(self):
        """Calculate the sum of all unmarked numbers left on the card."""
        grid_sum = sum([sum(row) for row in self.grid])
        return grid_sum - self.marked_sum


class Game:
    def __init__(self, draws: List, cards: List):
        self.draws = draws
        self.cards = [Card(i, card) for i, card in enumerate(cards)]
        self.rounds_played = 0
        self.winners: Set[int] = set()

    def first_winner(self):
        """
        Find card that wins first. Return product of sum unmarked fields
        and last draw. This is solution for part 1.
        """
        for draw in self.draws:
            self.rounds_played += 1
            for card in self.cards:
                card.process_draw(draw)
                if card.bingo:
                    self.winners.add(card.uid)
                    return card.unmarked_sum * draw
        return "No card wins"

    def last_winner(self):
        """
        Find card that wins last. Return product of sum unmarked fields
        and last draw. This is solution for part 2.
        """
        for draw in self.draws[self.rounds_played :]:
            for card in self.cards:
                card.process_draw(draw)
                if card.bingo:
                    last_sum = card.unmarked_sum * draw
                    self.winners.add(card.uid)
                    if len(self.winners) == len(self.cards):
                        return last_sum
        return "Not everybody wins"


if __name__ == "__main__":
    e1_draws, e1_card = get_input("examples/e2021_04.txt")
    e1 = Game(e1_draws, e1_card)
    assert e1.first_winner() == 4512
    assert e1.last_winner() == 1924

    day4_draws, day4_players = get_input("inputs/2021_04.txt")
    day4 = Game(day4_draws, day4_players)
    print("part 1 =", day4.first_winner())
    print("part 2 =", day4.last_winner())
