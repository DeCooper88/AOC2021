from typing import List
from collections import Counter


def get_input(data_file: str) -> List:
    """Read data file and return as list."""
    with open(data_file) as f:
        return [int(x.strip()) for x in f.read().split(",")]


def compute_p1(data, days):
    fish = data.copy()
    # population = len(fish)
    for day in range(days):
        # print(day)
        population = len(fish)
        new_born = 0
        for i in range(population):
            if fish[i] == 0:
                new_born += 1
                fish[i] = 6
            else:
                fish[i] -= 1
        new_fish = [8 for x in range(new_born)]
        fish.extend(new_fish)
        print(day + 1, len(fish))
        print(fish[:5])
    return len(fish)


def compute_p2(data, days):
    fish = data.copy()
    population = len(data)
    birth_registry = Counter()
    for day in range(days):
        kids = 0
        for i in range(len(data)):
            if fish[i] == 0:
                kids += 1
                fish[i] = 6
            else:
                fish[i] -= 1
        if kids:
            birth_registry[day + 9] += kids
        grandkids = birth_registry[day]
        if grandkids:
            birth_registry[day + 7] += grandkids
            birth_registry[day + 9] += grandkids
        population += kids + grandkids
    return population


if __name__ == "__main__":
    e1 = [3, 4, 3, 1, 2]
    assert compute_p2(e1, 80) == 5934
    assert compute_p2(e1, 256) == 26984457539

    day6 = get_input("inputs/2021_06.txt")
    print("p1 =", compute_p2(e1, 256))
    print("p2 =", compute_p2(day6, 256))
