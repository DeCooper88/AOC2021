from typing import List, Deque, Tuple
from collections import Counter, deque


def get_input(data_file: str) -> Tuple:
    """Read data file and return as list."""
    with open(data_file) as f:
        code, pairs = f.read().split("\n\n")
        pairs_dict = {}
        for pair in pairs.split("\n"):
            left, right = pair.split(" -> ")
            pairs_dict[left] = right
        return code, pairs_dict


def find_polymer(code, all_pairs, rounds):
    polymer = code
    for _ in range(rounds):
        insertions = {}
        offset = 0
        for i in range(1, len(polymer)):
            pair = polymer[i - 1 : i + 1]
            if pair in all_pairs:
                insertions[i + offset] = all_pairs[pair]
                offset += 1
        code_queue = deque(polymer)
        new_polymer = ""
        for i in range(len(polymer) + len(insertions)):
            if i in insertions:
                new_polymer += insertions[i]
            else:
                new_polymer += code_queue.popleft()
        polymer = new_polymer
    return polymer


def compute_p1(code, all_pairs, rounds):
    polymer = find_polymer(code, all_pairs, rounds)
    elements = {e for e in all_pairs.values()}
    pairs_counter = Counter()
    for e in polymer:
        if e in elements:
            pairs_counter[e] += 1
    return pairs_counter


e1 = get_input("examples/e2021_14.txt")
# print(e1)
e1c, e1p = e1
print(compute_p1(e1c, e1p, 10))
print()

day14 = get_input("inputs/2021_14.txt")
day14_code, day14_pairs = day14
print(compute_p1(day14_code, day14_pairs, 10))
