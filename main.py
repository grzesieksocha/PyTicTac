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
    # define first weapon to move
    if playerInfo['starter'] == 1:
        weapon = playerInfo['weapon1']
    else:
        weapon = playerInfo['weapon2']
    drawBoard(board)
    # must process first move before loop
    processedMove = processMove(playerInfo, board)
    playerInfo = processedMove[0]
    board = processedMove[1]
    weapon = playerInfo['weapon' + str(playerInfo['starter'])]
    # continue playing until someone wins
    while checkIfGameEnded(board) is False and \
            checkWinner(board, weapon) is False:
        # switch players
        if playerInfo['starter'] == 1:
            playerInfo['starter'] = 2
        else:
            playerInfo['starter'] = 1
        processedMove = processMove(playerInfo, board)
        playerInfo = processedMove[0]
        board = processedMove[1]
        # update weapon
        weapon = playerInfo['weapon' + str(playerInfo['starter'])]

if __name__ == '__main__':
    main()
