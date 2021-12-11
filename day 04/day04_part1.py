RUN_TEST = False
TEST_SOLUTION = 4512
TEST_INPUT_FILE = "test_input_day_04.txt"
INPUT_FILE = "input_day_04.txt"

ARGS = []


def update_board(board, number, letter):
    for row in board:
        for index, num in enumerate(row):
            if num == number:
                row[index] = letter


def check_board(board, marker):
    # Check if any row or column is completely marked, if so, return true
    for row in board:
        if all(x == marker for x in row):
            return True
    for i in range(len(board[0])):
        column = [row[i] for row in board]
        if all(x == marker for x in column):
            return True


def get_board_sum(board, marker="X"):
    sum_of_remaining_numbers = 0
    for row in board:
        for num in row:
            if num != marker:
                sum_of_remaining_numbers += num
    return sum_of_remaining_numbers


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Part 1 Bingo is played on a set of boards each consisting of a 5x5 grid
    # of numbers. Numbers are chosen at random, and the chosen number is marked
    # on all boards on which it appears. (Numbers may not appear on all
    # boards.) If all numbers in any row or any column of a board are marked,
    # that board wins. (Diagonals don't count.)

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

    # Iterate through the first row and check if any of the numbers are in
    # any of the boards. Update the numbers in the board set with the letter
    # 'X' if they are in the board. If a row or column is completely marked,
    # end the game, store that boards index and the last number drawn.
    winning_board_index = None
    winning_number = None
    marker = "X"
    for number in first_row:
        for board_index, board_set in enumerate(board_numbers_list):
            if number in board_set:
                update_board(boards_list[board_index], number, marker)
                winner = check_board(boards_list[board_index], marker)
                if winner:
                    winning_board_index = board_index
                    winning_number = number
                    break
        if winning_board_index is not None:
            break

    # Get the sum of all remaining numbers in the winning board
    sum_of_remaining_numbers = get_board_sum(boards_list[winning_board_index])

    final_answer = winning_number * sum_of_remaining_numbers

    solution = final_answer
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
