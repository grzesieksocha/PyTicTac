"""Select a field with player's weapon."""


def selectField(field, playerInfo, board):
    """Select provided field on a board."""
    if playerInfo['starter'] == 1:
        board[field[0]][field[1]] = playerInfo['weapon1']
    else:
        board[field[0]][field[1]] = playerInfo['weapon2']
    return board
