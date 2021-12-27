RUN_TEST = False
TEST_SOLUTION = 17
TEST_INPUT_FILE = "test_input_day_13.txt"
INPUT_FILE = "input_day_13.txt"

ARGS = []


def debug_print(dots):
    # Prints the dos at their respective coordinates, represented by '#'.
    # Padding with '.'
    for y in range(
        min(dots.keys(), key=lambda x: x[1])[1],
        max(dots.keys(), key=lambda x: x[1])[1] + 1,
    ):
        for x in range(
            min(dots.keys(), key=lambda x: x[0])[0],
            max(dots.keys(), key=lambda x: x[0])[0] + 1,
        ):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 13 Part 1 - Folding transparent paper. The input are a list of
    # coordinates representing dots on a transparent paper. The folding
    # instructions are represented by "fold along x=N" and "fold along y=N",
    # where N is a number. X goes from left to right, and Y goes from top to
    # bottom. After folding, any overlapping dots will be counted as one dot.
    # How many dots are visible after completing just the first fold
    # instruction on your transparent paper?

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
        break  # Only one instruction.

    solution = len(dots)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
