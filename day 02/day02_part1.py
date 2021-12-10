RUN_TEST = False
TEST_SOLUTION = 150
TEST_INPUT_FILE = "test_input_day_02.txt"
INPUT_FILE = "input_day_02.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 1
    # Calculate the horizontal position and depth you would have after
    # following the planned course. What do you get if you multiply your
    # final horizontal position by your final depth?

    # Inputs:
    # forward X increases the horizontal position by X units.
    # down X increases the depth by X units.
    # up X decreases the depth by X units.

    # Convert the input into a dictionary of instructions,
    # adding the total number of steps to each instruction.
    instructions = {}
    for line in lines:
        instruction, steps = line.split(" ")
        instructions[instruction] = instructions.setdefault(instruction, 0) + int(steps)

    # Calculate final position and depth.
    final_position = instructions["forward"] * (
        instructions["down"] - instructions["up"]
    )

    solution = final_position
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
