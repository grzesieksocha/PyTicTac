"""Check if there are still possible move."""


def checkIfGameEnded(board):
    """Check if there are any moves left."""
    for row in board:
        for cell in row:
            if cell == 'empty':
                return False
    print('Game ended!!! It\'s a tie!')
    return True
