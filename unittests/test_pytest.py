test_module = __import__("day 19")
from test_module import day19_part1 as test_code

# from .day 19 import day19_part1 as test_code

# Rotate point tests
# rotate_point(point: tuple, rotation: int, axis: int) -> tuple
print(f"test_code: {test_code}")


def test_rotate_zero():
    assert test_code.rotate_point((1, 2, 3), 0, 0) == (1, 2, 3)


def test_rotate_90_origin():
    # x, y, z = (0,0,0)
    assert test_code.rotate_point((0, 0, 0), 1, 0) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 1, 1) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 1, 2) == (0, 0, 0)


def test_rotate_90_x():
    # x, y, z = (1,0,0)
    assert test_code.rotate_point((1, 0, 0), 1, 0) == (1, 0, 0)
    assert test_code.rotate_point((1, 0, 0), 1, 1) == (0, 0, -1)
    assert test_code.rotate_point((1, 0, 0), 1, 2) == (0, 1, 0)


def test_rotate_90_y():
    # x, y, z = (0,1,0)
    assert test_code.rotate_point((0, 1, 0), 1, 0) == (0, 0, 1)
    assert test_code.rotate_point((0, 1, 0), 1, 1) == (0, 1, 0)
    assert test_code.rotate_point((0, 1, 0), 1, 2) == (-1, 0, 0)


def test_rotate_90_z():
    # x, y, z = (0,0,1)
    assert test_code.rotate_point((0, 0, 1), 1, 0) == (0, -1, 0)
    assert test_code.rotate_point((0, 0, 1), 1, 1) == (1, 0, 0)
    assert test_code.rotate_point((0, 0, 1), 1, 2) == (0, 0, 1)


def test_rotate_180_origin():
    # x, y, z = (0,0,0)
    assert test_code.rotate_point((0, 0, 0), 2, 0) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 2, 1) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 2, 2) == (0, 0, 0)


def test_rotate_180_x():
    # x, y, z = (1,0,0)
    assert test_code.rotate_point((1, 0, 0), 2, 0) == (1, 0, 0)
    assert test_code.rotate_point((1, 0, 0), 2, 1) == (-1, 0, 0)
    assert test_code.rotate_point((1, 0, 0), 2, 2) == (-1, 0, 0)


def test_rotate_180_y():
    # x, y, z = (0,1,0)
    assert test_code.rotate_point((0, 1, 0), 2, 0) == (0, -1, 0)
    assert test_code.rotate_point((0, 1, 0), 2, 1) == (0, 1, 0)
    assert test_code.rotate_point((0, 1, 0), 2, 2) == (0, -1, 0)


def test_rotate_180_z():
    # x, y, z = (0,0,1)
    assert test_code.rotate_point((0, 0, 1), 2, 0) == (0, 0, -1)
    assert test_code.rotate_point((0, 0, 1), 2, 1) == (0, 0, -1)
    assert test_code.rotate_point((0, 0, 1), 2, 2) == (0, 0, 1)


def test_rotate_270_origin():
    # x, y, z = (0,0,0)
    assert test_code.rotate_point((0, 0, 0), 3, 0) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 3, 1) == (0, 0, 0)
    assert test_code.rotate_point((0, 0, 0), 3, 2) == (0, 0, 0)


def test_rotate_270_x():
    # x, y, z = (1,0,0)
    assert test_code.rotate_point((1, 0, 0), 3, 0) == (1, 0, 0)
    assert test_code.rotate_point((1, 0, 0), 3, 1) == (0, 0, 1)
    assert test_code.rotate_point((1, 0, 0), 3, 2) == (0, -1, 0)


def test_rotate_270_y():
    # x, y, z = (0,1,0)
    assert test_code.rotate_point((0, 1, 0), 3, 0) == (0, 0, -1)
    assert test_code.rotate_point((0, 1, 0), 3, 1) == (0, 1, 0)
    assert test_code.rotate_point((0, 1, 0), 3, 2) == (1, 0, 0)


def test_rotate_270_z():
    # x, y, z = (0,0,1)
    assert test_code.rotate_point((0, 0, 1), 3, 0) == (0, 1, 0)
    assert test_code.rotate_point((0, 0, 1), 3, 1) == (-1, 0, 0)
    assert test_code.rotate_point((0, 0, 1), 3, 2) == (0, 0, 1)
