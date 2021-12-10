from typing import List, Deque
from collections import deque


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [x.strip() for x in f.readlines()]


def check(chunk: str) -> int:
    stack: Deque = deque()
    openers = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closers = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for char in chunk:
        if char in openers:
            stack.append(char)
        else:
            left = stack.pop()
            right = openers[left]
            if right != char:
                return closers[char]
    return 0


def compute_p1(data: List) -> int:
    score = 0
    for chunk in data:
        score += check(chunk)
    return score


def correct_chunks(data: List) -> List:
    correct = []
    for chunk in data:
        if check(chunk) == 0:
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
    complete_string = ""
    while stack:
        complete_string += openers[stack.pop()]
    score = 0
    for char in complete_string:
        score *= 5
        score += scores[char]
    return score


def compute_p2(data: List) -> int:
    correct_lines = correct_chunks(data)
    all_scores = []
    for line in correct_lines:
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
