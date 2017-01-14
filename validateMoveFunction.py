"""Validate players move."""


def validateMove(field, board):
    """Check if move can be processed."""
    if field[0] >= len(board) or field[1] >= len(board[0]):
        return False
    return board[field[0]][field[1]] == 'empty'
