'''
	Cinnamon Fresh
	Tic-Tac-Tournament
	FullBoard.py
	-----------------------------------------------------------------------
	The class that stores and handles information for an instance of
    Ultimate Tic-Tac-Toe.
	-----------------------------------------------------------------------
	Sources:
		1. 	https://www.geeksforgeeks.org/print-without-newline-python/
        2.  https://theasciicode.com.ar/extended-ascii-code/top-half-block-ascii-code-223.html
'''
# Import basic board
import BasicBoard
class FullBoard:
    def __init__(self):
        '''
        Creates variables for a FullBoard instance

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
        self.board = [BasicBoard.BasicBoard(), BasicBoard.BasicBoard(), BasicBoard.BasicBoard(),
                      BasicBoard.BasicBoard(), BasicBoard.BasicBoard(), BasicBoard.BasicBoard(),
                      BasicBoard.BasicBoard(), BasicBoard.BasicBoard(), BasicBoard.BasicBoard()]

        # Set containing possible boards that the player can play on
        self.moves = {0, 1, 2, 3, 4, 5, 6, 7, 8}

    def printwin(self):
        '''
        Prints the win status for each BasicBoard in self.board

        Arguments: 	None

        Returns: 	None
        '''
        for i in range(9):
            print(str(i) + ":", self.board[i].win)

    def printboard(self):
        '''
        Prints out a visual for the current instance of FullBoard

        Arguments: 	None

        Returns: 	None
        '''
        for i in range(3):
            print(self.board[3*i].board[0], "|", self.board[3*i].board[1], "|", self.board[3*i].board[2], end="")
            print(" ■ ", end="")
            print(self.board[3*i+1].board[0], "|", self.board[3*i+1].board[1], "|", self.board[3*i+1].board[2], end="")
            print(" ■ ", end="")
            print(self.board[3*i+2].board[0], "|", self.board[3*i+2].board[1], "|", self.board[3*i+2].board[2])
            print("----------■-----------■-----------")
            print(self.board[3*i].board[3], "|", self.board[3*i].board[4], "|", self.board[3*i].board[5], end="")
            print(" ■ ", end="")
            print(self.board[3*i+1].board[3], "|", self.board[3*i+1].board[4], "|", self.board[3*i+1].board[5], end="")
            print(" ■ ", end="")
            print(self.board[3*i+2].board[3], "|", self.board[3*i+2].board[4], "|", self.board[3*i+2].board[5])
            print("----------■-----------■-----------")
            print(self.board[3*i].board[6], "|", self.board[3*i].board[7], "|", self.board[3*i].board[8], end="")
            print(" ■ ", end="")
            print(self.board[3*i+1].board[6], "|", self.board[3*i+1].board[7], "|", self.board[3*i+1].board[8], end="")
            print(" ■ ", end="")
            print(self.board[3*i+2].board[6], "|", self.board[3*i+2].board[7], "|", self.board[3*i+2].board[8])
            if i != 2:
                print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

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
            for i in range(9):
                self.board[i].players.append(ID)
            if (len(self.players) == 2):
                self.running = True
                self.turn_ID = self.players[self.turn]
                self.other_ID = self.players[self.turn+1]
            for i in range(9):
                self.board[i].turn_ID = self.turn_ID
                self.board[i].other_ID = self.other_ID
            return True

    def checkwin(self):
        '''
        Checks the win conditions for this instance of FullBoard and updates win to the
        name of the winning player if someone has won. Returns True of someone has won and false otherwise

        Arguments: 	None

        Returns: 	Bool
        '''
        for i in range(9):
            self.board[i].checkwin()
        for i in range(0, 2, 1):
            # Check horizontal
            if ((self.board[0].win == self.players[i] and self.board[1].win == self.players[i] and self.board[2].win == self.players[i]) or
                (self.board[3].win == self.players[i] and  self.board[4].win == self.players[i] and self.board[5].win == self.players[i]) or
                (self.board[6].win == self.players[i] and self.board[7].win == self.players[i] and self.board[8].win == self.players[i])):
                self.win = self.players[i]
                if self.win == None:
                    return False
                return True

            # Check vertical
            if ((self.board[0].win == self.players[i] and self.board[3].win == self.players[i] and self.board[6].win == self.players[i]) or
                (self.board[1].win == self.players[i] and  self.board[4].win == self.players[i] and self.board[7].win == self.players[i]) or
                (self.board[2].win == self.players[i] and self.board[5].win == self.players[i] and self.board[8].win == self.players[i])):
                self.win = self.players[i]
                if self.win == None:
                    return False
                return True
            # Check diagonal
            if ((self.board[0].win == self.players[i] and self.board[4].win == self.players[i] and self.board[8].win == self.players[i]) or
                (self.board[2].win == self.players[i] and  self.board[4].win == self.players[i] and self.board[6].win == self.players[i])):
                self.win = self.players[i]
                if self.win == None:
                    return False
                return True
        return False

    def checkfull(self):
        '''
        Checks if all of the spaces on the board have been filled.
        Returns True if the have and False otherwise.

        Arguments: 	None

        Returns: 	Bool
        '''
        for i in range(9):
            if self.board[i].checkfull() == False and self.board[i].checkwin() == False:
                return False
        return True

    def validmove(self, index, space, player_id):
        '''
        Checks if the given move is a legal move according to the game rules.
        Returns True if the player can make the move, False otherwise

        Arguments: 	index = The board that the move is made on
                    space = The space on the board
                    player_id = The name of the player that is making the move

        Returns: 	Bool
        '''
        if self.win != None:
            return [False, "Game is over"]
        elif self.turn_ID != player_id:
            return [False, str(player_id), False]
        elif index not in self.moves:
            return [False, "Not valid board"]
        else:
            return self.board[index].validmove(space, player_id)

    def makemove(self, index, space, player_id):
        '''
        Makes a move at a given space if it is valid and return True if the move was made.
        Return False if the move is invalid.

        Arguments: 	None

        Returns: 	Bool
        '''
        if type(self.validmove(index, space, player_id)) is list:
            return False
        elif self.validmove(index, space, player_id):
            self.board[index].makemove(space, self.turn, player_id)
            # If the board is full or won let the player play on another playable board
            if self.board[space].checkfull() or self.board[space].checkwin():
                self.moves = {0, 1, 2, 3, 4, 5, 6, 7, 8}
                for i in range(9):
                    if self.board[i].checkfull() or self.board[i].checkwin():
                        self.moves.remove(i)
            # If not, the player has to play on the specified board
            else:
                self.moves = {space}
            return True
        return False

    def changeturn(self):
        '''
        Change the turns in this instance of FullBoard.
        Returns False when there is an error.

        Arguments: 	None

        Returns: 	None/Bool
        '''
        if (self.turn == 0):
            self.turn = 1
            self.turn_ID = self.players[1]
            self.other_ID = self.players[0]
            for i in range(9):
                self.board[i].turn = 1
                self.board[i].turn_ID = self.players[1]
                self.board[i].other_ID = self.players[0]
        elif (self.turn == 1):
            self.turn = 0
            self.turn_ID = self.players[0]
            self.other_ID = self.players[1]
            for i in range(9):
                self.board[i].turn = 0
                self.board[i].turn_ID = self.players[0]
                self.board[i].other_ID = self.players[1]
        else:
            print("Error changing turn")
            return False

    def getCurrentState(self):
        '''
        Returns the current board state

        Arguments: 	None

        Returns: 	BasicBoard[]
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
        self.moves = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        for i in range(9):
            self.board[i].clearState()

    def getCurrentPlayer(self):
        '''
        Retreive current player | 1 -> player 1 | 2 -> player 2 |

        Arguments: 	None

        Returns: 	int
        '''
        return self.turn

    def getTurn_ID(self):
        '''
		Retreive ID of current player

		Arguments:	None

		Returns:	this.turn_ID (str)
		'''
        return self.turn_ID
        
    def getOther_ID(self):
        '''
		Retreive ID of other player

		Arguments:	None

		Returns:	this.other_ID (str)
		'''
        return self.other_ID
        
    def setCurrentPlayer(self, player):
        '''
        Player setter function

        Arguments: 	None

        Returns: 	integer
        '''
        self.turn = player
        for i in range(9):
            self.board[i].turn=player
