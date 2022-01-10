RUN_TEST = True
TEST_SOLUTION = 444356092776315
TEST_INPUT_FILE = "test_input_day_21.txt"
INPUT_FILE = "input_day_21.txt"

ARGS = []

from day21_part1 import game_over


def multiverse_game_recursion(wins, scores, position, dice_side, player, roll_number):
    # Play game.
    position[player] = ((position[player] + dice_side) - 1) % 10 + 1
    if roll_number != 3:
        w11, w21 = multiverse_game_recursion(
            wins, scores, position, 1, player, roll_number + 1
        )
        w12, w22 = multiverse_game_recursion(
            wins, scores, position, 2, player, roll_number + 1
        )
        w13, w23 = multiverse_game_recursion(
            wins, scores, position, 3, player, roll_number + 1
        )
        player1_wins = w11 + w12 + w13
        player2_wins = w21 + w22 + w23
    else:
        scores[player] += position[player]
        if game_over(scores):
            return wins[0] + scores[0] > 1000, scores[1] > 1000
        player = (player + 1) % 2
        w11, w21 = multiverse_game_recursion(
            wins, scores, position, 1, player, roll_number=1
        )
        w12, w22 = multiverse_game_recursion(
            wins, scores, position, 2, player, roll_number=1
        )
        w13, w23 = multiverse_game_recursion(
            wins, scores, position, 3, player, roll_number=1
        )
        player1_wins = w11 + w12 + w13
        player2_wins = w21 + w22 + w23
    return player1_wins, player2_wins


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 21 Part 2 - Dirac Dice. As you experiment with the die, you feel a
    # little strange. An informational brochure in the compartment explains
    # that this is a quantum die: when you roll it, the universe splits into
    # multiple copies, one copy for each possible outcome of the die. In this
    # case, rolling the die always splits the universe into three copies: one
    # where the outcome of the roll was 1, one where it was 2, and one where it
    # was 3.
    #
    # The game is played the same as before, although to prevent things from
    # getting too far out of hand, the game now ends when either player's score
    # reaches at least 21. Using your given starting positions, determine every
    # possible outcome. Find the player that wins in more universes; in how
    # many universes does that player win?

    # Read starting positions.
    player1_start = int(lines[0][-1])
    player2_start = int(lines[1][-1])

    scores = [0, 0]
    position = [player1_start, player2_start]
    dice_side = 0  # 1-100
    wins = [0, 0]

    # Play game.
    player = 0  # 0 = player1, 1 = player2
    player1_wins, player2_wins = multiverse_game_recursion(
        wins, scores, position, dice_side, player, roll_number=1
    )

    solution = player1_wins if player1_wins > player2_wins else player2_wins
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
