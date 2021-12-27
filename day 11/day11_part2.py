RUN_TEST = False
TEST_SOLUTION = 195
TEST_INPUT_FILE = "test_input_day_11.txt"
INPUT_FILE = "input_day_11.txt"

ARGS = []

from day11_part1 import get_adjacent_coords, simulate_step


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 11 Part 2 - Simultaneous octopus flash. If you can calculate the
    # exact moments when the octopuses will all flash simultaneously, you
    # should be able to navigate through the cavern. What is the first step
    # during which all octopuses flash?

    octopus_dict = {}
    for x, line in enumerate(lines):
        for y, energy in enumerate(line):
            octopus_dict[(x, y)] = int(energy)

    # Simulate until every octopus flashes at the same step
    step = 0
    while True:
        step += 1
        octopus_dict, step_flashes = simulate_step(octopus_dict)
        if step_flashes == len(octopus_dict):
            break

    solution = step
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
