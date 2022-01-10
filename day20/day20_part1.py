RUN_TEST = True
TEST_SOLUTION = 35
TEST_INPUT_FILE = "test_input_day_20.txt"
INPUT_FILE = "input_day_20.txt"

ARGS = []


def debug_print_image(input_image, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in input_image:
                line += "#"
            else:
                line += "."
        print(line)
    print()


def padded_image(input_image, padding, min_x, max_x, min_y, max_y):
    # for y in range(min_y - padding, max_y + padding + 1):
    #     input_image[(min_x - padding - 1, y)] = 1
    #     input_image[(max_x + padding + 1, y)] = 1
    # for x in range(min_x - padding, max_x + padding + 1):
    #     input_image[(x, min_y - padding - 1)] = 1
    #     input_image[(x, max_y + padding + 1)] = 1
    return input_image


def remove_padding(input_image, padding, min_x, max_x, min_y, max_y):
    # Remove padded keys if they exists
    for y in range(min_y - padding, max_y + padding + 1):
        if (min_x - padding - 1, y) in input_image:
            del input_image[(min_x - padding - 1, y)]
        if (max_x + padding + 1, y) in input_image:
            del input_image[(max_x + padding + 1, y)]
    for x in range(min_x - padding, max_x + padding + 1):
        if (x, min_y - padding - 1) in input_image:
            del input_image[(x, min_y - padding - 1)]
        if (x, max_y + padding + 1) in input_image:
            del input_image[(x, max_y + padding + 1)]
    return input_image


def image_enhancement_algorithm(
    input_image, algorithm_reference, iterations, padding, min_x, max_x, min_y, max_y
):
    for enhancement in range(iterations):
        output_image = {}
        for x in range(min_x - padding, max_x + padding + 1):
            for y in range(min_y - padding, max_y + padding + 1):
                # Get the 3x3 square of pixels around the current pixel, and store
                # them as a binary number with 9 bits.
                binary_number = ""
                for y_offset in range(-1, 2):
                    if y + y_offset < min_y - padding or y + y_offset > max_y + padding:
                        break  # skip outside padding
                    for x_offset in range(-1, 2):
                        if (
                            x + x_offset < min_x - padding
                            or x + x_offset > max_x + padding
                        ):
                            break  # skip outside padding
                        if (x + x_offset, y + y_offset) in input_image:
                            binary_number += "1"
                        else:
                            binary_number += "0"
                    else:
                        continue
                    break  # skip outside padding
                else:
                    # Both loops exited without breaking.
                    pixel_string = algorithm_reference[int(binary_number, 2)]
                    if pixel_string == "#":
                        output_image[(x, y)] = 1
        # Fix min and max values for the next iteration
        min_x = min(output_image, key=lambda x: x[0])[0]
        max_x = max(output_image, key=lambda x: x[0])[0]
        min_y = min(output_image, key=lambda x: x[1])[1]
        max_y = max(output_image, key=lambda x: x[1])[1]
        # TODO: Need to add padding for the next iteration, but it needs to
        # read the value from index 0 on the algrithm_reference.
        input_image = output_image
        if RUN_TEST:
            print(f"Test input after {enhancement + 1} passes:")
            debug_print_image(
                input_image,
                min_x - padding,
                max_x + padding,
                min_y - padding,
                max_y + padding,
            )
    return input_image


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 20 Part 1 - Trench map (image processing). The first section of the
    # input is the image enhancement algorithm. The second section is the input
    # image, a two-dimensional grid of light pixels (#) and dark pixels (.).
    #
    # The image enhancement algorithm describes how to enhance an image by
    # simultaneously converting all pixels in the input image into an output
    # image. Each pixel of the output image is determined by looking at a 3x3
    # square of pixels centered on the corresponding input image pixel.
    #
    # The image enhancement algorithm string is exactly 512 characters long,
    # enough to match every possible 9-bit binary number.
    #
    # Through advances in imaging technology, the images being operated on here
    # are infinite in size. Every pixel of the infinite output image needs to
    # be calculated exactly based on the relevant pixels of the input image.
    # The small input image you have is only a small region of the actual
    # infinite input image; the rest of the input image consists of dark pixels
    # (.).
    #
    # Start with the original input image and apply the image enhancement
    # algorithm twice, being careful to account for the infinite size of the
    # images. How many pixels are lit in the resulting image?

    input_image = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    padding = 3  # Padding for the looping to include external pixels.

    # Lines 3 and out are the puzzle input.
    # Store the lit pixel values in a dictionary of coordinates.
    # Keep track of the minimum and maximum x and y values, so we can iterate
    # over the entire image later.
    skip_lines = 2
    for y, line in enumerate(lines[skip_lines:]):
        for x, char in enumerate(line):
            if char == "#":
                input_image[(x, y - skip_lines)] = 1
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y - skip_lines)
                max_y = max(max_y, y - skip_lines)

    # Pad the image with extra pixels on the edges, so we can skip the edge.
    # input_image = padded_image(input_image, padding, min_x, max_x, min_y, max_y)

    if RUN_TEST:
        print("Test input:")
        debug_print_image(
            input_image,
            min_x - padding,
            max_x + padding,
            min_y - padding,
            max_y + padding,
        )

    # Iterate over the entire image, applying the image enhancement algorithm.
    input_image = image_enhancement_algorithm(
        input_image, lines[0], 2, padding, min_x, max_x, min_y, max_y
    )

    # Remove the padding from the image.
    # input_image = remove_padding(input_image, padding, min_x, max_x, min_y, max_y)

    # Count the number of lit pixels.
    solution = sum(input_image.values())
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
