'''
	Cinnamon Fresh
	Tic-Tac-Tournament
	ultimateTest.py
	-----------------------------------------------------------------------
	This file runs an instance of Ultimate Tic-Tac-Toe with the FullBoard
    class
	-----------------------------------------------------------------------
'''
# Import basic board and full board
import BasicBoard
import FullBoard

testSwitch = 1

def main():
    '''
    Runs the test cases or a game of Ultimate Tic-Tac-Toe.

    Arguments: 	None

    Returns: 	None
    '''
    full = FullBoard.FullBoard()

    full.addplayer("alpha")
    full.addplayer("beta")

    while not full.checkwin() and not full.checkfull():
        # Print board
        full.printboard()

        # Print player's turn
        print("Player " + str(full.turn) + "'s turn")

        # Get board
        board = input("Please enter a board: ")
        try:
            board = int(board)
        except ValueError:
            board = -1

        # Get board location
        space = input("Please enter a location on the board: ")
        try:
            space = int(space)
        except ValueError:
            space = -1

        while not full.validmove(board, space, full.turn_ID):
            print("Invalid location")
            # Get board
            board = input("Please enter a board: ")
            try:
                board = int(board)
            except ValueError:
                board = -1

            # Get board location
            space = input("Please enter a location on the board: ")
            try:
                space = int(space)
            except ValueError:
                space = -1

        # Make move
        full.makemove(board, space, full.turn_ID)

        # Change turns
        full.changeturn()

    if full.win is None:
        print("Cat's Game!")
    else:
        print("Player", full.win, "wins!")
    
main()