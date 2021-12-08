from typing import List, Dict


def get_input(data_file: str) -> List:
    """Read data file and return as list of lists."""
    with open(data_file) as f:
        raw = [x.strip() for x in f.readlines()]
        return [y.split(" | ") for y in raw]


def compute_p1(data: List) -> int:
    """Answer part 1."""
    lengths = {2, 3, 4, 7}
    matches = 0
    for line in data:
        _, raw_outputs = line
        matches += sum([1 for x in raw_outputs.split() if len(x) in lengths])
    return matches


def find_numbers(data: str) -> Dict:
    """Map unique signal patterns to integers and return as dictionary."""
    all_charsets = data.split()
    lengths_dict = {2: 1, 3: 7, 4: 4, 7: 8}
    translator = dict()
    for charset in all_charsets:
        if len(charset) in lengths_dict:
            translator[charset] = lengths_dict[len(charset)]
    helper_dict = {v: k for k, v in translator.items()}

    # find all charsets of length 6
    sixes = [c for c in all_charsets if len(c) == 6]
    seven = set(helper_dict[7])
    four = set(helper_dict[4])
    sixes_seen = set()
    for i, six in enumerate(sixes):
        # find the 6, which can NOT contain all chars of 7
        if not seven.issubset(set(six)):
            translator[six] = 6
            sixes_seen.add(i)
        # find the 9, which WILL contain all chars of 7
        if four.issubset(set(six)):
            translator[six] = 9
            sixes_seen.add(i)
    # the last remaining six should be 0
    last_six = {0, 1, 2} - sixes_seen
    translator[sixes[last_six.pop()]] = 0

    # find all charsets of length 5
    fives = [c for c in all_charsets if len(c) == 5]
    three_index = None
    for j, five in enumerate(fives):
        # find the 3, which WILL contain all chars of 7
        if seven.issubset(five):
            translator[five] = 3
            three_index = j

    # refresh helper dict
    helper_dict = {v: k for k, v in translator.items()}
    # find top_right, which is diff between charsets 6 and 8
    top_right_set = set(helper_dict[8]) - set(helper_dict[6])
    top_raw_outputs = top_right_set.pop()
    # find the two fives that are left after finding 3
    fives_left = [fives[y] for y in range(3) if y != three_index]
    for char_set in fives_left:
        # if char_set contains top_raw_outputs it must be 2
        if top_raw_outputs in set(char_set):
            translator[char_set] = 2
        # if not then it must be five
        else:
            translator[char_set] = 5
    sorted_translator = {"".join(sorted(k)): v for k, v in translator.items()}
    return sorted_translator


def translate(signal):
    """
    Beginnings of a better function to translate the signal
    patterns into integers.
    """
    lengths_dict = {2: 1, 3: 7, 4: 4, 7: 8}
    pattern_to_int = dict()
    for pattern in signal.split():
        if len(pattern) in lengths_dict:
            pattern_to_int[pattern] = lengths_dict[len(pattern)]
    int_to_pattern = {v: k for k, v in pattern_to_int.items()}
    # top element is char that is in 7, but not in 1.
    diff_seven_one = set(int_to_pattern[7]) - set(int_to_pattern[1])
    top = diff_seven_one.pop()
    return pattern_to_int


def compute_p2(data: List) -> int:
    """Answer part 2."""
    total_output = 0
    for row in data:
        output = ""
        signal_patterns, raw_outputs = row
        mapper = find_numbers(signal_patterns)
        for code in raw_outputs.split():
            sorted_code = "".join(sorted(code))
            output += str(mapper[sorted_code])
        total_output += int(output)
    return total_output


# t1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
# print(translate(t1))
# print()

e1 = get_input("examples/e2021_08.txt")
assert compute_p1(e1) == 26
assert compute_p2(e1) == 61229


day8 = get_input("inputs/2021_08.txt")
print("day 8 part 1 =", compute_p1(day8))
print("day 8 part 2 =", compute_p2(day8))
