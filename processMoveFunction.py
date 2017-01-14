"""Process whole players move."""
from drawBoardFunction import drawBoard
from validateMoveFunction import validateMove
from selectFieldFunction import selectField
import re


def processMove(playerInfo, board):
    """Process player's move."""
    correctMove = False
    selectedField = ''
    while correctMove is False:
        while re.match("^\d\s\d$", selectedField) is None:
            selectedField = input(playerInfo['nick' +
                str(playerInfo['starter'])] + ' choose field to attack (ex. "1 2"): ')
        selectedField = list(map(int, selectedField.split()))
        selectedField = [number - 1 for number in selectedField]
        if validateMove(selectedField, board) is True:
            board = selectField(selectedField, playerInfo, board)
            drawBoard(board)
            correctMove = True
        else:
            selectedField = ''
    return playerInfo, board
