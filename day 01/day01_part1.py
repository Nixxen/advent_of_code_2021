RUN_TEST = False
TEST_SOLUTION = 7
TEST_INPUT_FILE = "test_input_day_01.txt"
INPUT_FILE = "input_day_01.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 1
    # count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)
    # Must count every time a number is higher than the previous number

    increases = 0
    previous_depth = int(lines[0])
    for i in range(1, len(lines)):
        depth = int(lines[i])
        if depth > previous_depth:
            increases += 1
        previous_depth = depth

    solution = increases
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
