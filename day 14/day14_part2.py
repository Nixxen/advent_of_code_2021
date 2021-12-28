RUN_TEST = False
TEST_SOLUTION = 2188189693529
TEST_INPUT_FILE = "test_input_day_14.txt"
INPUT_FILE = "input_day_14.txt"

ARGS = []


def apply_polymer_rules(pairs, rules, element_count, num_steps) -> dict:
    for i in range(num_steps):
        new_pairs = {}
        for pair in pairs:
            if pair in rules:
                new_pairs[pair[0] + rules[pair]] = (
                    new_pairs.get(pair[0] + rules[pair], 0) + pairs[pair]
                )
                new_pairs[rules[pair] + pair[1]] = (
                    new_pairs.get(rules[pair] + pair[1], 0) + pairs[pair]
                )
                element_count[rules[pair]] = (
                    element_count.get(rules[pair], 0) + pairs[pair]
                )
            else:
                print(f"No rule for pair: {pair}")
                new_pairs[pair] = new_pairs.get(pair, 0) + pairs[pair]
        pairs = new_pairs
    return element_count


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 14 Part 2 - More polymerization. Apply 40 steps of pair insertion to
    # the polymer template and find the most and least common elements in the
    # result. What do you get if you take the quantity of the most common
    # element and subtract the quantity of the least common element?

    # Store the base polymer as a list of characters, and the rules as a dict
    # where they key is the two letter pairing and the value is the reaction
    # NOTE: String manipulation is way slow... Rebuild pairs as dict instead.
    pairs = {}
    element_count = {}  # Workaround for not having to rebuild the pairs dict afterwards
    for i in range(len(lines[0]) - 1):
        pair = lines[0][i : i + 2]
        pairs[pair] = pairs.get(pair, 0) + 1
        element_count[lines[0][i]] = element_count.get(lines[0][i], 0) + 1
    element_count[lines[0][len(lines[0]) - 1]] = (
        element_count.get(lines[0][len(lines[0]) - 1], 0) + 1
    )

    rules = {}
    for line in lines[2:]:  # Second line is blank.
        rules[line.split()[0]] = line.split()[2]

    element_count = apply_polymer_rules(pairs, rules, element_count, 40)

    # Find the most common and least common elements in the result and subtract
    # the least common element from the most common element to get the answer.
    most_common = max(element_count, key=element_count.get)
    least_common = min(element_count, key=element_count.get)

    solution = element_count[most_common] - element_count[least_common]
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
