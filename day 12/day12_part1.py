RUN_TEST = False
TEST_SOLUTION = 226
TEST_INPUT_FILE = "test_input_day_12.txt"
INPUT_FILE = "input_day_12.txt"

ARGS = []


# Returns the number of paths through the cave system that start at start and
# end at end.
def get_number_of_paths(cave_system, start, end, visited=None):
    # Save a set of all small caves (lowercase) that have been visited.
    if visited is None:
        visited = set()
        visited.add(start)

    paths = 0

    for cave in cave_system[start]:
        if cave == end:
            paths += 1
        else:
            # If the cave has not been visited, add it to the visited set and
            # recurse.
            if cave not in visited:
                visited.add(cave)  # Prevent going back in recursive calls.
                paths += get_number_of_paths(cave_system, cave, end, visited)
                visited.remove(cave)  # Open cave again.
            # If cave is big, enter it and recurse.
            elif cave.isupper():
                paths += get_number_of_paths(cave_system, cave, end, visited)

    return paths


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 12 Part 1 - Cave system mapping. Your goal is to find the number of
    # distinct paths that start at start, end at end, and don't visit small
    # caves more than once. There are two types of caves: big caves (written in
    # uppercase, like A) and small caves (written in lowercase, like b). It
    # would be a waste of time to visit any small cave more than once, but big
    # caves are large enough that it might be worth visiting them multiple
    # times. So, all paths you find should visit small caves at most once, and
    # can visit big caves any number of times.

    # How many paths through this cave system are there that visit small caves
    # at most once?

    # Each line contains two linked cavves, separated by a '-'.
    # Build the cave system as a graph, each key is a cave, and each value is
    # a list of caves that are connected to it.
    cave_system = {}
    for line in lines:
        first_cave, second_cave = line.split("-")
        if first_cave not in cave_system:
            cave_system[first_cave] = []
        if second_cave not in cave_system:
            cave_system[second_cave] = []
        cave_system[first_cave].append(second_cave)
        cave_system[second_cave].append(first_cave)

    solution = get_number_of_paths(cave_system, "start", "end")
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
