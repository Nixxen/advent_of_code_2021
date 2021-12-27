RUN_TEST = False
TEST_SOLUTION = 1656
TEST_INPUT_FILE = "test_input_day_11.txt"
INPUT_FILE = "input_day_11.txt"

ARGS = []


def debug_print(octopus_dict):
    # Print the current state of the octopus dictionary
    for y in range(10):
        for x in range(10):
            coord = (x, y)
            if coord in octopus_dict:
                print(octopus_dict[coord], end="")
            else:
                print(".", end="")
        print()
    print()


def get_adjacent_coords(coord, min_x=0, max_x=9, min_y=0, max_y=9):
    # Return a list of coordinates that are adjacent to coord, including
    # diagonally adjacent coordinates
    x, y = coord
    adjacent_coords = []
    for x_adj in range(max(x - 1, min_x), min(x + 2, max_x + 1)):
        for y_adj in range(max(y - 1, min_y), min(y + 2, max_y + 1)):
            if (x_adj, y_adj) != coord:
                adjacent_coords.append((x_adj, y_adj))
    return adjacent_coords


def simulate_step(octopus_dict):
    # Simulate a single step
    # - First, the energy level of each octopus increases by 1.
    # - Then, any octopus with an energy level greater than 9 flashes.
    #   This increases the energy level of all adjacent octopuses by 1,
    #   including octopuses that are diagonally adjacent. If this causes an
    #   octopus to have an energy level greater than 9, it also flashes. This
    #   process continues as long as new octopuses keep having their energy
    #   level increased beyond 9. (An octopus can only flash at most once per
    #   step.)
    # - Finally, any octopus that flashed during this step has its energy
    #   level set to 0, as it used all of its energy to flash.
    #
    # Return the new octopus dictionary and the number of flashes
    flashes = 0
    octopus_flashed = set()
    octopus_coords = list(octopus_dict.keys())

    # Increment all octopus energy levels by 1
    for octopus in octopus_dict:
        octopus_dict[octopus] += 1

    # Check if any octopus has an energy level greater than 9
    something_changed = True
    while something_changed:
        something_changed = False
        for coord in octopus_coords:
            if octopus_dict[coord] > 9 and not coord in octopus_flashed:
                flashes += 1
                octopus_flashed.add(coord)
                for adjacent_coord in get_adjacent_coords(coord):
                    octopus_dict[adjacent_coord] += 1
                something_changed = True

    # Set all flashed octopuses to 0
    for coord in octopus_flashed:
        octopus_dict[coord] = 0
    return octopus_dict, flashes


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 11 Part 1 - Dumbo octopus flashes. There are 100 octopuses arranged
    # neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and
    # flashes brightly for a moment when its energy is full. The energy level
    # of each octopus is a value between 0 and 9.
    #
    # You can model the energy levels and flashes of light in steps. During a
    # single step, the following occurs:
    # - First, the energy level of each octopus increases by 1.
    # - Then, any octopus with an energy level greater than 9 flashes.
    #   This increases the energy level of all adjacent octopuses by 1,
    #   including octopuses that are diagonally adjacent. If this causes an
    #   octopus to have an energy level greater than 9, it also flashes. This
    #   process continues as long as new octopuses keep having their energy
    #   level increased beyond 9. (An octopus can only flash at most once per
    #   step.)
    # - Finally, any octopus that flashed during this step has its energy
    #   level set to 0, as it used all of its energy to flash.

    # Given the starting energy levels of the dumbo octopuses in your cavern,
    # simulate 100 steps. How many total flashes are there after 100 steps?

    # Map the input to a dictionary of (x, y) -> energy level
    octopus_dict = {}
    for x, line in enumerate(lines):
        for y, energy in enumerate(line):
            octopus_dict[(x, y)] = int(energy)

    flashes = 0
    # Simulate 100 steps
    for _ in range(100):
        octopus_dict, step_flashes = simulate_step(octopus_dict)
        flashes += step_flashes

    solution = flashes
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
