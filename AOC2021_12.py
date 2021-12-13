from typing import Counter, DefaultDict, Deque
from collections import defaultdict, deque, Counter


def get_input(data_file: str) -> DefaultDict:
    """Read data file and return as list."""
    with open(data_file) as f:
        raw = [x.strip() for x in f.readlines()]
        # print(raw)
        pairs = defaultdict(list)
        for pair in raw:
            left, right = pair.split('-')
            # print(left, right)
            pairs[left].append(right)
            if right == 'end' or left == 'start':
                continue
            else:
                pairs[right].append(left)
        return pairs


def compute_p1(graph):
    valid_paths = []
    active_paths: Deque = deque()
    for child in graph['start']:
        route = ['start', child]
        active_paths.append(route)
    # for i in range(100):
    while active_paths:
        # print(active_paths)
        cur_path = active_paths.popleft()
        end_point = cur_path[-1]
        for child in graph[end_point]:
            new_path = cur_path.copy()
            new_path.append(child)
            if child == 'end':
                valid_paths.append(new_path)
                continue

            # part 1
            if child.islower() and child in cur_path:
                continue

            # # part 2
            # if child.islower():
            #     small_caves = [c for c in cur_path[1:] if c.islower()]
            #     if small_caves:
            #         visit_log: Counter = Counter(small_caves)
            #
            #         most_visited = visit_log.most_common(2)
            #         print(most_visited)
            #         most_visits = most_visited[0][1]
            #
            #         if most_visits > 2:
            #             print(visit_log)
            #             print('most_visits =', most_visits)
            #             continue
            #         if len(most_visited) > 1:
            #             second_most_visits = most_visited[1][1]
            #             print('second_most_visits =', second_most_visits)
            #             if second_most_visits > 1:
            #                 continue

            active_paths.append(new_path)
    print(len(valid_paths))
    return valid_paths


e1 = get_input("examples/e2021_12a.txt")
# print(e1)
# print()
e1_paths = compute_p1(e1)
# for p in sorted(e1_paths):
#     print(p)

day12 = get_input("inputs/2021_12.txt")
compute_p1(day12)
