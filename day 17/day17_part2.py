RUN_TEST = False
TEST_SOLUTION = 112
TEST_INPUT_FILE = "test_input_day_17.txt"
INPUT_FILE = "input_day_17.txt"

ARGS = []


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 17 - Trick shot, but not. How many distinct initial velocity values
    # cause the probe to be within the target area after any step?

    target_area = {}
    for word in lines[0].replace(",", "").split():
        if word.startswith("x="):
            x_range = list(map(int, word[2:].split("..")))
        elif word.startswith("y="):
            y_range = list(map(int, word[2:].split("..")))

    for x in range(x_range[0], x_range[1] + 1):
        for y in range(y_range[0], y_range[1] + 1):
            target_area[(x, y)] = True

    # Target area static variables.
    target_area_y_min = y_range[0]
    target_area_y_max = y_range[1]
    target_area_x_min = x_range[0]
    target_area_x_max = x_range[1]

    # Dictionary to store the good initial velocity values.
    good_initial_velocity_values = {}

    # Bruteforce all possible velocities (well within reason)
    for x_velocity in range(0, target_area_x_max + 1):
        for y_velocity in range(-target_area_y_min, target_area_y_min * 2, -1):
            x = 0
            y = 0
            x_velocity_change = 0
            y_velocity_change = 0
            while True:
                x += x_velocity + x_velocity_change
                y += y_velocity + y_velocity_change
                if (x, y) in target_area:
                    good_initial_velocity_values[(x_velocity, y_velocity)] = True
                    break  # Hit the target, try next velocity
                if x_velocity + x_velocity_change > 0:
                    x_velocity_change -= 1
                elif x_velocity + x_velocity_change < 0:
                    x_velocity_change += 1
                y_velocity_change -= 1
                if y_velocity + y_velocity_change < 0 and y < target_area_y_min:
                    break  # Bad attempt, try next velocity
                if x > target_area_x_max:
                    break  # Bad attempt, try next velocity

    solution = len(good_initial_velocity_values)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
