RUN_TEST = False
TEST_SOLUTION = 1924
TEST_INPUT_FILE = "test_input_day_04.txt"
INPUT_FILE = "input_day_04.txt"

ARGS = []

from day04_part1 import update_board
from day04_part1 import get_board_sum
from day04_part1 import check_board


def count_unsolved_bingos(boards_list):
    unsolved_boards = []
    for board in boards_list:
        if not check_board(board, "X"):
            unsolved_boards.append(board)
    return len(unsolved_boards)


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 2
    # figure out which board will win last

    # Remove the numbers in the sets as they are updated, and add an 'X'
    # marker, to avoid having to check filled boards.

    # Get the first row from lines and convert it to a list of ints
    # These are the bingo numbers that are drawn
    first_row = list(map(int, lines[0].split(",")))

    # Make a list of sets and a mirrored set of lists for each board
    # (consisting of a 2d list of ints) The list of sets contain all the
    # numbers in a board, which can then be used to find the index of a board
    # in the set of board lists
    boards_list = []  # List of lists of lists of ints
    board_numbers_list = []  # List of sets of ints
    current_board = []
    for i in range(2, len(lines), 6):
        # append the numbers in the next five lines to the current board
        for j in range(5):
            current_board.append(list(map(int, lines[i + j].split())))
        boards_list.append(current_board)
        # Get all numbers in the current board and add them to the current
        # board set
        current_board_set = set()
        for row in current_board:
            current_board_set.update(row)
        board_numbers_list.append(current_board_set)
        current_board = []

    # Iterate through the first row and check if any of the numbers are in any
    # of the boards. Remove the number from that boards set. If a row or column
    # is completely marked, end the game, store that boards index and the last
    # number drawn.
    losing_board_index = None
    losing_number = None
    marker = "X"

    for number in first_row:
        for board_index, board_set in enumerate(board_numbers_list):
            if number in board_set:
                board_set.remove(number)
                update_board(boards_list[board_index], number, marker)
                if check_board(boards_list[board_index], marker):
                    # Check if this is the last board to be solved
                    if count_unsolved_bingos(boards_list) == 0:
                        losing_board_index = board_index
                        losing_number = number
                        break

        if losing_board_index is not None:
            break

    losing_board_sum = get_board_sum(boards_list[losing_board_index])
    losing_board_score = losing_board_sum * losing_number

    solution = losing_board_score
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
