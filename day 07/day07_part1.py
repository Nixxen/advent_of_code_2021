RUN_TEST = False
TEST_SOLUTION = 37
TEST_INPUT_FILE = "test_input_day_07.txt"
INPUT_FILE = "input_day_07.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 7 Part 1: Crab submarines have limited fuel, so you need to find a
    # way to make all of their horizontal positions match while requiring them
    # to spend as little fuel as possible. Each change of 1 step in horizontal
    # position of a single crab costs 1 fuel. Determine the horizontal position
    # that the crabs can align to using the least fuel possible. How much fuel
    # must they spend to align to that position?

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
    for end_position in position_counts:
        fuel_requirement = 0
        for start_position, crab_count in position_counts.items():
            # Calculate the fuel required to move from start_position to
            # end_position for every crab in the start_position
            fuel_requirement += abs(start_position - end_position) * crab_count
        if min_fuel is None or fuel_requirement < min_fuel:
            min_fuel = fuel_requirement

    solution = min_fuel
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
