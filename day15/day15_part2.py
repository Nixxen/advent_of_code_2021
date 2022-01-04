RUN_TEST = False
TEST_SOLUTION = 315
TEST_INPUT_FILE = "test_input_day_15.txt"
INPUT_FILE = "input_day_15.txt"

ARGS = []


from day15_part1 import heuristic, get_neighbors, reconstruct_path, astar


def debug_print(lines, risk_map, path):
    # Print the map, with the repeated map, substituting empty spaces with
    # periods. Path elements are colored green.
    for y in range(len(lines) * 5):
        for x in range(len(lines[0]) * 5):
            if (x, y) in risk_map:
                if (x, y) in path:
                    print("\033[92m{}\033[0m".format(risk_map[(x, y)]), end="")
                else:
                    print(risk_map[(x, y)], end="")
            else:
                print(".", end="")
        print()
    print()


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 15 Part 2 - Chiton pathfinding x5. The entire cave is actually five
    # times larger in both dimensions than you thought; the area you originally
    # scanned is just one tile in a 5x5 tile area that forms the full map. Your
    # original map tile repeats to the right and downward; each time the tile
    # repeats to the right or downward, all of its risk levels are 1 higher
    # than the tile immediately up or left of it. However, risk levels above 9
    # wrap back around to 1.

    # Define the map as a dictionary of (x,y) tuples to risk values.
    risk_map = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            risk_map[(x, y)] = int(char)

    # Add 5 more repetitions of risk_map in every direction, each repetition
    # increasing the risk value by 1, up to a maximum of 9. After 9 risk value
    # it wraps back around to 1.
    for coord in list(risk_map.keys()):
        for x in range(0, 5):
            for y in range(0, 5):
                if x == 0 and y == 0:
                    continue
                new_coord = (
                    coord[0] + (len(lines[0]) * x),
                    coord[1] + (len(lines) * y),
                )
                risk_map[new_coord] = risk_map[coord] + (x + y)
                while risk_map[new_coord] > 9:
                    risk_map[new_coord] -= 9

    # Define the start and goal positions.
    start = (0, 0)
    goal = (len(lines[0]) * 5 - 1, len(lines) * 5 - 1)

    # Find the path with the lowest risk.
    path = astar(risk_map, start, goal, len(lines[0]) * 5, len(lines) * 5)

    # debug_print(lines, risk_map, path)

    # Calculate the total risk of the path.
    total_risk = 0
    for x, y in path:
        total_risk += risk_map[(x, y)]
    # Subract the risk of the starting position.
    total_risk -= risk_map[start]

    solution = total_risk
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
