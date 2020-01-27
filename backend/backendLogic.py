'''
	Cinnamon Fresh
	Tic-Tac-Tournament
	backendLogic.py
	-----------------------------------------------------------------------
	This file allows you to play regular Tic-Tac-Toe with the BasicBoard
    class
	-----------------------------------------------------------------------
'''
# Import basic board
import BasicBoard

def main():
	'''
    	Runs a game of Tic-Tac-Toe or run test cases.

    	Arguments: 	None

    	Returns: 	None
	'''

    # Initialize class
	b = BasicBoard.BasicBoard()

    # Print board layout
	print("0", "|", "1", "|", "2")
	print("---------")
	print("3", "|", "4", "|", "5")
	print("---------")
	print("6", "|", "7", "|", "8")
	print("\n")

    # Start game loop
	while not b.checkwin():

		# Print board
		b.printboard()

        # Player's turn message
		print("Player " + str(b.turn) + "'s turn")

        # Get input
		space = input("Please enter a board location: ")
		try:
			space = int(space)
		except ValueError:
			space = -1

        # Repeat for invalid input
		while not b.validmove(space, b.turn):
			print("Invalid location")
			space = input("Please enter a board location: ")
			try:
				space = int(space)
			except ValueError:
				space = -1

        # Make move
		b.makemove(space, b.turn)

        # Change turns
		if b.turn == 1:
			b.turn = 2
		else:
			b.turn = 1
        # Add spacing
		print("\n")

    # Win message
	if b.win is None:
		print("Cat's Game!")
	else:
		print("Player", b.win, "wins!")



main()
