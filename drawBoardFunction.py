"""Draw a board."""


def drawBoard(board):
    """Drawing a board."""
    for row in board:
        for cell in row:
            if cell == 'empty':
                print('| ', end='')
            elif cell == 'cross':
                print('|x', end='')
            elif cell == 'circle':
                print('|o', end='')
        print('|')
