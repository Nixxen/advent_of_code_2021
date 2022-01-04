RUN_TEST = False
TEST_SOLUTION = 198
TEST_INPUT_FILE = "test_input_day_03.txt"
INPUT_FILE = "input_day_03.txt"

ARGS = []


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 1
    # You need to use the binary numbers in the diagnostic report to generate
    # two new binary numbers (called the gamma rate and the epsilon rate).
    # The power consumption can then be found by multiplying the gamma rate
    # by the epsilon rate.

    # Each bit in the gamma rate can be determined by finding the most
    # common bit in the corresponding position of all numbers in the
    # diagnostic report.

    # Use the binary numbers in your diagnostic report to calculate the gamma
    # rate and epsilon rate, then multiply them together.
    # What is the power consumption of the submarine?

    # We have 12 bits. Need 12 counters for each bit.
    # Need to find the most common bit in each position.

    # This will be the gamma rate.
    # Flipping each bit will give us the epsilon rate.

    # Then find consumption by multiplying the two rates.

    # Create a dictionary to store the sum of bits in each position.
    # If the total for that bit is bigger than the list / 2, then 1 is the
    # most common bit for that position.

    bit_keeper = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            bit_keeper[j] = bit_keeper.setdefault(j, 0) + int(lines[i][j])

    # Find the most common bit for each position.
    gamma_rate = ""
    for i in bit_keeper:
        if bit_keeper[i] > len(lines) / 2:
            gamma_rate += "1"
        else:
            gamma_rate += "0"

    # Convert gamma rate to binary
    gamma_rate = int(gamma_rate, 2)

    # Bit flip gamma rate to get epsilon rate
    epsilon_rate = gamma_rate ^ (2 ** len(bit_keeper) - 1)

    # Convert gamma and epsilon rates from binary to decimal
    gamma_rate = int(bin(gamma_rate)[2:], 2)
    epsilon_rate = int(bin(epsilon_rate)[2:], 2)

    # Multiply the two rates to get the power consumption
    power_consumption = gamma_rate * epsilon_rate

    solution = power_consumption
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
