"""Process whole players move."""
from drawBoardFunction import drawBoard
from validateMoveFunction import validateMove
from selectFieldFunction import selectField


def processMove(playerInfo, board):
    """Process player's move."""
    correctMove = False
    while correctMove is False:
        selectedField = input(playerInfo['nick' + str(playerInfo['starter'])] +
                              ' choose field to attack (ex. "1 2"): ')
        selectedField = list(map(int, selectedField.split()))
        selectedField = [number - 1 for number in selectedField]
        if validateMove(selectedField, board):
            board = selectField(selectedField, playerInfo, board)
            drawBoard(board)
            correctMove = True
            if playerInfo['starter'] == 1:
                playerInfo['starter'] = 2
            else:
                playerInfo['starter'] = 1
    return board
