RUN_TEST = False
TEST_SOLUTION = ...
TEST_INPUT_FILE = "test_input_day_13.txt"
INPUT_FILE = "input_day_13.txt"

ARGS = []


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 13 part 2 - Complete the folding. Same procedure as in part 1, but
    # fold every insctruction in the list.

    # Parse the dots into a dictionary of coordinates. Parse the instructions
    # into a list of instructions.
    dots = {}
    instructions = []

    parsing_dots = True
    for line in lines:
        if parsing_dots:
            if line == "":
                parsing_dots = False
            else:
                x, y = line.split(",")
                dots[(int(x), int(y))] = True
        else:
            instructions.append(line.split(" ")[2])

    # Fold the paper.
    for instruction in instructions:
        if instruction[0] == "x":
            x = int(instruction[2:])
            for key in list(dots.keys()):
                if key[0] >= x:
                    dots[(x - abs(x - key[0]), key[1])] = True
                    del dots[key]
        elif instruction[0] == "y":
            y = int(instruction[2:])
            for key in list(dots.keys()):
                if key[1] >= y:
                    dots[(key[0], y - abs(y - key[1]))] = True
                    del dots[key]

    from day13_part1 import debug_print

    print("Final message:")
    debug_print(dots)

    solution = ...  # Solution is shown in debug print.
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
