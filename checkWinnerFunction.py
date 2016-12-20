"""Check if someone had a winning move."""


def checkRow(board, weapon):
    winner = False
    for row in board:
        elements = set(row)
        if len(elements) == 1 and 'empty' not in elements:
            winner = True
    return winner


def checkColumn(board, weapon):
    # Build columns to check
    columnsAsRows = [[0 for
                     x in range(len(board))] for y in range(len(board))]
    for rowNumber, row in enumerate(board):
        for columnNumber, column in enumerate(row):
            columnsAsRows[columnNumber][rowNumber] = column
    return checkRow(columnsAsRows, weapon)


def checkAcross(board, weapon):
    return False


def checkWinner(board, weapon):
    """Check if someone won."""
    if checkRow(board, weapon):
        print(weapon.capitalize() + ' has a row and won!!!')
        return True
    elif checkColumn(board, weapon):
        print(weapon.capitalize() + ' has a column and won!!!')
        return True
    elif checkAcross(board, weapon):
        print(weapon.capitalize() + ' has a diagonal and won!!!')
        return True
    return False
