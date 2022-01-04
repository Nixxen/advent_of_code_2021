RUN_TEST = False
TEST_SOLUTION = 26984457539
TEST_INPUT_FILE = "test_input_day_06.txt"
INPUT_FILE = "input_day_06.txt"

ARGS = []

from day06_part1 import fish_breeder


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 6 Part 2: Suppose the lanternfish live forever and have unlimited
    # food and space. Would they take over the entire ocean? How many
    # lanternfish would there be after 256 days?

    # Initialize dictionary with day values as keys and fish population as values
    fish_dict = {}
    for fish in lines[0].split(","):
        fish_dict[int(fish)] = fish_dict.get(int(fish), 0) + 1

    solution = fish_breeder(fish_dict, 256)

    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
