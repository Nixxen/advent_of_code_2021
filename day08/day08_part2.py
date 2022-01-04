RUN_TEST = True
TEST_SOLUTION = 61229
TEST_INPUT_FILE = "test_input_day_08.txt"
INPUT_FILE = "input_day_08.txt"

ARGS = []


# Helper function to find the possible wire segments.
def detect_wires(digit, segment_dictionary) -> dict:
    if len(digit) == 2:
        # Upper right + bottom right.
        if not "c" in segment_dictionary:
            segment_dictionary["c"] = [digit[0], digit[1]]
        if not "f" in segment_dictionary:
            segment_dictionary["f"] = [digit[0], digit[1]]
    elif len(digit) == 3:
        # Upper middle wire + Upper right + bottom right.
        if not "a" in segment_dictionary:
            segment_dictionary["a"] = [digit[0], digit[1], digit[2]]
        if not "c" in segment_dictionary:
            segment_dictionary["c"] = [digit[0], digit[1], digit[2]]
        if not "f" in segment_dictionary:
            segment_dictionary["f"] = [digit[0], digit[1], digit[2]]
    elif len(digit) == 4:
        # Upper left + upper right + center + bottom right.
        if not "b" in segment_dictionary:
            segment_dictionary["b"] = [digit[0], digit[1], digit[2], digit[3]]
        if not "c" in segment_dictionary:
            segment_dictionary["c"] = [digit[0], digit[1], digit[2], digit[3]]
        if not "d" in segment_dictionary:
            segment_dictionary["d"] = [digit[0], digit[1], digit[2], digit[3]]
        if not "f" in segment_dictionary:
            segment_dictionary["f"] = [digit[0], digit[1], digit[2], digit[3]]
    elif len(digit) == 7:
        # Every wire
        for i in range(int("a"), int("g") + 1):
            if not chr(i) in segment_dictionary:
                segment_dictionary[chr(i)] = [
                    digit[0],
                    digit[1],
                    digit[2],
                    digit[3],
                    digit[4],
                    digit[5],
                    digit[6],
                ]
    return segment_dictionary


# Attempts to remove invalid wires from the pattern.
def correct_pattern(pattern) -> dict:
    changed = True
    while changed:
        changed = False
        # Correct the pattern to find overlapping wires that can be removed.
        for key, value in pattern.items():
            if len(value) == 1:
                # Remove the value from other wires.
                for key2, value2 in pattern.items():
                    if key != key2:
                        if value[0] in value2:
                            pattern[key2].remove(value[0])
                            changed = True
        # Check for wires that make up 7 and 1, to eliminate the overlap.
        if "a" in pattern:  # Top center wire.
            if "c" and "f" in pattern:
                # Check if values from 'c' and 'f' are overlapping with 0.
                for value in pattern.values():
                    if value in pattern["c"] or value in pattern["f"]:
                        pattern[0].remove(value)
                        changed = True

    return pattern


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 8 Part 2 - 7 segment decoder. For each entry, determine all of the
    # wire/segment connections and decode the four-digit output values. What do
    # you get if you add up all of the output values?

    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f
    # e    f
    #  gggg

    # 0: denoted by six letters. <- a, b, c, e, f, g - length 6
    # 1: denoted by two letters. <- c, f - length 2
    # 2: denoted by five letters. <- a, c, d, e, g - length 5
    # 3: denoted by five letters. <- a, c, d, f, g - length 5
    # 4: denoted by four letters. <- b, c, d, f - length 4
    # 5: denoted by five letters. <- a, b, d, f, g - length 5
    # 6: denoted by six letters. <- a, b, d, e, f, g - length 6
    # 7: denoted by three letters. <- a, c, f - length 3
    # 8: denoted by seven letters. <- a, b, c, d, e, f, g - length 7
    # 9: denoted by six letters. <- a, b, c, d, f, g - length 6

    # Split the training data and actual values into two lists.
    training_data = list(map(lambda line: line.split(" |")[0], lines))
    actual_values = list(map(lambda line: line.split(" |")[1], lines))

    # Define the base pattern for each wire linking it to one or more numbers.
    base_patterns = {
        "a": [0, 2, 3, 5, 6, 7, 8, 9],
        "b": [0, 4, 5, 6, 8, 9],
        "c": [0, 1, 2, 3, 4, 7, 8, 9],
        "d": [2, 3, 4, 5, 6, 8, 9],
        "e": [0, 2, 6, 8],
        "f": [0, 1, 3, 4, 5, 6, 7, 8, 9],
        "g": [0, 2, 3, 5, 8, 9],
    }

    # Logic: For each line find the trivial numbers, 1, 4, 7 and 8. Build a
    # dictionary of the wires and their connections. Eliminate overlapping
    # wires using logic. Then, for each wire, find the possible values for the
    # wire, again eliminating overlapping wires as they are discovered. Repeat
    # this process until all wires have only one possible value. Using the base
    # patterns in combination with the discovered wire layout determine the
    # values for the actual_values numbers.

    for line in training_data:
        current_pattern = {}
        # Repeat until we have identified all wires for the current pattern
        while len(current_pattern) < 7:
            for digit in line.split():
                # Find the wire possibilities for the current digit.
                current_pattern = detect_wires(digit, current_pattern)
                # Correct current pattern, clearing overlapping wires.
                current_pattern = correct_pattern(current_pattern)
        singular_pattern = False
        while not singular_pattern:
            singular_pattern = True
            current_pattern = correct_pattern(current_pattern)
            for wires in current_pattern.values():
                if len(wires) > 1:
                    singular_pattern = False
        print(f"{line} -> {current_pattern}")

    solution = "Banana"
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
