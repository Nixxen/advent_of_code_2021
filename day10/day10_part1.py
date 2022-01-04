RUN_TEST = False
TEST_SOLUTION = 26397
TEST_INPUT_FILE = "test_input_day_10.txt"
INPUT_FILE = "input_day_10.txt"

ARGS = []


from collections import deque


def is_open_bracket(char):
    return char in ["(", "{", "<", "["]


def is_close_bracket(char):
    return char in [")", "}", ">", "]"]


def is_matching_bracket(open_bracket, close_bracket):
    return (
        (open_bracket == "(" and close_bracket == ")")
        or (open_bracket == "{" and close_bracket == "}")
        or (open_bracket == "[" and close_bracket == "]")
        or (open_bracket == "<" and close_bracket == ">")
    )


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 10 Part 1 - Bracket matching. Some lines are incomplete, but others
    # are corrupted. Find and discard the corrupted lines first. A corrupted
    # line is one where a chunk closes with the wrong character - that is,
    # where the characters it opens and closes with do not form one of the four
    # legal pairs [], {}, () or <>.

    # To calculate the syntax error score for a line, take the first illegal
    # character on the line and look it up in the following table:
    # ): 3 points.
    # ]: 57 points.
    # }: 1197 points.
    # >: 25137 points.
    # The total syntax error score for the entire subsystem is the sum of the
    # scores for each line.

    # Find the first illegal character in each corrupted line of the navigation
    # subsystem. What is the total syntax error score for those errors?

    score_table = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    score_list = []
    for line in lines:
        syntax_stack = deque()
        for char in line:
            if is_open_bracket(char):
                syntax_stack.append(char)
            elif is_close_bracket(char):
                if not syntax_stack:
                    score_list.append(char)
                    break
                else:
                    open_bracket = syntax_stack.pop()
                    if not is_matching_bracket(open_bracket, char):
                        score_list.append(char)
                        break

    # The total syntax error score for the navigation subsystem is the sum of
    # the scores for each line.
    solution = sum(map(lambda char: score_table[char], score_list))
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
