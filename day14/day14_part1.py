RUN_TEST = False
TEST_SOLUTION = 1588
TEST_INPUT_FILE = "test_input_day_14.txt"
INPUT_FILE = "input_day_14.txt"

ARGS = []


def apply_polymer_rules(base_polymer, rules, num_steps):
    for _ in range(num_steps):
        next_polymer = ""
        # Apply the rules to the base polymer, storing the result in next_polymer
        for i in range(len(base_polymer)):
            if i == len(base_polymer) - 1:
                next_polymer += base_polymer[i]
            elif base_polymer[i : i + 2] in rules:
                next_polymer += base_polymer[i] + rules[base_polymer[i : i + 2]]
            else:
                next_polymer += base_polymer[i]
                print(f"Warning: {base_polymer[i : i + 2]} not in rules")
        base_polymer = next_polymer
    return base_polymer


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 14 part 1 - Extended polymerization. The first line in the input
    # contains a base polymer. Any filled line after this is a rule that
    # applies to the pairs of the base polymer. Pairs overlap, so the last
    # element of one pair is the first element of the next pair. The rules take
    # a two letter pairing and inserts the reaction between the pair letters,
    # such as "NN -> C" would insert a C between the Ns. One step of insertions
    # traverses the length of the polymer, applying the rules in order. Apply
    # 10 steps of pair insertion to the polymer template and find the most and
    # least common elements in the result. What do you get if you take the
    # quantity of the most common element and subtract the quantity of the
    # least common element?

    # Store the base polymer as a list of characters, and the rules as a dict
    # where they key is the two letter pairing and the value is the reaction
    base_polymer = lines[0]
    rules = {}
    for line in lines[2:]:  # Second line is blank.
        rules[line.split()[0]] = line.split()[2]

    base_polymer = apply_polymer_rules(base_polymer, rules, 10)

    # Find the most common and least common elements in the result and subtract
    # the least common element from the most common element to get the answer
    most_common = max(set(base_polymer), key=base_polymer.count)
    least_common = min(set(base_polymer), key=base_polymer.count)

    solution = base_polymer.count(most_common) - base_polymer.count(least_common)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
