RUN_TEST = False
TEST_SOLUTION = 40
TEST_INPUT_FILE = "test_input_day_15.txt"
INPUT_FILE = "input_day_15.txt"

ARGS = []

from queue import PriorityQueue
from typing import get_args

# Define the heuristic function.
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# Get the neighbors of the current node.
def get_neighbors(current: tuple, graph: dict, max_x: int, max_y: int) -> list:
    # Get neighbors north, south, west and east (not diagonally).
    neighbors = []
    if current[1] > 0:
        neighbors.append((current[0], current[1] - 1))
    if current[1] < max_y - 1:
        neighbors.append((current[0], current[1] + 1))
    if current[0] > 0:
        neighbors.append((current[0] - 1, current[1]))
    if current[0] < max_x - 1:
        neighbors.append((current[0] + 1, current[1]))
    return neighbors


# Reconstruct the path.
def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# Define the Astar search function.
def astar(graph: dict, start: tuple, goal: tuple, max_x: int, max_y: int) -> list:
    # Initialize the frontier.
    frontier = PriorityQueue()
    frontier.put(start, 0)
    # Initialize the came_from map.
    came_from = {}
    came_from[start] = None
    # Initialize the cost_so_far map.
    cost_so_far = {}
    cost_so_far[start] = 0
    # While the frontier is not empty.
    while not frontier.empty():
        # Get the current node.
        current = frontier.get()
        # If the current node is the goal, return the path.
        if current == goal:
            break
        # Get the neighbors of the current node.
        neighbors = get_neighbors(current, graph, max_x, max_y)
        # For each neighbor.
        for next in neighbors:
            # Calculate the new cost.
            new_cost = cost_so_far[current] + graph[next]
            # If the new cost is less than the current cost, update the cost.
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # Calculate the priority.
                priority = new_cost + heuristic(goal, next)
                # Add the neighbor to the frontier.
                frontier.put(next, priority)
                # Update the came_from map.
                came_from[next] = current
    # Return the path.
    return reconstruct_path(came_from, start, goal)


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 15 Part 1 - Chiton pathfinding. You start in the top left position,
    # your destination is the bottom right position, and you cannot move
    # diagonally. The number at each position is its risk level; to determine
    # the total risk of an entire path, add up the risk levels of each position
    # you enter (that is, don't count the risk level of your starting position
    # unless you enter it; leaving it adds no risk to your total). Your goal is
    # to find a path with the lowest total risk. What is the lowest total risk
    # of any path from the top left to the bottom right?

    # Can use Astar to find the path with the lowest risk.
    # Define the map as a dictionary of (x,y) tuples to risk values.
    risk_map = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            risk_map[(x, y)] = int(char)

    # Define the start and goal positions.
    start = (0, 0)
    goal = (len(lines[0]) - 1, len(lines) - 1)

    # Find the path with the lowest risk.
    path = astar(risk_map, start, goal, len(lines[0]), len(lines))

    # Calculate the total risk of the path.
    total_risk = 0
    for x, y in path:
        total_risk += risk_map[(x, y)]
    # Subract the risk of the starting position.
    total_risk -= risk_map[start]

    solution = total_risk
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
