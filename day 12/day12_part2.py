RUN_TEST = False
TEST_SOLUTION = 3509
TEST_INPUT_FILE = "test_input_day_12.txt"
INPUT_FILE = "input_day_12.txt"

ARGS = []


# Returns the number of paths through the cave system that start at start and
# end at end - allowing for revisits on large caves, but only once on small
# caves, with the exception of ONE small cave which can be visited twice.
def get_number_of_paths(
    cave_system, start, end, visited=None, special=False, forbidden=None
):
    # Save a set of all small caves (lowercase) that have been visited.
    if visited is None:
        visited = set()
        visited.add(start)
        forbidden = set()
        forbidden.add(start)
        forbidden.add(end)

    paths = 0

    for cave in cave_system[start]:
        if cave == end:
            paths += 1
        else:
            # If the cave has not been visited, add it to the visited set and
            # recurse.
            if cave not in visited:
                visited.add(cave)  # Prevent going back in recursive calls.
                paths += get_number_of_paths(
                    cave_system, cave, end, visited, special, forbidden
                )
                visited.remove(cave)  # Open cave again.
            else:
                # If cave is big, enter it and recurse.
                if cave.isupper():
                    paths += get_number_of_paths(
                        cave_system, cave, end, visited, special, forbidden
                    )
                # If the cave is small, check if special is available.
                elif not special and cave not in forbidden:
                    paths += get_number_of_paths(
                        cave_system, cave, end, visited, not special, forbidden
                    )

    return paths


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 12 Part 2 - Cave traversal, with revisits. big caves can be visited
    # any number of times, a single small cave can be visited at most twice,
    # and the remaining small caves can be visited at most once. However, the
    # caves named start and end can only be visited exactly once each: once you
    # leave the start cave, you may not return to it, and once you reach the
    # end cave, the path must end immediately. Given these new rules, how many
    # paths through this cave system are there?

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
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
