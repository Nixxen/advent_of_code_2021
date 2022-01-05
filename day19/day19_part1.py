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
        if line == "":
            continue
        if line[1] == "-":  # --- scanner n ---, [1] to handle -x values.
            scanner = {}
            scanner["name"] = line.split()[2]
            scanners.append(scanner)
        else:
            # Parse the line of beacons
            x, y, z = [int(coord) for coord in line.split(",")]
            scanner[(x, y, z)] = True

    # For each scanner, search through every other scanner, flipping the other
    # scanner orientation in each of the 6 directions (each with 4 up
    # orientations making a total of 24 orientations), and see if any of the
    # coordinate keys overlap. If so, add them to the map dictionary.
    # TODO: Factor out the rotation and axis logic into a function, so that
    #       I can first find the first match, then use that first match to
    #       find the next match. We could potentially end up with a case where
    #       not every scanner is matched... Let's hope we don't need to deal
    #       with that yet.
    # TODO: Check for delta distances instead of direct equality. If there are
    #       12 matches, combined with 4 directions
    scanner_library = {}
    beacon_map = {}
    for scanner in scanners:
        for other_scanner in scanners:
            if scanner == other_scanner:
                continue
            if (
                scanner["name"] in scanner_library
                and other_scanner["name"] in scanner_library
            ):
                continue
            # Rotate the other scanner 90 degrees around each axis.
            for axis in [0, 1, 2]:  # x, y, z
                for direction in [1, -1]:  # positive, negative
                    for rotation in range(4):  # 0, 90, 180, 270
                        # Rotate the other scanner.
                        other_scanner_rotated = {}
                        for key in other_scanner:
                            if not isinstance(key, tuple):
                                continue
                            x, y, z = key
                            if axis == 0:
                                x = x * direction
                            elif axis == 1:
                                y = y * direction
                            elif axis == 2:
                                z = z * direction
                            x, y, z = rotate_point((x, y, z), rotation, axis)
                            other_scanner_rotated[(x, y, z)] = True
                        # Check if any of the rotated coordinates overlap.
                        match_counter = 0
                        for key in scanner:
                            if match_counter < 12:
                                if key in other_scanner_rotated:
                                    match_counter += 1
                            else:
                                break

                        if match_counter >= 12:
                            # Check if either scanner is in the scanner library.
                            orientation_offset = None
                            # Simplifies adding to the library later
                            missing_scanner = None
                            if scanner["name"] in scanner_library:
                                # Get the orientation offset from the library.
                                orientation_offset = scanner_library[scanner["name"]]
                                missing_scanner = other_scanner
                            if other_scanner["name"] in scanner_library:
                                # Get the orientation offset from the library.
                                orientation_offset = scanner_library[
                                    other_scanner["name"]
                                ]
                                missing_scanner = scanner

                            # Store the scanner orientation in the scanner
                            # library.
                            if orientation_offset is None:
                                scanner_library[scanner["name"]] = ((0, 0, 0), (0, 0))
                                scanner_library[other_scanner["name"]] = (
                                    (x, y, z),
                                    (rotation, axis),
                                )
                                # Add the coordinates to the beacon map.
                                for key in scanner:
                                    if not isinstance(key, tuple):
                                        continue
                                    beacon_map[key] = True
                                for key in other_scanner:
                                    if not isinstance(key, tuple):
                                        continue
                                    beacon_map[key] = True
                            else:
                                scanner_library[missing_scanner["name"]] = (
                                    (
                                        x + orientation_offset[0][0],
                                        y + orientation_offset[0][1],
                                        z + orientation_offset[0][2],
                                    ),
                                    (
                                        rotation + orientation_offset[1][0],
                                        axis + orientation_offset[1][1],
                                    ),
                                )
                                # Add the coordinates to the beacon map.
                                for key in missing_scanner:
                                    if not isinstance(key, tuple):
                                        continue
                                    beacon_map[
                                        (
                                            key[0] + orientation_offset[0][0],
                                            key[1] + orientation_offset[0][1],
                                            key[2] + orientation_offset[0][2],
                                        )
                                    ] = True

    # Count the number of beacons in the map.
    solution = len(beacon_map)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
