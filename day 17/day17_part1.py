RUN_TEST = False
TEST_SOLUTION = 45
TEST_INPUT_FILE = "test_input_day_17.txt"
INPUT_FILE = "input_day_17.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 17 Part 1 - Trick shot. The probe launcher on your submarine can fire
    # the probe with any integer velocity in the x (forward) and y (upward, or
    # downward if negative) directions. The probe's x,y position starts at 0,0.
    # Then, it will follow some trajectory by moving in steps. On each step,
    # these changes occur in the following order:
    #
    # - The probe's x position increases by its x velocity.
    # - The probe's y position increases by its y velocity.
    # - Due to drag, the probe's x velocity changes by 1 toward the value 0;
    #   that is, it decreases by 1 if it is greater than 0, increases by 1 if
    #   it is less than 0, or does not change if it is already 0.
    # - Due to gravity, the probe's y velocity decreases by 1.
    #
    # Target area is given by the input, and appears in this form:
    # - target area: x=20..30, y=-10..-5
    #
    # Find the initial velocity that causes the probe to reach the highest y
    # position and still eventually be within the target area after any step.
    # What is the highest y position it reaches on this trajectory?

    # Make a target area dictionary containing the x and y coordinates of the
    # target area.
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

    # We're bruteforcing this. I started with math, but honestly, time setting
    # up the math is more time consuming than just bruteforcing a range, since
    # I don't know the rules required. X value is irelevant, since we only want
    # to find the highest y value. I'll still simulate X, since I already have
    # the dictionary set up.
    max_y = 0
    for x_velocity in range(1, 100):  # Assume one of these will be accurate enough
        for y_velocity in range(1000, 0, -1):
            x = 0
            y = 0
            x_velocity_change = 0
            y_velocity_change = 0
            temp_max_y = max_y
            while True:
                x += x_velocity + x_velocity_change
                y += y_velocity + y_velocity_change
                if y > temp_max_y:
                    temp_max_y = y
                    temp_max_y_velocity = y_velocity
                    temp_max_x_velocity = x_velocity
                if (x, y) in target_area:
                    if temp_max_y > max_y:
                        max_y = temp_max_y
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

    solution = max_y
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
