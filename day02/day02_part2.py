RUN_TEST = False
TEST_SOLUTION = 900
TEST_INPUT_FILE = "test_input_day_02.txt"
INPUT_FILE = "input_day_02.txt"

ARGS = []


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 2
    # down X increases your aim by X units.
    # up X decreases your aim by X units.
    # forward X does two things:
    # It increases your horizontal position by X units.
    # It increases your depth by your aim multiplied by X.

    # "down" means aiming in the positive direction.
    # calculate the horizontal position and depth you would have after
    # following the planned course. What do you get if you multiply your
    # final horizontal position by your final depth?

    instructions = {}
    instructions["aim"] = 0

    for line in lines:
        instruction, steps = line.split(" ")
        match instruction:
            case "forward":
                instructions[instruction] = instructions.setdefault(instruction, 0) + int(steps)
                instructions["depth"] = instructions.setdefault("depth", 0) + int(steps) * instructions["aim"]
            case "up":
                instructions["aim"] = instructions.setdefault("aim", 0) - int(steps)
            case "down":
                instructions["aim"] = instructions.setdefault("aim", 0) + int(steps)

    final_position = instructions["forward"] * instructions["depth"]
            
        

    solution = final_position
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
