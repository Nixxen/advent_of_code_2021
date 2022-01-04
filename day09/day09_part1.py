RUN_TEST = False
TEST_SOLUTION = 15
TEST_INPUT_FILE = "test_input_day_09.txt"
INPUT_FILE = "input_day_09.txt"

ARGS = []


def get_adjacent_points(lines, x, y):
    # Build a list of adjacent points
    adjacent_points = []
    if y > 0:
        adjacent_points.append(lines[x][y - 1])
    if y < len(lines[0]) - 1:
        adjacent_points.append(lines[x][y + 1])
    if x > 0:
        adjacent_points.append(lines[x - 1][y])
    if x < len(lines) - 1:
        adjacent_points.append(lines[x + 1][y])
    return adjacent_points


# Boolean to check if the point at (x, y) is a low point.
def is_low_point(value, adjacent_points):
    # Check if the point at (x, y) is a low point
    if value < min(adjacent_points):
        return True
    else:
        return False


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 9 Part 1. Your first goal is to find the low points - the locations
    # that are lower than any of its adjacent locations. Most locations have
    # four adjacent locations (up, down, left, and right); locations on the
    # edge or corner of the map have three or two adjacent locations,
    # respectively. (Diagonal locations do not count as adjacent.) The risk
    # level of a low point is 1 plus its height. Find all of the low points on
    # your heightmap. What is the sum of the risk levels of all low points on
    # your heightmap?

    # The input is a list of strings, each string representing a row of the
    # heightmap.

    # Scan every location in the heightmap, and check if it is a low point.
    # If so, add it to the list of low points.
    low_points = []
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if is_low_point(lines[x][y], get_adjacent_points(lines, x, y)):
                low_points.append(lines[x][y])

    # Sum the risk level of all low points
    risk_level = 0
    for point in low_points:
        risk_level += int(point) + 1

    solution = risk_level
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
