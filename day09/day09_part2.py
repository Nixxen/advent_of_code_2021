RUN_TEST = False
TEST_SOLUTION = 1134
TEST_INPUT_FILE = "test_input_day_09.txt"
INPUT_FILE = "input_day_09.txt"

ARGS = []


def debug_print(lines, coordinates):
    # Print a 2D array of the basins numbers, based on coordinates.
    for x, line in enumerate(lines):
        for y, height in enumerate(line):
            if (x, y) in coordinates:
                print(coordinates[(x, y)], end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def get_adjacent_coords(x, y, lines):
    adjacent_coords = []
    if x > 0 and lines[x - 1][y] != "9":
        adjacent_coords.append((x - 1, y))
    if x < len(lines) - 1 and lines[x + 1][y] != "9":
        adjacent_coords.append((x + 1, y))
    if y > 0 and lines[x][y - 1] != "9":
        adjacent_coords.append((x, y - 1))
    if y < len(lines[0]) - 1 and lines[x][y + 1] != "9":
        adjacent_coords.append((x, y + 1))
    return adjacent_coords


def flood_fill_in(x, y, basin_id, lines, coordinates, basin_sizes) -> tuple:
    # Scan the heightmap in every direction from the starting location until a
    # location with height 9 is encounteed. If the location is already in the
    # basin, skip it. If the location is not in the basin, add the coordinates
    # to the coordinates dictionary, and updating the basin_sizes dictionary.
    # Then, flood-fill-in from the new location.
    if (x, y) in coordinates or lines[x][y] == "9":
        return coordinates, basin_sizes, basin_id

    adjacent_coords = get_adjacent_coords(x, y, lines)

    # Update the basin ID to adjacent coordinates basin ID.
    temp_basin_id = None
    for coord in adjacent_coords:
        if coord in coordinates:
            temp_basin_id = coordinates[coord]
            adjacent_coords.remove(coord)
            break
    if temp_basin_id == None:
        basin_id += 1  # New basin. Increment the basin ID.

    # Add the current coordinate to the system, then check adjacent coordinates.
    coordinates[(x, y)] = basin_id
    basin_sizes[basin_id] = basin_sizes.get(basin_id, 0) + 1

    for coord in adjacent_coords:
        if lines[coord[0]][coord[1]] == "9":
            continue  # Should never happen due to earlier filtering but just in case.
        if coord not in coordinates:
            coordinates, basin_sizes, basin_id = flood_fill_in(
                coord[0], coord[1], basin_id, lines, coordinates, basin_sizes
            )
    return coordinates, basin_sizes, basin_id


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 9 Part 2 - Basin hunt. A basin is all locations that eventually flow
    # downward to a single low point. Therefore, every low point has a basin,
    # although some basins are very small. Locations of height 9 do not count
    # as being in any basin, and all other locations will always be part of
    # exactly one basin. The size of a basin is the number of locations within
    # the basin, including the low point.

    # Find the three largest basins and multiply their sizes together. What do
    # you get if you multiply together the sizes of the three largest basins?

    # The input is a list of strings, each string representing a row in the
    # heightmap.

    # Build a dictionary of X and Y coordinates where each coordinate is linked
    # to a basin ID. Keep a separate dictionary with basin IDs as keys and the
    # size (number of locations) of the basin as the value.
    coordinates = {}
    basin_sizes = {}
    basin_id = -1

    # Use flood-fill-in to populate the dictionary, skipping 9-height locations.
    # Start by finding the first non-9 location, adding it to the dictionary,
    # and giving it the starting basin ID, then flood-fill-in from there.

    number_of_nines = 0
    for line in lines:
        for height in line:
            if height == "9":
                number_of_nines += 1
    total_number_of_locations = len(lines) * len(lines[0])

    # Map / fill all basins
    while (number_of_nines + len(coordinates)) < total_number_of_locations:
        for x, line in enumerate(lines):
            for y, height in enumerate(line):
                if height == "9" or (x, y) in coordinates:
                    continue
                coordinates, basin_sizes, basin_id = flood_fill_in(
                    x, y, basin_id, lines, coordinates, basin_sizes
                )

    # Find the three largest basins.
    basin_sizes = sorted(basin_sizes.items(), key=lambda x: x[1], reverse=True)
    largest_basins = basin_sizes[:3]

    print("Largest basins:", largest_basins)

    # Multiply the sizes of the three largest basins together.
    solution = largest_basins[0][1] * largest_basins[1][1] * largest_basins[2][1]
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
