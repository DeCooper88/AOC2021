from typing import List, Deque
from collections import deque


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [x.strip() for x in f.readlines()]


def corrupted_check(line: str) -> int:
    """
    Return error code if line is corrupted. Otherwise return 0. Lines are
    corrupted if opening characters are not matched with the right
    closing character.
    """
    stack: Deque = deque()
    openers = {"(": ")", "[": "]", "{": "}", "<": ">"}
    syntax_errors = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            left_char = stack.pop()
            right_char = openers[left_char]
            if right_char != char:
                return syntax_errors[char]
    return 0


def compute_p1(data: List) -> int:
    """
    Return 
    """
    score = 0
    for line in data:
        score += corrupted_check(line)
    return score


def incomplete_lines(data: List) -> List:
    correct = []
    for chunk in data:
        if corrupted_check(chunk) == 0:
            correct.append(chunk)
    return correct


def complete(chunk: str) -> int:
    stack: Deque = deque()
    openers = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    for char in chunk:
        if char in openers:
            stack.append(char)
        else:
            stack.pop()
    total_score = 0
    while stack:
        closer = openers[stack.pop()]
        total_score *= 5
        total_score += scores[closer]
    return total_score


def compute_p2(data: List) -> int:
    incomplete = incomplete_lines(data)
    all_scores = []
    for line in incomplete:
        result = complete(line)
        all_scores.append(result)
    middle = int(len(all_scores) / 2)
    return sorted(all_scores)[middle]


e1 = get_input("examples/e2021_10.txt")
assert compute_p1(e1) == 26397
assert compute_p2(e1) == 288957

day6 = get_input("inputs/2021_10.txt")
print("day 10 part 1 =", compute_p1(day6))
print("day 10 part 2 =", compute_p2(day6))
