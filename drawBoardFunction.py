"""Draw a board."""


def drawBoard(board):
    """Drawing a board."""
    print('   1 2 3')
    for rowNumber, row in enumerate(board):
        print(str(rowNumber + 1) + ' ', end='')
        for cell in row:
            if cell == 'empty':
                print('| ', end='')
            elif cell == 'cross':
                print('|x', end='')
            elif cell == 'circle':
                print('|o', end='')
        print('|')
