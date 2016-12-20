"""Tic tac toe game."""
from checkWinnerFunction import checkWinner
from createBoardFunction import createBoard
from checkIfGameEndedFunction import checkIfGameEnded
from beginGameFunction import beginGame
from processMoveFunction import processMove
from drawBoardFunction import drawBoard


def main():
    """Main program."""
    board = createBoard(3, 3)
    playerInfo = beginGame()
    if playerInfo['starter'] == 1:
        weapon = playerInfo['weapon1']
    else:
        weapon = playerInfo['weapon2']
    drawBoard(board)
    while checkIfGameEnded(board) is False and \
            checkWinner(board, weapon) is False:
        board = processMove(playerInfo, board)

if __name__ == '__main__':
    main()
