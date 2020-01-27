'''
	Cinnamon Fresh
	Tic-Tac-Tournament
	BasicBoard.py
	-----------------------------------------------------------------------
	The class that stores and handles information for an instance of
	regular Tic-Tac-Toe.
	-----------------------------------------------------------------------
'''
class BasicBoard:
	def __init__(self):
		'''
        Creates variables for a BasicBoard instance

        Arguments: 	None

        Returns: 	None
        '''
		# Player who has won
		self.win = None
		# List of players
		self.players = []
		# Player index of whose turn it is
		self.turn = 0
		# Player's ID whose turn it is
		self.turn_ID = None
		# Other player's ID
		self.other_ID = None
		# Keeps track of when there's enough players connected to start
		self.running = False
		# Board array
		self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		'''
		board index mapping
		0 | 1 | 2
		---------
		3 | 4 | 5
		---------
		6 | 7 | 8
		'''

	def printboard(self):
		'''
        Prints out a visual for the current instance of BasicBoard

        Arguments: 	None

        Returns: 	None
        '''
		print(self.board[0], "|", self.board[1], "|", self.board[2])
		print("---------")
		print(self.board[3], "|", self.board[4], "|", self.board[5])
		print("---------")
		print(self.board[6],  "|", self.board[7], "|", self.board[8])

	def addplayer(self, ID):
		'''
        Adds a player to the game. Returns True if successful,
		False if there ar too many players.

        Arguments: 	ID = The name of the player being added to the game

        Returns: 	Bool
        '''
		if (len(self.players) >= 2):
			return False
		else:
			self.players.append(ID)
			if (len(self.players) == 2):
				self.running = True
				self.turn_ID = self.players[self.turn]
				self.other_ID = self.players[self.turn+1]
			return True

	def checkwin(self):
		'''
        Checks the win conditions for this instance of BasicBoard and updates win to the
        name of the winning player if someone has won. Returns True of someone has won and false otherwise

        Arguments: 	None

        Returns: 	Bool
        '''
		for i in range(1, 3, 1):
			# Check horizontal
			if ((self.board[0] == i and self.board[1] == i and self.board[2] == i) or
				(self.board[3] == i and  self.board[4] == i and self.board[5] == i) or
				(self.board[6] == i and self.board[7] == i and self.board[8] == i)):
				self.win = self.players[i-1]
				return True

			# Check vertical
			if ((self.board[0] == i and self.board[3] == i and self.board[6] == i) or
				(self.board[1] == i and  self.board[4] == i and self.board[7] == i) or
				(self.board[2] == i and self.board[5] == i and self.board[8] == i)):
				self.win = self.players[i-1]
				return True
			# Check diagonal
			if ((self.board[0] == i and self.board[4] == i and self.board[8] == i) or
				(self.board[2] == i and  self.board[4] == i and self.board[6] == i)):
				self.win = self.players[i-1]
				return True
		return False

	# Returns True if the board is full, false otherwise
	def checkfull(self):
		'''
        Checks if all of the spaces on the board have been filled.
        Returns True if the have and False otherwise.

        Arguments: 	None

        Returns: 	Bool
        '''
		for i in range(9):
			if self.board[i] == 0:
				return False
		return True

	# Check if move is valid
	def validmove(self, space, player_id):
		'''
        Checks if the given move is a legal move according to the game rules.
        Returns True if the player can make the move, False otherwise

        Arguments: 	space = The space on the board
                    player_id = The name of the player that is making the move

        Returns: 	Bool
        '''
		# Not the player's turnw
		if self.turn_ID != player_id:
			#print("Not " + str(player_id) +"'s turn.")
			return [False, "Not " + str(player_id) + "'s turn"]

		if space > 8 or space < 0:
			return False

		# Space already taken
		if self.board[space] != 0:
			return [False, "Space taken"]

		# A player has already won
		if self.win != None:
			return [False, "Game is over"]

		# Player can place here
		return True

	# Check if move is valid and make move if it is
	def makemove(self, space, player_index, player_id):
		'''
        Makes a move at a given space if it is valid and return True if the move was made.
        Return False if the move is invalid.

        Arguments: 	None

        Returns: 	Bool
        '''
		# Check for validity
		if type(self.validmove(space, player_id)) is list:
			return self.validmove(space, player_id)
		elif self.validmove(space, player_id):
			# Make move
			self.board[space] = player_index+1
			return True
		# Move wasn't possible
		return  False

	def changeturn(self):
		'''
        Change the turns in this instance of BasicBoard.
        Returns False when there is an error.

        Arguments: 	None

        Returns: 	None/Bool
        '''
		if (self.turn == 0):
			self.turn = 1
			self.turn_ID = self.players[1]
			self.other_ID = self.players[0]
		elif (self.turn == 1):
			self.turn = 0
			self.turn_ID = self.players[0]
			self.other_ID = self.players[1]
		else:
			print("Error changing turn")
			return False

	def getCurrentState(self):
		'''
        Returns the board array.

        Arguments: 	None

        Returns: 	int[]
        '''
		return self.board

	def clearState(self):
		'''
        Resets the state of the board to starting conditions

        Arguments: 	None

        Returns: 	None
        '''
		self.win = None
		self.players = []
		self.turn = 0
		self.turn_ID = None
		self.other_ID = None
		self.running = False
		self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	def getCurrentPlayer(self):
		'''
        Retreive current player | 1 -> player 1 | 2 -> player 2 |

        Arguments: 	None

        Returns: 	int
        '''
		return self.turn

	def getTurn_ID(self):
		'''
		Retreive current player ID

		Arguments:	None

		Returns:	self.turn_ID (str)
		'''
		return self.turn_ID

	def getOther_ID(self):
		'''
		Retreive other player ID

		Arguments:	None

		Returns:	self.other_ID (str)
		'''
		return self.other

	def setCurrentPlayer(self, player):
		'''
		Player setter function

		Arguments: 	None

		Returns: 	integer
		'''
		self.turn = player
