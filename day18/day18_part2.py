RUN_TEST = False
TEST_SOLUTION = 3993
TEST_INPUT_FILE = "test_input_day_18.txt"
INPUT_FILE = "input_day_18.txt"

ARGS = []

import ast
import copy
from day18_part1 import (
    Node,
    add_list_to_tree,
    add_tree_to_tree,
    reduce_tree,
)


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 18 Part 2 - Largest possible magnitute. What is the
    # largest magnitude of any sum of two different snailfish numbers from the
    # homework assignment?

    # Parse each line into a list. Parse the list into a binary tree
    numbers = []
    for line in lines:
        list_line = ast.literal_eval(line)
        head = Node()
        head.left = add_list_to_tree(list_line[0], parent=head)
        head.right = add_list_to_tree(list_line[1], parent=head)
        head = reduce_tree(head)
        numbers.append(head)

    # Make a list of unique pairings of numbers, going both ways.
    unique_pairs = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                # Deepcopy hack, to avoid modifying the objects when adding.
                unique_pairs.append(
                    (copy.deepcopy(numbers[i]), copy.deepcopy(numbers[j]))
                )
                unique_pairs.append(
                    (copy.deepcopy(numbers[j]), copy.deepcopy(numbers[i]))
                )

    # Find the largest sum of two numbers.
    largest_sum = 0
    for pair in unique_pairs:
        combined_pair = add_tree_to_tree(pair[0], pair[1])
        combined_pair = reduce_tree(combined_pair)
        total = combined_pair.get_magnitude()
        if total >= largest_sum:
            largest_sum = total

    solution = largest_sum
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
