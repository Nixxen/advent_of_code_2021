RUN_TEST = False
TEST_SOLUTION = 230
TEST_INPUT_FILE = "test_input_day_03.txt"
INPUT_FILE = "input_day_03.txt"

ARGS = []


def find_most_common_binaries_from_list(binary_list):
    # Find the most common value in the current bit position
    bit_keeper = {}
    for i in range(len(binary_list)):
        for j in range(len(binary_list[i])):
            bit_keeper[j] = bit_keeper.setdefault(j, 0) + int(binary_list[i][j])

    most_common_bits = ""
    for i in bit_keeper:
        if bit_keeper[i] > len(binary_list) / 2:
            most_common_bits += "1"
        else:
            most_common_bits += "0"

    return most_common_bits


def find_most_common_binaries_from_set(binary_set):
    # Find the most common value in the current bit position
    bit_keeper = {}
    for i in binary_set:
        for j in range(len(i)):
            bit_keeper[j] = bit_keeper.setdefault(j, 0) + int(i[j])

    most_common_bits = ""
    for i in bit_keeper:
        if bit_keeper[i] >= len(binary_set) / 2:
            most_common_bits += "1"
        else:
            most_common_bits += "0"

    return most_common_bits


def find_least_common_binaries_from_set(binary_set):
    # Find the least common value in the current bit position
    bit_keeper = {}
    for i in binary_set:
        for j in range(len(i)):
            bit_keeper[j] = bit_keeper.setdefault(j, 0) + int(i[j])

    least_common_bits = ""
    for i in bit_keeper:
        if bit_keeper[i] >= len(binary_set) / 2:
            least_common_bits += "0"
        else:
            least_common_bits += "1"

    return least_common_bits


def get_strings_matching_nth_bit(binary_set, n, bit_refference):
    # Get the strings matching the nth bit
    strings_matching_nth_bit = set()
    for i in binary_set:
        if i[n] == bit_refference[n]:
            strings_matching_nth_bit.add(i)

    return strings_matching_nth_bit


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 2
    # Keep only numbers selected by the bit criteria for the type of rating
    # value for which you are searching. Discard numbers which do not match the bit criteria.
    # If you only have one number left, stop; this is the rating value for
    # which you are searching. Otherwise, repeat the process, considering
    # the next bit to the right.

    # The bit criteria depends on which type of rating value you want to find:

    # To find oxygen generator rating, determine the most common value (0 or 1)
    # in the current bit position, and keep only numbers with that bit in that
    # position. If 0 and 1 are equally common, keep values with a 1 in the
    # position being considered.
    # To find CO2 scrubber rating, determine the least common value (0 or 1)
    # in the current bit position, and keep only numbers with that bit in that
    # position. If 0 and 1 are equally common, keep values with a 0 in the
    # position being considered.

    # Steps:
    # Find the most common value in the current bit position
    # Find the least common value in the current bit position
    # For oxygen generator:
    #   Keep only numbers with the most common value in the current bit position
    # For co2 scrubber:
    #   Keep only numbers with the least common value in the current bit position
    # For life support:
    #   Get decimal of oxygen generator rating and co2 scrubber rating
    #   Multiply the two to get the final rating

    # Get the first most common value
    lines = set(lines)
    most_common_bits = find_most_common_binaries_from_set(lines)

    # Get the first least common value
    least_common_bits = find_least_common_binaries_from_set(lines)

    # Prime the sets with the first most common value
    oxygen_generator_set = get_strings_matching_nth_bit(lines, 0, most_common_bits)
    co2_scrubber_set = get_strings_matching_nth_bit(lines, 0, least_common_bits)

    for i in range(1, len(most_common_bits)):
        most_common_bits = find_most_common_binaries_from_set(oxygen_generator_set)
        oxygen_generator_set = get_strings_matching_nth_bit(
            oxygen_generator_set, i, most_common_bits
        )
        if len(oxygen_generator_set) == 1:
            break

    for i in range(1, len(least_common_bits)):
        least_common_bits = find_least_common_binaries_from_set(co2_scrubber_set)
        co2_scrubber_set = get_strings_matching_nth_bit(
            co2_scrubber_set, i, least_common_bits
        )
        if len(co2_scrubber_set) == 1:
            break

    # Get the life support rating by multiplying the oxygen generator rating and the co2 scrubber rating
    oxygen_generator_rating = int("".join(map(str, oxygen_generator_set.pop())), 2)
    co2_scrubber_rating = int("".join(map(str, co2_scrubber_set.pop())), 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    solution = life_support_rating
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
