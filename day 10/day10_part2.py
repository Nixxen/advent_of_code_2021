RUN_TEST = False
TEST_SOLUTION = 288957
TEST_INPUT_FILE = "test_input_day_10.txt"
INPUT_FILE = "input_day_10.txt"

ARGS = []

from collections import deque
from day10_part1 import is_close_bracket, is_open_bracket, is_matching_bracket


def get_correct_closing_bracket(open_bracket):
    if open_bracket == "(":
        return ")"
    elif open_bracket == "[":
        return "]"
    elif open_bracket == "{":
        return "}"
    elif open_bracket == "<":
        return ">"


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 10 Part 2 - Bracket matching fixing. Incomplete lines don't have any
    # incorrect characters - instead, they're missing some closing characters
    # at the end of the line. To repair the navigation subsystem, you just need
    # to figure out the sequence of closing characters that complete all open
    # chunks in the line. You can only use closing characters; ), ], }, or >,
    # and you must add them in the correct order so that only legal pairs are
    # formed and all chunks end up closed.

    # The score is determined by considering the completion string
    # character-by-character. Start with a total score of 0. Then, for each
    # character, multiply the total score by 5 and then increase the total
    # score by the point value given for the character in the following table:
    # ): 1 point.
    # ]: 2 points.
    # }: 3 points.
    # >: 4 points.

    score_table = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    # The winner is found by sorting all of the scores and then taking the
    # middle score. Find the completion string for each incomplete line, score
    # the completion strings, and sort the scores. What is the middle score?

    score_list = []
    for line in lines:
        line_score_list = []
        syntax_stack = deque()
        for char in line:
            if is_open_bracket(char):
                syntax_stack.append(char)
            elif is_close_bracket(char):
                if not syntax_stack:
                    print(f"Error: {char} without matching open bracket")
                    break
                else:
                    open_bracket = syntax_stack.pop()
                    if not is_matching_bracket(open_bracket, char):
                        break  # Skip corrupted lines
        else:  # No break in the for loop
            while syntax_stack:
                missing_bracket = syntax_stack.pop()
                line_score_list.append(get_correct_closing_bracket(missing_bracket))
            score = 0
            for i, bracket in enumerate(line_score_list):
                score = score * 5 + score_table[bracket]
            score_list.append(score)

    solution = sorted(score_list)[len(score_list) // 2]
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
