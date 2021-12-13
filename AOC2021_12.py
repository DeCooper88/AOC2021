from typing import Counter, DefaultDict, Deque
from collections import defaultdict, deque, Counter


def get_input(data_file: str) -> DefaultDict:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = [x.strip() for x in f.readlines()]
        # print(raw)
        pairs = defaultdict(list)
        for pair in raw:
            left, right = pair.split("-")
            if right != "start":
                pairs[left].append(right)
            if right == "end" or left == "start":
                continue
            else:
                pairs[right].append(left)
        return pairs


def compute_p1(graph):
    valid_paths = []
    active_paths: Deque = deque()
    for child in graph["start"]:
        route = ["start", child]
        active_paths.append(route)
    # for i in range(100):
    while active_paths:
        # print(active_paths)
        cur_path = active_paths.popleft()
        end_point = cur_path[-1]
        for child in graph[end_point]:
            new_path = cur_path.copy()
            new_path.append(child)
            if child == "end":
                valid_paths.append(new_path)
                continue
            # TODO: Refactor function so it can solve par 1 AND part 2
            # # part 1
            # if child.islower() and child in cur_path:
            #     continue

            # part 2
            # print(new_path)
            if child.islower():
                small_caves = [c for c in new_path if c.islower()]
                visit_log: Counter = Counter(small_caves)
                # print(visit_log)

                most_visited = visit_log.most_common(2)
                # print(most_visited)
                more_than_two = most_visited[0][1] > 2
                two_twice = most_visited[1][1] > 1

                if more_than_two or two_twice:
                    continue

            active_paths.append(new_path)
    # print(valid_paths)
    return len(valid_paths)


e1 = get_input("examples/e2021_12a.txt")
# print(e1)
print(compute_p1(e1))

e2 = get_input("examples/e2021_12b.txt")
# print(e2)
print(compute_p1(e2))
print()

day12 = get_input("inputs/2021_12.txt")
print("calculating.....")
print("answer part 2 =", compute_p1(day12))
