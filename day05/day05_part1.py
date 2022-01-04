RUN_TEST = False
TEST_SOLUTION = 5
TEST_INPUT_FILE = "test_input_day_05.txt"
INPUT_FILE = "input_day_05.txt"

ARGS = []


def get_line_coords_if_horizontal_or_vertical(line):
    # Extract the coordinates from the line. Format: X1,Y1 -> X2,Y2
    line_coords = []
    x_coord = int(line.split(" ")[0].split(",")[0])
    y_coord = int(line.split(" ")[0].split(",")[1])
    x_coord_end = int(line.split(" ")[2].split(",")[0])
    y_coord_end = int(line.split(" ")[2].split(",")[1])

    # Calculate the coordinates of the line if it is horizontal or vertical.
    if x_coord == x_coord_end:
        # Horizontal line
        for y in range(min(y_coord, y_coord_end), max(y_coord, y_coord_end) + 1):
            line_coords.append((x_coord, y))
    if y_coord == y_coord_end:
        # Vertical line
        for x in range(min(x_coord, x_coord_end), max(x_coord, x_coord_end) + 1):
            line_coords.append((x, y_coord))

    return line_coords


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 1 To avoid the most dangerous areas, you need to determine the
    # number of points where at least two lines overlap. Consider only
    # horizontal and vertical lines. At how many points do at least two lines
    # overlap?

    # Create a dictionary with all coordinates as keys. Iterate through the
    # lines and add the coordinates to the dictionary.
    coordinates = {}
    for line in lines:
        line_coords = get_line_coords_if_horizontal_or_vertical(line)
        for coord in line_coords:
            coordinates[coord] = coordinates.get(coord, 0) + 1

    # Count the number of coordinates that have a value of 2 or more.
    count = 0
    for coord in coordinates:
        if coordinates[coord] >= 2:
            count += 1

    solution = count
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
