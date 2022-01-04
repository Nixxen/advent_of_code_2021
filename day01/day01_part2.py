RUN_TEST = False
TEST_SOLUTION = 5
TEST_INPUT_FILE = "test_input_day_01.txt"
INPUT_FILE = "input_day_01.txt"

ARGS = []


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: int(line.rstrip()), file.readlines()))

    # Part 2
    # consider sums of a three-measurement sliding window.
    # count the number of times the sum of measurements in this sliding
    # window increases from the previous sum. So, compare A with B, then
    # compare B with C, then C with D, and so on. Stop when there aren't
    # enough measurements left to create a new three-measurement sum.

    # Represent the sliding windows as numbers to more easily increment over
    # the list of measurements.
    # Increment the letter for every new group of three and calculate the sum.
    # Then count every time the sliding window increased.

    # Create a dictionary to store the sliding window sums.
    # The key is a number representing the sliding window, the value is the
    # sum of the three measurements in the sliding window.
    sliding_window_sums = {}

    # Add the initial sliding window sum to the dictionary.
    sliding_window_sums[0] = sum(lines[0:3])
    previous_sliding_window_sum = sliding_window_sums[0]

    increments = 0

    # Iterate over the list of measurements.
    for i in range(1, len(lines) - 2):
        # Add the next three measurements to the sliding window sum.
        sliding_window_sums[i] = sum(lines[i : i + 3])
        if sliding_window_sums[i] > previous_sliding_window_sum:
            increments += 1
        previous_sliding_window_sum = sliding_window_sums[i]

    solution = increments
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
