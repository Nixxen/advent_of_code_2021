RUN_TEST = False
TEST_SOLUTION = 168
TEST_INPUT_FILE = "test_input_day_07.txt"
INPUT_FILE = "input_day_07.txt"

ARGS = []

import math


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 7 Part 2 crab submarine engines don't burn fuel at a constant rate.
    # Instead, each change of 1 step in horizontal position costs 1 more unit
    # of fuel than the last: the first step costs 1, the second step costs 2,
    # the third step costs 3, and so on.

    # Get a list of the position of all crabs from the input, split on ',',
    # and convert to integers
    positions = list(map(lambda x: int(x), lines[0].split(",")))

    # Count number of crabs in each position and store as a dictionary. The key
    # is the position and the value is the number of crabs in that position.
    position_counts = {}
    for position in positions:
        position_counts[position] = position_counts.get(position, 0) + 1

    # Find the minimum fuel required to align the crabs, iterating through
    # every possible position (costly, but it's a small dictionary)
    min_fuel = None
    for end_position in range(min(positions), max(positions) + 1):
        fuel_requirement = 0
        for start_position, crab_count in position_counts.items():
            # Calculate the fuel required to move from start_position to
            # end_position for each crab in the start position. The fuel
            # cost is increased by one for each step in the horizontal
            # direction.

            # Need to add Factorial but for addition. "Trianglenotation":
            # https://i1115.photobucket.com/albums/k544/akinuri/nth%20triangle%20number-01.jpg
            # sum = n*(n+1)/2
            n = abs(end_position - start_position)
            fuel_requirement += crab_count * math.floor((n * (n + 1)) / 2)
        if min_fuel is None or fuel_requirement < min_fuel:
            min_fuel = fuel_requirement

    solution = min_fuel
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
