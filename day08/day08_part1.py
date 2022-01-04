RUN_TEST = False
TEST_SOLUTION = 26
TEST_INPUT_FILE = "test_input_day_08.txt"
INPUT_FILE = "input_day_08.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 8: Part 1 - 7 segment display. Each digit of a seven-segment display
    # is rendered by turning on or off any of seven segments named a through g:
    #   0:      1:      2:      3:      4:
    #  aaaa    ....    aaaa    aaaa    ....
    # b    c  .    c  .    c  .    c  b    c
    # b    c  .    c  .    c  .    c  b    c
    #  ....    ....    dddd    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f
    # e    f  .    f  e    .  .    f  .    f
    #  gggg    ....    gggg    gggg    ....
    #   5:      6:      7:      8:      9:
    #  aaaa    aaaa    aaaa    aaaa    aaaa
    # b    .  b    .  .    c  b    c  b    c
    # b    .  b    .  .    c  b    c  b    c
    #  dddd    dddd    ....    dddd    dddd
    # .    f  e    f  .    f  e    f  .    f
    # .    f  e    f  .    f  e    f  .    f
    #  gggg    gggg    ....    gggg    gggg

    # Each entry consists of ten unique signal patterns, a | delimiter, and
    # finally the four digit output value. Within an entry, the same
    # wire/segment connections are used (but you don't know what the
    # connections actually are). The unique signal patterns correspond to the
    # ten different ways the submarine tries to render a digit using the
    # current wire/segment connections.

    # In the output values, how many times do digits 1, 4, 7, or 8 appear?

    # 0: denoted by six letters.
    # 1: denoted by two letters. <- only one with two wires
    # 2: denoted by five letters.
    # 3: denoted by five letters.
    # 4: denoted by four letters. <- only one with four wires
    # 5: denoted by five letters.
    # 6: denoted by six letters.
    # 7: denoted by three letters. <- only one with three wires
    # 8: denoted by seven letters. <- only one with seven wires
    # 9: denoted by six letters.

    # Split the training data and actual values into two lists.
    training_data = list(map(lambda line: line.split(" |")[0], lines))
    actual_values = list(map(lambda line: line.split(" |")[1], lines))

    # Hold that thought... Only need to count occurences of 1, 4, 7, and 8.
    # Can just count the length of the values in actual_values.

    easy_distinct_values = {}
    for numbers in actual_values:
        for digit in numbers.split(" "):
            if len(digit) == 2:
                easy_distinct_values[1] = easy_distinct_values.get(1, 0) + 1
            elif len(digit) == 3:
                easy_distinct_values[7] = easy_distinct_values.get(7, 0) + 1
            elif len(digit) == 4:
                easy_distinct_values[4] = easy_distinct_values.get(4, 0) + 1
            elif len(digit) == 7:
                easy_distinct_values[8] = easy_distinct_values.get(8, 0) + 1

    solution = sum(easy_distinct_values.values())
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
