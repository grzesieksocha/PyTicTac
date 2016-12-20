"""Create board function."""


def createBoard(height, width):
    """Create an empty board."""
    return [['empty' for x in range(width)] for y in range(height)]
