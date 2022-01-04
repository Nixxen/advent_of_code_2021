RUN_TEST = True
TEST_SOLUTION = 79
TEST_INPUT_FILE = "test_input_day_19.txt"
INPUT_FILE = "input_day_19.txt"

ARGS = []


def rotate_point(point: tuple, rotation: int, axis: int) -> tuple:
    """Rotate the point around the given axis, from the origin.

    Args:
        point (tuple): Coordinate tuple in the form (x,y,z)
        rotation (int): rotation ID. Indicating counter-clockwise rotation.
                        0 = no rotation, 1 = 90, 2 = 180, 3 = 270
        axis (int): axis ID. 0 = x, 1 = y, 2 = z
    """
    x, y, z = point
    if rotation == 0:
        pass
    elif rotation == 1:  # 90
        if axis == 0:  # x
            y, z = -z, y  # Rotation according to RH rule
        elif axis == 1:  # y
            x, z = z, -x
        elif axis == 2:  # z
            x, y = -y, x
    elif rotation == 2:  # 180
        if axis == 0:
            y, z = -y, -z
        elif axis == 1:
            x, z = -x, -z
        elif axis == 2:
            x, y = -x, -y
    elif rotation == 3:  # 270
        if axis == 0:
            y, z = z, -y
        elif axis == 1:
            x, z = -z, x
        elif axis == 2:
            x, y = y, -x
    return (x, y, z)


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 19 - Part 1 - Beacon scanner. Each scanner is capable of detecting
    # all beacons in a large cube centered on the scanner; beacons that are at
    # most 1000 units away from the scanner in each of the three axes (x, y,
    # and z) have their precise position determined relative to the scanner.
    # However, scanners cannot detect other scanners. The submarine has
    # automatically summarized the relative positions of beacons detected by
    # each scanner (your puzzle input).
    #
    # The scanners and beacons map a single contiguous 3d region. This region
    # can be reconstructed by finding pairs of scanners that have overlapping
    # detection regions such that there are at least 12 beacons that both
    # scanners detect within the overlap. By establishing 12 common beacons,
    # you can precisely determine where the scanners are relative to each
    # other, allowing you to reconstruct the beacon map one scanner at a time.
    #
    # Unfortunately, there's a second problem: the scanners also don't know
    # their rotation or facing direction. Due to magnetic alignment, each
    # scanner is rotated some integer number of 90-degree turns around all of
    # the x, y, and z axes. That is, one scanner might call a direction
    # positive x, while another scanner might call that direction negative y.
    # Or, two scanners might agree on which direction is positive x, but one
    # scanner might be upside-down from the perspective of the other scanner.
    # In total, each scanner could be in any of 24 different orientations:
    # facing positive or negative x, y, or z, and considering any of four
    # directions "up" from that facing.
    #
    # Assemble the full map of beacons. How many beacons are there?

    # Scanner lines are of the form: --- scanner n ---
    # Followed by several lines of beacons, each of the form: x,y,z

    # Store the scanners in a list of dicts where each dict is a scanner
    # containing the x,y,z coordinates of the beacons as keys.
    scanners = []
    for line in lines:
        if "scanner" in line:
            scanner = {}
            scanner["name"] = line.split()[2]
            scanners.append(scanner)
        else:
            # Parse the line of beacons
            x, y, z = line.split(",")
            scanner[(x, y, z)] = True

    # For each scanner, search through every other scanner, flipping the other
    # scanner orientation in each of the 6 directions (each with 4 up
    # orientations making a total of 24 orientations), and see if any of the
    # coordinate keys overlap. If so, add them to the map dictionary.
    beacon_map = {}
    for scanner in scanners:
        for other_scanner in scanners:
            if scanner == other_scanner:
                continue
            # Rotate the other scanner 90 degrees around each axis.
            for axis in [0, 1, 2]:  # x, y, z
                for direction in [1, -1]:  # positive, negative
                    for rotation in range(4):  # 0, 90, 180, 270
                        # Rotate the other scanner.
                        other_scanner_rotated = {}
                        for key in other_scanner:
                            x, y, z = key
                            if axis == 0:
                                x = x * direction
                            elif axis == 1:
                                y = y * direction
                            elif axis == 2:
                                z = z * direction
                            x, y, z = rotate_point(x, y, z, rotation, axis)
                            other_scanner_rotated[(x, y, z)] = True

            for coordinate in other_scanner:
                other_scanner[axis] *= -1  # TODO: This won't work. Need to split it up.
            # Check if any of the keys overlap
            for key in scanner.keys():
                if key in other_scanner.keys():
                    beacon_map[key] = True
            # Flip the other scanner back
            for axis in ["x", "y", "z"]:
                other_scanner[axis] *= -1

    solution = ...
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
