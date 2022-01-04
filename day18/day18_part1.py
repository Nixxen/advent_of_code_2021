RUN_TEST = False
TEST_SOLUTION = 4140
TEST_INPUT_FILE = "test_input_day_18.txt"
INPUT_FILE = "input_day_18.txt"

ARGS = []

import ast
import math


class Node:
    def __init__(self, parent=None, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.exploded = False
        self.split = False

    def send_left_parent(self, value, sender=None):
        # Send the value to the left child and add it to its value,
        # as long as the sender is not the left child.
        if self.left is not None and self.left != sender:
            if self.left.value is not None:
                self.left.value += value
            else:
                self.left.send_right_child(value, sender=self)
        else:
            if self.parent is not None:
                self.parent.send_left_parent(value, sender=self)
            elif self.right == sender:
                self.left.send_right_child(value, sender=self)
            else:
                # Value is tossed.
                pass

    def send_right_parent(self, value, sender=None):
        # Send the value to the right child and add it to its value,
        # as long as the sender is not the right child.
        if self.right is not None and self.right != sender:
            if self.right.value is not None:
                self.right.value += value
            else:
                self.right.send_left_child(value, sender=self)
        else:
            if self.parent is not None:
                self.parent.send_right_parent(value, sender=self)
            elif self.left == sender:
                self.right.send_left_child(value, sender=self)
            else:
                # Value is tossed.
                pass

    def send_left_child(self, value, sender=None):
        # Called if send right parent reaches a right branch with children.
        if self.left is not None:
            if self.left.value is not None:
                self.left.value += value
            else:
                self.left.send_left_child(value, sender=self)
        else:
            if sender is not None:
                # Exhausted left child, return to sender and check right.
                sender.send_right_parent(value, sender=self)

    def send_right_child(self, value, sender=None):
        # Called if the send left parent reaches a left branch with children.
        if self.right is not None:
            if self.right.value is not None:
                self.right.value += value
            else:
                self.right.send_right_child(value, sender=self)
        else:
            if sender is not None:
                # Exhausted right child, return to sender and check left.
                sender.send_left_parent(value, sender=self)

    def explode(self):
        self.exploded = True
        self.parent.send_left_parent(self.left.value, sender=self)
        self.parent.send_right_parent(self.right.value, sender=self)
        del self.left
        del self.right
        self.left = None
        self.right = None
        self.value = 0

    def split_node(self):
        self.split = True
        self.left = Node(parent=self, value=math.floor(self.value / 2))
        self.right = Node(parent=self, value=math.ceil(self.value / 2))
        self.value = None

    def print_tree(self, level=0):
        if self.right is not None:
            self.right.print_tree(level + 1)
        if self.value is not None:
            print("\t" * level, self.value)
        else:
            print("\t" * level, "[,]")
        if self.left is not None:
            self.left.print_tree(level + 1)

    def get_as_list(self):
        if self.value is not None:
            return self.value
        else:
            return [self.left.get_as_list(), self.right.get_as_list()]

    def get_magnitude(self):
        left_magnitude = 0
        right_magnitude = 0
        if self.left.value is not None:
            left_magnitude = self.left.value * 3
        else:
            left_magnitude = self.left.get_magnitude() * 3
        if self.right.value is not None:
            right_magnitude = self.right.value * 2
        else:
            right_magnitude = self.right.get_magnitude() * 2

        return left_magnitude + right_magnitude


def add_list_to_tree(list_line, parent):
    # Recursively scan the lists until the content are a pair of numbers.
    # Add the pair to the tree as left and right nodes. Then, return the
    # current node.
    current_node = Node(parent=parent)
    if isinstance(list_line, list):
        current_node.left = add_list_to_tree(list_line[0], parent=current_node)
        current_node.right = add_list_to_tree(list_line[1], parent=current_node)
        return current_node
    else:
        current_node.value = list_line
        return current_node


def reduce_tree_explode(head: Node, depth: int) -> Node:
    # Explode any node with a depth of 4 or greater (that contain only numbers).
    if not isinstance(head.value, int):  # Node is an empty link between to children.
        if depth >= 4:
            if isinstance(head.left.value, int) and isinstance(head.right.value, int):
                head.explode()
                return head
        head.left = reduce_tree_explode(head.left, depth=depth + 1)
        if head.left.exploded:
            head.left.exploded = False
            head.exploded = True
        else:
            head.right = reduce_tree_explode(head.right, depth=depth + 1)
            if head.right.exploded:
                head.right.exploded = False
                head.exploded = True
    return head


def reduce_tree_split(head: Node) -> Node:
    # Split numbers at 10 or above.
    if isinstance(head.value, int):
        if head.value >= 10:
            head.split_node()
    else:
        head.left = reduce_tree_split(head.left)
        if head.left.split:
            head.left.split = False
            head.split = True
        else:
            head.right = reduce_tree_split(head.right)
            if head.right.split:
                head.right.split = False
                head.split = True
    return head


def reduce_tree(head: Node) -> Node:
    # Parent function for reducing the tree. First by calling the recursive
    # explode function. If any node explodes, re-call the function on the
    # parent node. If no node explodes, run the recursive split function.
    # If no node splits, return the head node. If a node splits, run the
    # recursive explode function on the parent node again.
    changed = True
    while changed:
        changed = False
        head = reduce_tree_explode(head, depth=0)
        changed = head.exploded
        if changed:
            # Something exploded, re-call the function on the parent node.
            head.exploded = False
            continue
        head = reduce_tree_split(head)
        changed = head.split
        if changed:
            # Something split, re-call the function on the parent node.
            head.split = False
            continue
        return head


def add_tree_to_tree(left_branch, right_branch) -> Node:
    # Make a new head node and add the left and right branches to it.
    head = Node()
    head.left = left_branch
    head.right = right_branch
    head.left.parent = head
    head.right.parent = head
    return head


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 18 Part 1 - Snailfish additons. To add two snailfish numbers, form a
    # pair from the left and right parameters of the addition operator. For
    # example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]]. snailfish numbers
    # must always be reduced, and the process of adding two snailfish numbers
    # can result in snailfish numbers that need to be reduced.
    #
    # To reduce a snailfish number, you must repeatedly do the first action in
    # this list that applies to the snailfish number:
    #
    # - If any pair is nested inside four pairs, the leftmost such pair
    #   explodes.
    # - If any regular number is 10 or greater, the leftmost such regular
    #   number splits.
    #
    # Once no action in the above list applies, the snailfish number has been
    # reduced.
    #
    # To explode a pair, the pair's left value is added to the first regular
    # number to the left of the exploding pair (if any), and the pair's right
    # value is added to the first regular number to the right of the exploding
    # pair (if any). Exploding pairs will always consist of two regular
    # numbers. Then, the entire exploding pair is replaced with the regular
    # number 0.
    #
    # To split a regular number, replace it with a pair; the left element of
    # the pair should be the regular number divided by two and rounded down,
    # while the right element of the pair should be the regular number divided
    # by two and rounded up.
    #
    # The snailfish numbers are each listed on a separate line. Add the first
    # snailfish number and the second, then add that result and the third, then
    # add that result and the fourth, and so on until all numbers in the list
    # have been used once.
    #
    # The magnitude of a pair is 3 times the magnitude of its left element plus
    # 2 times the magnitude of its right element. The magnitude of a regular
    # number is just that number. Magnitude calculations are recursive: the
    # magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.
    #
    # Add up all of the snailfish numbers from the homework assignment in the
    # order they appear. What is the magnitude of the final sum?

    # Parse each line into a list. Parse the list into a binary tree
    numbers = []
    for line in lines:
        list_line = ast.literal_eval(line)
        head = Node()
        head.left = add_list_to_tree(list_line[0], parent=head)
        head.right = add_list_to_tree(list_line[1], parent=head)
        head = reduce_tree(head)
        numbers.append(head)

    # Add the trees together.
    total = numbers[0]
    for number in numbers[1:]:
        total = add_tree_to_tree(total, number)
        total = reduce_tree(total)

    # Print the resulting tree.
    total.print_tree()
    print(f"As list: {total.get_as_list()}")

    # Solution is the magnitude of the tree.
    solution = total.get_magnitude()
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
