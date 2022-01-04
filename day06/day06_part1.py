RUN_TEST = False
TEST_SOLUTION = 5934
TEST_INPUT_FILE = "test_input_day_06.txt"
INPUT_FILE = "input_day_06.txt"

ARGS = []


def fish_breeder(fish_dict, end_day):
    # Iterate through dictionary, starting at the bottom.
    for _ in range(0, end_day):
        # Initialize new fish population and recently reproduced fish
        new_fish = 0
        reproduced_fish = 0
        # Save dictionary keys as a list so we can iterate through it while
        # editing.
        fish_list = list(fish_dict.keys())
        fish_list.sort()
        # Iterate through dictionary and add new fish and recently reproduced
        # fish
        for days_to_reproduction in fish_list:
            number_of_fish = fish_dict.get(days_to_reproduction)
            # If the fish is at reproduction day, add to reproduced fish
            # along with new fish
            if days_to_reproduction == 0:
                new_fish += number_of_fish
                reproduced_fish += number_of_fish
            # If the fish is not at reproduction day, move (overwrite) the
            # value to the lower key in the order.
            else:
                fish_dict[days_to_reproduction - 1] = number_of_fish
                fish_dict[days_to_reproduction] = 0

        # Add new fish and recently reproduced fish to the total population
        fish_dict[8] = new_fish
        fish_dict[6] = fish_dict.get(6, 0) + reproduced_fish
    return sum(fish_dict.values())


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 6 Part 1: Each day, a 0 becomes a 6 and adds a new 8 to the end of
    # the list, while each other number decreases by 1 if it was present at the
    # start of the day. [3,4,3,1,2]. This list means that the first fish has an
    # internal timer of 3, the second fish has an internal timer of 4, and so
    # on until the fifth fish, which has an internal timer of 2. Find a way to
    # simulate lanternfish. How many lanternfish would there be after 80 days?

    # Thought process: Iterate through list. Store each day value as a key in a
    # keyvalue pair in a dictionary. The value is the amount of fish with the
    # same day value. Iterate through the dictionary, starting at the bottom,
    # saving new fish and recently reproduced fish as a temporary value. Once
    # the dictionary has been iteraterated through, add the new population and
    # the recently reproduced fish to the total population again. Repeat until
    # we have passed 80 days.

    # Initialize dictionary with day values as keys and fish population as values
    fish_dict = {}
    for fish in lines[0].split(","):
        fish_dict[int(fish)] = fish_dict.get(int(fish), 0) + 1

    solution = fish_breeder(fish_dict, 80)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
