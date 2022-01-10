RUN_TEST = False
TEST_SOLUTION = 739785
TEST_INPUT_FILE = "test_input_day_21.txt"
INPUT_FILE = "input_day_21.txt"

ARGS = []


def game_over(scores):
    return scores[0] >= 1000 or scores[1] >= 1000


def losing_player_score(scores):
    return scores[0] if scores[0] < scores[1] else scores[1]


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 21 Part 1 - Dirac Dice. The submarine computer challenges you to a
    # nice game of Dirac Dice. This game consists of a single die, two pawns,
    # and a game board with a circular track containing ten spaces marked 1
    # through 10 clockwise. Each player's starting space is chosen randomly
    # (your puzzle input). Player 1 goes first.
    #
    # Players take turns moving. On each player's turn, the player rolls the
    # die three times and adds up the results. Then, the player moves their
    # pawn that many times forward around the track (that is, moving clockwise
    # on spaces in order of increasing value, wrapping back around to 1 after
    # 10). So, if a player is on space 7 and they roll 2, 2, and 1, they would
    # move forward 5 times, to spaces 8, 9, 10, 1, and finally stopping on 2.
    #
    # After each player moves, they increase their score by the value of the
    # space their pawn stopped on. Players' scores start at 0. So, if the first
    # player starts on space 7 and rolls a total of 5, they would stop on space
    # 2 and add 2 to their score (for a total score of 2). The game immediately
    # ends as a win for any player whose score reaches at least 1000.
    #
    # Since the first game is a practice game, the submarine opens a
    # compartment labeled deterministic dice and a 100-sided die falls out.
    # This die always rolls 1 first, then 2, then 3, and so on up to 100, after
    # which it starts over at 1 again. Play using this die.
    #
    # Play a practice game using the deterministic 100-sided die. The moment
    # either player wins, what do you get if you multiply the score of the
    # losing player by the number of times the die was rolled during the game?

    # Read starting positions.
    player1_start = int(lines[0][-1])
    player2_start = int(lines[1][-1])

    scores = [0, 0]
    position = [player1_start, player2_start]
    dice_side = 0  # 1-100
    dice_rolls = 0
    # Play game.
    player = 0  # 0 = player1, 1 = player2
    while not game_over(scores):
        sum_rolls = 0
        for _ in range(3):
            # new_roll = (i - 1) % n + 1, i-1 would then be the previous roll.
            dice_side = (dice_side) % 100 + 1
            sum_rolls += dice_side
        dice_rolls += 3
        # Same logic as for rolls.
        position[player] = ((position[player] + sum_rolls) - 1) % 10 + 1
        scores[player] += position[player]
        player = (player + 1) % 2

    solution = losing_player_score(scores) * dice_rolls
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
