'''
    Cinnamon Fresh
    Tic-Tac-Tournament
    backendTest.py
    -----------------------------------------------------------------------
    This file tests scenarios for both BasicBoard.py and FullBoard.py
    -----------------------------------------------------------------------
'''
# Import BasicBoard & FullBoard
import BasicBoard, FullBoard, sys, os

BACKEND_TEST_SWITCH = 2
def basicBoardTest(TestBasicBoard, p1MoveArray, p2MoveArray, expectedArray, testType, PRINT_MODE=True):
    '''
        runs a Tic-Tac-Toe game on TestBasicBoard using p1MoveArray and p2MoveArray 
        as player1's and player2's turns respectively. Compares resulting state 
        of TestBasicBoard with accurate expectedArray
        (testType can only be "P1WIN", "P2WIN", or "CAT")

        Arguments:  (BasicBoard, int[], int[], int[], str) 

        Returns:    bool
    '''


    # Clear state of TestBasicBoard. All moves will be made on TestBasicBoard
    TestBasicBoard.clearState()
    TestBasicBoard.addplayer("player1")
    TestBasicBoard.addplayer("player2")

    # Initialize testPassed as -1 by default, will change to 0 if test failed and 1 if test actually passes
    testPassed = -1
    
    # Iterate through p1 and p2 moves
    for p1Move, p2Move in zip(p1MoveArray, p2MoveArray):

        # Set current player to player 1
        TestBasicBoard.setCurrentPlayer(0)

        # If Player 1 is unable to take current turn, fail test
        try:
            TestBasicBoard.makemove(p1Move, TestBasicBoard.getCurrentPlayer(), TestBasicBoard.getTurn_ID())
        except ValueError:
            print("TEST FAILED :(")
            print("Player 1 unable to take turn")
            testPassed = 0
            break

        # Change current player to player 2
        TestBasicBoard.changeturn()

        # If Player 2 either doesn't have a turn to take or is able to take one, return False
        if(p2Move != -1):
            try:
                TestBasicBoard.makemove(p2Move, TestBasicBoard.getCurrentPlayer(), TestBasicBoard.getTurn_ID())
            except ValueError:
                print("TEST FAILED :()")
                print("Player 2 unable to take turn")
                testPassed = 0
                break

    # Retreive resulting Array
    resultArray = TestBasicBoard.getCurrentState()

    # If testType is "CAT", then fail test if TestBasicBoard has a winner
    if testType == "CAT":
        if TestBasicBoard.checkwin():
            print("TEST FAILED :(")
            print("player " + str(TestBasicBoard.getCurrentPlayer()) + " won somehow.")
            testPassed = 0

    # If testType is either "P1WIN" or "P2WIN", then fail test if TestBasicBoard has *no* winner
    elif testType == "P1WIN" or testType == "P2WIN":
        if TestBasicBoard.checkwin() == False:
            print("TEST FAILED :(")
            print("win condition not met.")
            testPassed = 0
        
    # Else throw value error
    else:
        print("INVALID testType")
        testPassed = 0


    # If the test has already failed, just return False and give results. Otherwise, compare with expected Array
    if testPassed == -1:

        # Compare resulting Array with expected Array
        for resultEntry, expectedEntry in zip(resultArray, expectedArray):
            if resultEntry != expectedEntry:
                print("TEST FAILED :(")
                testPassed = 0
                break


    # If nothing has failed at this point, then test is passed
    if testPassed != 0:            
        print("TEST PASSED :)")
        testPassed = 1

    # Print Expected Array
    print("Expected: ")
    for i in expectedArray:
        print(i, end = " ")
    print("\n")

    # Print Resulting Array
    print("Got: ")
    for j in resultArray:
        print(j, end = " ")
    print("\n")

    # Print Resulting Board
    TestBasicBoard.printboard()

    # Return bool corresponding to whether or not test passed
    if testPassed == 1:
        return True
    else:
        return False

def fullBoardTest(TestFullBoard, p1MoveArray, p2MoveArray, expectedBasicBoardArray, testType):
    '''
        Runs a Tic-Tac-Tournament game on TestFullBoard using p1MoveArray and p2MoveArray
        as player1's and player2's turns respectively. Compares resulting state
        of TestFullBoard with accurate expectedBasicBoardArray
        (testType can only be "P1WIN", "P2WIN", or "CAT")
        (set PRINT_MODE to False to suppress print statements)

        Arguments:  (FullBoard, int[][], int[][], BasicBoard[])

        Returns:    None
    '''
    # TODO: Make this work

    # Clear state of TestFullBoard. All moves will be made on TestFullBoard
    TestFullBoard.clearState()
    TestFullBoard.addplayer("player1")
    TestFullBoard.addplayer("player2")

    # Initialize testPassed as -1 by default, will change to 0 if test fails and 1 if test passes
    testPassed = -1

    # Iterate through p1 and p2 moves
    for p1Move, p2Move in zip(p1MoveArray, p2MoveArray):

        # Retreive Current BasicBoard location for p1 and p2
        p1CurrentBoard = p1Move[0]
        p2CurrentBoard = p2Move[0]

        # Retreive Current Space (on current BasicBoard) for p1 and p2
        p1CurrentSpace = p1Move[1]
        p2CurrentSpace = p2Move[1]

        # Change Turn (if necessary) and take p1's turn
        if TestFullBoard.getCurrentPlayer() != 0:
            TestFullBoard.changeturn()

        # If move is invalid, throw error and report attempted move
        if TestFullBoard.makemove(p1CurrentBoard, p1CurrentSpace, TestFullBoard.getTurn_ID()) == False:
            print("TEST FAILED :(")
            print(str(TestFullBoard.moves))
            print("p1 unable to take move: [" + str(p1CurrentBoard) + "," + str(p1CurrentSpace) + "]")
            testPassed = 0
            break

        # Change Turn and take p2's turn
        TestFullBoard.changeturn()

        if p2CurrentSpace != -1:
            # If move is invalid, throw error and report attempted move
            if TestFullBoard.makemove(p2CurrentBoard, p2CurrentSpace, TestFullBoard.getTurn_ID()) == False:
                print("TEST FAILED :(")
                print(str(TestFullBoard.moves))
                print("p2 unable to take move: [" + str(p2CurrentBoard) + "," + str(p2CurrentSpace) + "]")
                testPassed = 0
                break

    # Retreive result array of BasicBoard object and compare with expectedBasicBoardArray
    resultBasicBoardArray = TestFullBoard.getCurrentState()

    # If testType is "CAT", then fail test if TestFullBoard has win condition
    if testType == "CAT":
        if TestFullBoard.checkwin():
            print("TEST FAILED :(")
            print("player " + str(TestFullBoard.getCurrentPlayer()) + " won somehow.")
            testPassed = 0
        if not TestFullBoard.checkfull():
            print("TEST FAILED :(")
            print("Board not full")
            testPassed = 0

    # If testType is either "P1WIN" or "P2WIN", then fail test if TestFullBoard doesn't have win condition
    elif testType == "P1WIN" or testType == "P2WIN":
        if TestFullBoard.checkwin() == False:
            print("TEST FAILED :(")
            print("win condition not met.")
            testPassed = 0

    # Else throw value error
    else:
        print("INVALID testType")
        testPassed = 0

    # If the test has already failed just return False and give results. Otherwise, compare with expectedBasicBoardArray
    if testPassed == -1:

        # Compare resultBasicBoardArray with expectedBasicBoardArray
        for resultBasicBoard, expectedBasicBoard in zip(resultBasicBoardArray, expectedBasicBoardArray):
            if resultBasicBoard.getCurrentState() != expectedBasicBoard.getCurrentState():
                print("TEST FAILED :(")
                print("Resulting BasicBoard: " + str(resultBasicBoardArray.index(resultBasicBoard)) + " doesn't match Expected BasicBoard: " + str(expectedBasicBoardArray.index(expectedBasicBoard)))
                testPassed = 0
                break

    # If nothing has failed at this point, then test is passed
    if testPassed != 0:
        print("TEST PASSED :)")
        testPassed = 1

    # Print Expected BasicBoard States
    print("Expected: ")
    i = -1
    for expectedBasicBoard in expectedBasicBoardArray:
        i += 1
        print("Board " + str(i) + ": " + str(expectedBasicBoard.getCurrentState()), end = "\n")
    print("\n")

    # Print Resulting BasicBoard States
    print("Got: ")
    j = -1
    for resultBasicBoard in resultBasicBoardArray:
        j += 1
        print("Board " + str(j) + ": " + str(resultBasicBoard.getCurrentState()), end = "\n")
    print("\n")

    # Print Resulting FullBoard
    TestFullBoard.printboard()
    TestFullBoard.printwin()
    print("WIN:", TestFullBoard.win)
    # Return bool corresponding to whether or not test passed
    if testPassed == 1:
        return True
    else:
        return False

def executeBasicBoardTests():
    '''
        Tests the BasicBoard object, and prints the results of the test

        Arguments:  None

        Returns:    True if all tests pass, false otherwise
    '''

    # ------------------------------------------------------------------ #
    # ------------------- START BASIC BOARD TEST CONDITIONS ------------ #
    # ------------------------------------------------------------------ #
    
    #Initialize Test Basic Board
    TestBasicBoard = BasicBoard.BasicBoard()

    # Arrays to test against for all possible player1 wins
    BasicBoard_PlayerOneWin_LeftRow_ExpectedArray = [1, 0, 0, 1, 2, 2, 1, 0, 0]
    BasicBoard_PlayerOneWin_RightRow_ExpectedArray = [0, 0, 1, 0, 2, 1, 2, 0, 1]
    BasicBoard_PlayerOneWin_TopRow_ExpectedArray = [1, 1, 1, 0, 2, 0, 2, 0, 0]
    BasicBoard_PlayerOneWin_BottomRow_ExpectedArray = [2, 0, 0, 0, 2, 0, 1, 1, 1]
    BasicBoard_PlayerOneWin_Diagonal1_ExpectedArray = [2, 0, 1, 0, 1, 2, 1, 0, 0]
    BasicBoard_PlayerOneWin_Diagonal2_ExpectedArray = [1, 0, 0, 2, 1, 0, 2, 0 , 1]

    # Arrays to test against for all possible player2 wins
    BasicBoard_PlayerTwoWin_LeftRow_ExpectedArray = [2, 1, 0, 2, 1, 1, 2, 0, 0]
    BasicBoard_PlayerTwoWin_RightRow_ExpectedArray = [1, 0, 2, 1, 1, 2, 0, 0, 2]
    BasicBoard_PlayerTwoWin_TopRow_ExpectedArray = [2, 2, 2, 1, 1, 0, 1, 0, 0]
    BasicBoard_PlayerTwoWin_BottomRow_ExpectedArray = [0, 1, 0, 1, 0, 1, 2, 2, 2]
    BasicBoard_PlayerTwoWin_Diagonal1_ExpectedArray = [1, 1, 2, 1, 2, 0, 2, 0, 0]
    BasicBoard_PlayerTwoWin_Diagonal2_ExpectedArray = [2, 1, 0, 1, 2, 1, 0, 0, 2]

    ## Initialize test cases for general win conditions
    # ------------------ Cases where player 1 wins --------------- #
    # Left Row Win #
    BasicBoard_PlayerOneWin_LeftRow_p1 = [0, 6, 3]
    BasicBoard_PlayerOneWin_LeftRow_p2 = [4, 5, -1]

    # Right Row Win
    BasicBoard_PlayerOneWin_RightRow_p1 = [2, 5, 8]
    BasicBoard_PlayerOneWin_RightRow_p2 = [4, 6, -1]

    # Top Row Win
    BasicBoard_PlayerOneWin_TopRow_p1 = [0, 1, 2]
    BasicBoard_PlayerOneWin_TopRow_p2 = [4, 6, -1]

    # Bottom Row Win
    BasicBoard_PlayerOneWin_BottomRow_p1 = [6, 7, 8]
    BasicBoard_PlayerOneWin_BottomRow_p2 = [4, 0, -1]

    # Diagonal Win 1 (/) #
    BasicBoard_PlayerOneWin_Diagonal1_p1 = [6, 4, 2]
    BasicBoard_PlayerOneWin_Diagonal1_p2 = [0, 5, -1]

    # Diagonal Win 2 (\) #
    BasicBoard_PlayerOneWin_Diagonal2_p1 = [0, 4, 8]
    BasicBoard_PlayerOneWin_Diagonal2_p2 = [6, 3, -1]

    # ------------------------------------------------------------ #

    ### ---------------### Cases where player 2 wins ###------------ ###
    # Left Row Win #
    BasicBoard_PlayerTwoWin_LeftRow_p1 = [1, 4, 5]
    BasicBoard_PlayerTwoWin_LeftRow_p2 = [0, 3, 6]

    # Right Row Win #
    BasicBoard_PlayerTwoWin_RightRow_p1 = [0, 3, 4]
    BasicBoard_PlayerTwoWin_RightRow_p2 = [2, 5, 8]

    # Top Row Win #
    BasicBoard_PlayerTwoWin_TopRow_p1 = [3, 4, 6]
    BasicBoard_PlayerTwoWin_TopRow_p2 = [0, 1, 2]

    # Bottom Row Win #
    BasicBoard_PlayerTwoWin_BottomRow_p1 = [3, 5, 1]
    BasicBoard_PlayerTwoWin_BottomRow_p2 = [6, 7, 8]

    # Diagonal Win / #
    BasicBoard_PlayerTwoWin_Diagonal1_p1 = [0, 1, 3]
    BasicBoard_PlayerTwoWin_Diagonal1_p2 = [6, 4, 2]

    # Diagonal Win \ #
    BasicBoard_PlayerTwoWin_Diagonal2_p1 = [3, 5, 1]
    BasicBoard_PlayerTwoWin_Diagonal2_p2 = [0, 4, 8]
    # ------------------------------------------------------------ #
    ## Initialize test cases for Cat conditions
    BasicBoard_Cat_1_p1 = [4, 5, 1, 8, 6]
    BasicBoard_Cat_1_p2 = [2, 3, 7, 0, -1]
    BasicBoard_Cat_1_ExpectedArray = [2, 1, 2, 2, 1, 1, 1, 2, 1]

    BasicBoard_Cat_2_p1 = [4, 8, 3, 2, 1]
    BasicBoard_Cat_2_p2 = [7, 0, 5, 6, -1]
    BasicBoard_Cat_2_ExpectedArray = [2, 1, 1, 1, 1, 2, 2, 2, 1]

    BasicBoard_Cat_3_p1 = [0, 3, 2, 7, 8]
    BasicBoard_Cat_3_p2 = [4, 6, 1, 5, -1]
    BasicBoard_Cat_3_ExpectedArray = [1, 2, 1, 1, 2, 2, 2, 1, 1]

    
    # Counters for total number of BasicBoard tests
    BasicBoard_TestCounter_Total = 15
    BasicBoard_TestCounter_p1Win = 6
    BasicBoard_TestCounter_p2Win = 6
    BasicBoard_TestCounter_Cat = 3

    # Counters for numbers of BasicBoard test failures
    BasicBoard_TestFailCounter_p1Win = 0
    BasicBoard_TestFailCounter_p2Win = 0
    BasicBoard_TestFailCounter_Cat = 0
    BasicBoard_TestFailCounter_Total = 0

    # ---------------------------------------------------------------------------- #
    # ------------------ START P1 WIN TESTING ------------------------------------ #
    # ---------------------------------------------------------------------------- #
    print("-- STARTING P1 WIN CONDITION TESTING --")

    # ------------------------ Begin Testing Left Row Player 1 Win ---------------------- #
    print("\nTesting P1 Left Row Win...")
    print("----------------------------------------------------------")

    # Run test on Left Row Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_LeftRow_p1, BasicBoard_PlayerOneWin_LeftRow_p2, BasicBoard_PlayerOneWin_LeftRow_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #

# ------------------------ Begin Testing Right Row Player 1 Win -------------- #
    print("\nTesting P1 Right Row Win...")
    print("----------------------------------------------------------")

    # Run test on Right Row Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_RightRow_p1, BasicBoard_PlayerOneWin_RightRow_p2, BasicBoard_PlayerOneWin_RightRow_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ------------------------ Begin Testing Top Row Player 1 Win -------------- #
    print("\nTesting P1 Top Row Win...")
    print("----------------------------------------------------------")

    # Run test on Top Row Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_TopRow_p1, BasicBoard_PlayerOneWin_TopRow_p2, BasicBoard_PlayerOneWin_TopRow_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1    

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ------------------------ Begin Testing Bottom Row Player 1 Win -------------- #
    print("\nTesting P1 Bottom Row Win...")
    print("----------------------------------------------------------")

    # Run test on Bottom Row Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_BottomRow_p1, BasicBoard_PlayerOneWin_BottomRow_p2, BasicBoard_PlayerOneWin_BottomRow_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1   

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ------------------------ Begin Testing Diagonal (/) Player 1 Win -------------- #
    print("\nTesting P1 Diagonal 1 Win...")
    print("----------------------------------------------------------")

    # Run test on Diagonal (/) Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_Diagonal1_p1, BasicBoard_PlayerOneWin_Diagonal1_p2, BasicBoard_PlayerOneWin_Diagonal1_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1   

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ------------------------ Begin Testing Diagonal (\) Player 1 Win -------------- #
    print("\nTesting P1 Diagonal 2 Win...")
    print("----------------------------------------------------------")

    # Run test on Diagonal (\) Player 1 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerOneWin_Diagonal2_p1, BasicBoard_PlayerOneWin_Diagonal2_p2, BasicBoard_PlayerOneWin_Diagonal2_ExpectedArray, "P1WIN") == False:
        BasicBoard_TestFailCounter_p1Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #




# ---------------------------------------------------------------------------- #
# ------------------ START P2 WIN TESTING ------------------------------------ #
# ---------------------------------------------------------------------------- #
    print("\n\n\n")
    print("----------------------------------------------------------")
    print("---------- STARTING P2 WIN CONDITION TESTING -------------")
    print("----------------------------------------------------------")


# ----------------------- Begin Testing Left Row Player 2 Win ---------------- #
    print("\nTesting P2 Left Row Win")
    print("----------------------------------------------------------")

    # Run test on Left Row Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_LeftRow_p1, BasicBoard_PlayerTwoWin_LeftRow_p2, BasicBoard_PlayerTwoWin_LeftRow_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1   

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing Right Row Player 2 Win ---------------- #
    print("\nTesting P2 Right Row Win")
    print("----------------------------------------------------------")

    # Run test on Right Row Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_RightRow_p1, BasicBoard_PlayerTwoWin_RightRow_p2, BasicBoard_PlayerTwoWin_RightRow_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1   

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing Top Row Player 2 Win ---------------- #

    print("\nTesting P2 Top Row Win")
    print("----------------------------------------------------------")

    # Run test on Top Row Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_TopRow_p1, BasicBoard_PlayerTwoWin_TopRow_p2, BasicBoard_PlayerTwoWin_TopRow_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing Bottom Row Player 2 Win ---------------- #
    print("\nTesting P2 Bottom Row Win")
    print("----------------------------------------------------------")

    # Run test on Bottom Row Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_BottomRow_p1, BasicBoard_PlayerTwoWin_BottomRow_p2, BasicBoard_PlayerTwoWin_BottomRow_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing Diagonal 1 (/) Player 2  Win ---------------- #
    print("\nTesting P2 Diagonal 1 Win")
    print("----------------------------------------------------------")

    # Run test on Diagonal 1 (/) Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_Diagonal1_p1, BasicBoard_PlayerTwoWin_Diagonal1_p2, BasicBoard_PlayerTwoWin_Diagonal1_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing Diagonal2 Player 2 Win ---------------- #
    print("\nTesting P2 Diagonal 2 Win")
    print("----------------------------------------------------------")

    # Run test on Diagonal 2 (\) Player 2 Win
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_PlayerTwoWin_Diagonal2_p1, BasicBoard_PlayerTwoWin_Diagonal2_p2, BasicBoard_PlayerTwoWin_Diagonal2_ExpectedArray, "P2WIN") == False:
        BasicBoard_TestFailCounter_p2Win += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# ------------------ START CAT TESTING --------------------------------------- #
# ---------------------------------------------------------------------------- #

    print("\n\n\n")
    print("----------------------------------------------------------")
    print("---------- STARTING CAT CONDITION TESTING -------------")
    print("----------------------------------------------------------")

# ----------------------- Begin Testing CAT 1 CONDITION ---------------------- #
    print("\nTesting CAT 1 Condition")
    print("----------------------------------------------------------")

    # Run test on Cat 1 Condition
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_Cat_1_p1, BasicBoard_Cat_1_p2, BasicBoard_Cat_1_ExpectedArray, "CAT") == False:
        BasicBoard_TestFailCounter_Cat += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing CAT 2 CONDITION ---------------------- #
    print("\nTesting CAT 2 Condition")
    print("----------------------------------------------------------")

    # Run test on Cat 2 Condition
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_Cat_2_p1, BasicBoard_Cat_2_p2, BasicBoard_Cat_2_ExpectedArray, "CAT") == False:
        BasicBoard_TestFailCounter_Cat += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #


# ----------------------- Begin Testing CAT 3 CONDITION ---------------------- #
    print("\nTesting CAT 3 Condition")
    print("----------------------------------------------------------")

    # Run test on Cat 3 Condition
    # If test fails, increment corresponding testFail Counter
    if basicBoardTest(TestBasicBoard, BasicBoard_Cat_3_p1, BasicBoard_Cat_3_p2, BasicBoard_Cat_3_ExpectedArray, "CAT") == False:
        BasicBoard_TestFailCounter_Cat += 1 

    print("----------------------------------------------------------\n")
# ------------------------------------------------------------------------------- #
    BasicBoard_TestFailCounter_Total = BasicBoard_TestFailCounter_p1Win + BasicBoard_TestFailCounter_p2Win + BasicBoard_TestFailCounter_Cat

    print("\n\n\n")
    print("BasicBoard Testing Results")
    print("Total: " + str(BasicBoard_TestCounter_Total - BasicBoard_TestFailCounter_Total) + "/" + str(BasicBoard_TestCounter_Total) + " test cases passed.")
    print("p1 Win: " + str(BasicBoard_TestCounter_p1Win - BasicBoard_TestFailCounter_p1Win) + "/" + str(BasicBoard_TestCounter_p1Win) + " test cases passed.")
    print("p2 Win: " + str(BasicBoard_TestCounter_p2Win - BasicBoard_TestFailCounter_p2Win) + "/" + str(BasicBoard_TestCounter_p2Win) + " test cases passed.")
    print("cat: " + str(BasicBoard_TestCounter_Cat - BasicBoard_TestFailCounter_Cat) + "/" + str(BasicBoard_TestCounter_Cat) + " test cases passed.")

def executeFullBoardTests():
    '''
        Tests the FullBoard object, and prints the results of the test

        Arguments:  None

        Returns:    True if all tests pass, false otherwise
    '''
    # Initialize TeFstFullBoard "FullBoard" object
    TestFullBoard = FullBoard.FullBoard()

    # Counters for total number FullBoard tests
    FullBoard_TestCounter_Total = 6
    FullBoard_TestCounter_p1Win = 2
    FullBoard_TestCounter_p2Win = 2
    FullBoard_TestCounter_Cat = 2

    # Counters for numbers of FullBoard test failures
    FullBoard_TestFailCounter_p1Win = 0
    FullBoard_TestFailCounter_p2Win = 0
    FullBoard_TestFailCounter_Cat = 0
    FullBoard_TestFailCounter_Total = 0


    # ------------------------------------------------------------------ #
    # ------------------- START FULL BOARD TEST CONDITIONS ------------ #
    # ------------------------------------------------------------------ #

    # Initialize BasicBoards for FullBoard p1Win condition #1
    FullBoard_p1Win_1_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_p1Win_1_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate BasicBoards for FullBoard p1Win condition #1
    FullBoard_p1Win_1_ExpectedBasicBoard_0.board = [2, 0, 0, 1, 1, 1, 0, 0, 0]
    FullBoard_p1Win_1_ExpectedBasicBoard_1.board = [0, 0, 0, 1, 0, 0, 0, 0, 0]
    FullBoard_p1Win_1_ExpectedBasicBoard_2.board = [1, 2, 0, 0, 2, 0, 0, 0, 0]
    FullBoard_p1Win_1_ExpectedBasicBoard_3.board = [0, 0, 2, 0, 2, 0, 2, 0, 0]
    FullBoard_p1Win_1_ExpectedBasicBoard_4.board = [0, 0, 1, 0, 2, 1, 0, 0, 1]
    FullBoard_p1Win_1_ExpectedBasicBoard_5.board = [2, 0, 0, 0, 0, 0, 0, 0, 2]
    FullBoard_p1Win_1_ExpectedBasicBoard_6.board = [0, 0, 1, 0, 0, 0, 0, 0, 2]
    FullBoard_p1Win_1_ExpectedBasicBoard_7.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    FullBoard_p1Win_1_ExpectedBasicBoard_8.board = [1, 0, 0, 1, 2, 0, 1, 0, 0]

    FullBoard_p1Win_1_ExpectedBasicBoardArray = [FullBoard_p1Win_1_ExpectedBasicBoard_0, FullBoard_p1Win_1_ExpectedBasicBoard_1, FullBoard_p1Win_1_ExpectedBasicBoard_2, FullBoard_p1Win_1_ExpectedBasicBoard_3, FullBoard_p1Win_1_ExpectedBasicBoard_4, FullBoard_p1Win_1_ExpectedBasicBoard_5, FullBoard_p1Win_1_ExpectedBasicBoard_6, FullBoard_p1Win_1_ExpectedBasicBoard_7, FullBoard_p1Win_1_ExpectedBasicBoard_8]

    FullBoard_p1Win_1_p1 = [[0,3], [2,0], [0,4], [4,2], [4,5], [0,5], [8,3], [6,2], [1,3], [4,8], [8,6], [8,0]]
    FullBoard_p1Win_1_p2 = [[3,2], [0,0], [4,4], [2,4], [5,0], [5,8], [3,6], [2,1], [3,4], [8,4], [6,8], [-1,-1]]


# Initialize BasicBoards for FullBoard p1Win condition #2
    FullBoard_p1Win_2_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_p1Win_2_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate BasicBoards for FullBoard p1Win condition #2
    FullBoard_p1Win_2_ExpectedBasicBoard_0.board = [1, 1, 2, 2, 1, 0, 0, 1, 0]
    FullBoard_p1Win_2_ExpectedBasicBoard_1.board = [0, 0, 0, 0, 0, 0, 2, 2, 2]
    FullBoard_p1Win_2_ExpectedBasicBoard_2.board = [2, 0, 0, 0, 1, 0, 0, 0, 0]
    FullBoard_p1Win_2_ExpectedBasicBoard_3.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    FullBoard_p1Win_2_ExpectedBasicBoard_4.board = [2, 0, 0, 2, 2, 0, 2, 0, 1]
    FullBoard_p1Win_2_ExpectedBasicBoard_5.board = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    FullBoard_p1Win_2_ExpectedBasicBoard_6.board = [1, 1, 1, 0, 2, 0, 0, 0, 0]
    FullBoard_p1Win_2_ExpectedBasicBoard_7.board = [2, 0, 0, 2, 0, 0, 1, 0, 0]
    FullBoard_p1Win_2_ExpectedBasicBoard_8.board = [2, 0, 1, 0, 0, 2, 0, 1, 0]

    FullBoard_p1Win_2_ExpectedBasicBoardArray = [FullBoard_p1Win_2_ExpectedBasicBoard_0, FullBoard_p1Win_2_ExpectedBasicBoard_1, FullBoard_p1Win_2_ExpectedBasicBoard_2, FullBoard_p1Win_2_ExpectedBasicBoard_3, FullBoard_p1Win_2_ExpectedBasicBoard_4, FullBoard_p1Win_2_ExpectedBasicBoard_5, FullBoard_p1Win_2_ExpectedBasicBoard_6, FullBoard_p1Win_2_ExpectedBasicBoard_7, FullBoard_p1Win_2_ExpectedBasicBoard_8]

    FullBoard_p1Win_2_p1 = [[8,2], [0,0], [3,4], [0,1], [6,0], [2,4], [4,8], [0,7], [0,4], [3,0], [6,1], [8,7], [3,8], [5,1], [7,6], [6,2]]
    FullBoard_p1Win_2_p2 = [[2,0], [0,3], [4,0], [1,6], [0,2], [4,4], [8,0], [7,0], [4,3], [4,6], [1,8], [7,3], [8,5], [1,7], [6,4], [-1,-1]]


    # Initialize BasicBoards for p2Win condition #1
    FullBoard_p2Win_1_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_p2Win_1_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate Expected Basic Boards for FullBoard p2Win condition #1
    FullBoard_p2Win_1_ExpectedBasicBoard_0.board = [1, 1, 0, 2, 2, 2, 0, 0, 0]
    FullBoard_p2Win_1_ExpectedBasicBoard_1.board = [2, 0, 0, 2, 1, 0, 2, 0, 0]
    FullBoard_p2Win_1_ExpectedBasicBoard_2.board = [2, 1, 0, 0, 2, 0, 1, 2, 2]
    FullBoard_p2Win_1_ExpectedBasicBoard_3.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    FullBoard_p2Win_1_ExpectedBasicBoard_4.board = [0, 0, 1, 0, 1, 2, 1, 1, 2]
    FullBoard_p2Win_1_ExpectedBasicBoard_5.board = [0, 1, 0, 2, 0, 0, 0, 1, 1]
    FullBoard_p2Win_1_ExpectedBasicBoard_6.board = [0, 0, 2, 0, 1, 2, 0, 0, 2]
    FullBoard_p2Win_1_ExpectedBasicBoard_7.board = [0, 2, 2, 0, 2, 0, 0, 0, 1]
    FullBoard_p2Win_1_ExpectedBasicBoard_8.board = [0, 0, 1, 0, 2, 1, 1, 1, 2]

    FullBoard_p2Win_1_ExpectedBasicBoardArray = [FullBoard_p2Win_1_ExpectedBasicBoard_0, FullBoard_p2Win_1_ExpectedBasicBoard_1, FullBoard_p2Win_1_ExpectedBasicBoard_2, FullBoard_p2Win_1_ExpectedBasicBoard_3, FullBoard_p2Win_1_ExpectedBasicBoard_4, FullBoard_p2Win_1_ExpectedBasicBoard_5, FullBoard_p2Win_1_ExpectedBasicBoard_6, FullBoard_p2Win_1_ExpectedBasicBoard_7, FullBoard_p2Win_1_ExpectedBasicBoard_8]

    FullBoard_p2Win_1_p1 = [[0,0], [3,2], [7,8], [4,6], [2,1] ,[6,4], [5,7], [1,4], [8,5], [3,0], [5,1], [0,1], [3,1], [4,2], [8,6], [8,7], [4,7], [2,6], [5,8], [8,2], [4,4]]
    FullBoard_p2Win_1_p2 = [[0,3], [2,7], [8,4], [6,2], [1,6] ,[4,5], [7,1], [4,8], [5,3], [0,5], [1,0], [1,3], [0,4], [2,8], [6,8], [7,4], [7,2], [6,5], [8,8], [2,4], [2,0]]

    # Initialize BasicBoards for FullBoard p2Win condition #2
    FullBoard_p2Win_2_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_p2Win_2_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate BasicBoards for FullBoard p2Win condition #2
    FullBoard_p2Win_2_ExpectedBasicBoard_0.board = [0, 0, 0, 1, 1, 0, 2, 2, 2]
    FullBoard_p2Win_2_ExpectedBasicBoard_1.board = [1, 1, 2, 2, 2, 2, 1, 0, 0]
    FullBoard_p2Win_2_ExpectedBasicBoard_2.board = [2, 2, 2, 0, 1, 0, 0, 0, 0]
    FullBoard_p2Win_2_ExpectedBasicBoard_3.board = [2, 2, 0, 1, 0, 0, 0, 0, 0]
    FullBoard_p2Win_2_ExpectedBasicBoard_4.board = [1, 1, 1, 0, 0, 2, 0, 0, 2]
    FullBoard_p2Win_2_ExpectedBasicBoard_5.board = [0, 0, 1, 0, 0, 0, 0, 0, 1]
    FullBoard_p2Win_2_ExpectedBasicBoard_6.board = [1, 0, 1, 0, 2, 0, 2, 0, 0]
    FullBoard_p2Win_2_ExpectedBasicBoard_7.board = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    FullBoard_p2Win_2_ExpectedBasicBoard_8.board = [0, 0, 1, 0, 2, 0, 1, 0, 0]

    FullBoard_p2Win_2_ExpectedBasicBoardArray = [FullBoard_p2Win_2_ExpectedBasicBoard_0, FullBoard_p2Win_2_ExpectedBasicBoard_1, FullBoard_p2Win_2_ExpectedBasicBoard_2, FullBoard_p2Win_2_ExpectedBasicBoard_3, FullBoard_p2Win_2_ExpectedBasicBoard_4, FullBoard_p2Win_2_ExpectedBasicBoard_5, FullBoard_p2Win_2_ExpectedBasicBoard_6, FullBoard_p2Win_2_ExpectedBasicBoard_7, FullBoard_p2Win_2_ExpectedBasicBoard_8]

    FullBoard_p2Win_2_p1 = [[3,3], [0,4], [5,2], [2,4], [8,2], [1,0], [6,0], [7,1], [4,2], [0,3], [1,6], [4,0], [8,6], [6,2], [1,1], [5,8], [4,1]]
    FullBoard_p2Win_2_p2 = [[3,0], [4,5], [2,2], [4,8], [2,1], [0,6], [0,7], [1,4], [2,0], [3,1], [6,4], [0,8], [6,6], [1,2], [1,5], [8,4], [1,3]]


    # Initialize Expected BasicBoards for FullBoard cat 1 condition
    FullBoard_Cat_1_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_Cat_1_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate Expected Basic Boards for FullBoard cat 1 condition
    FullBoard_Cat_1_ExpectedBasicBoard_0.board = [2, 0, 1, 2, 1, 0, 1, 0, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_1.board = [0, 2, 1, 0, 1, 0, 1, 0, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_2.board = [1, 0, 2, 1, 2, 0, 2, 0, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_3.board = [0, 1, 0, 2, 2, 2, 1, 2, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_4.board = [1, 2, 0, 1, 2, 0, 1, 1, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_5.board = [2, 0, 0, 1, 1, 1, 0, 0, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_6.board = [0, 0, 2, 2, 2, 2, 0, 0, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_7.board = [1, 2, 2, 0, 2, 1, 1, 2, 0]
    FullBoard_Cat_1_ExpectedBasicBoard_8.board = [1, 2, 2, 2, 1, 1, 1, 1, 2]

    FullBoard_Cat_1_ExpectedBasicBoardArray = [FullBoard_Cat_1_ExpectedBasicBoard_0, FullBoard_Cat_1_ExpectedBasicBoard_1, FullBoard_Cat_1_ExpectedBasicBoard_2, FullBoard_Cat_1_ExpectedBasicBoard_3, FullBoard_Cat_1_ExpectedBasicBoard_4, FullBoard_Cat_1_ExpectedBasicBoard_5, FullBoard_Cat_1_ExpectedBasicBoard_6, FullBoard_Cat_1_ExpectedBasicBoard_7, FullBoard_Cat_1_ExpectedBasicBoard_8]

    FullBoard_Cat_1_p1 = [[4,0] ,[0,4], [1,4], [4,7], [2,0], [3,6], [2,3], [4,3], [7,5], [0,6], [3,1], [1,6], [4,6], [5,4], [5,3], [0,2], [1,2], [8,7], [7,6], [8,4], [5,5], [8,0], [8,5], [8,6], [7,0]]
    FullBoard_Cat_1_p2 = [[0,0], [4,1], [4,4], [7,2], [0,3], [6,2], [3,4], [3,7], [5,0], [6,3], [1,1], [6,4], [6,5], [3,5], [3,3], [2,6], [2,4], [7,4], [2,2], [8,1], [8,2], [8,8], [8,3], [7,1], [7,7]]


    # Initialize BasicBoards for FullBoard cat 2 condition
    FullBoard_Cat_2_ExpectedBasicBoard_0 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_1 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_2 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_3 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_4 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_5 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_6 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_7 = BasicBoard.BasicBoard()
    FullBoard_Cat_2_ExpectedBasicBoard_8 = BasicBoard.BasicBoard()

    # Populate BasicBoards for FullBoard cat 2 condition
    FullBoard_Cat_2_ExpectedBasicBoard_0.board = [0, 0, 0, 1, 1, 1, 0, 0, 0]
    FullBoard_Cat_2_ExpectedBasicBoard_1.board = [1, 2, 2, 2, 1, 1, 1, 1, 2]
    FullBoard_Cat_2_ExpectedBasicBoard_2.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    FullBoard_Cat_2_ExpectedBasicBoard_3.board = [2, 2, 2, 0, 0, 0, 0, 0, 0]
    FullBoard_Cat_2_ExpectedBasicBoard_4.board = [2, 0, 2, 1, 2, 0, 2, 0, 1]
    FullBoard_Cat_2_ExpectedBasicBoard_5.board = [2, 1, 1, 1, 1, 2, 2, 1, 2]
    FullBoard_Cat_2_ExpectedBasicBoard_6.board = [0, 1, 2, 1, 1, 2, 0, 0, 2]
    FullBoard_Cat_2_ExpectedBasicBoard_7.board = [1, 0, 2, 1, 2, 0, 1, 0, 0]
    FullBoard_Cat_2_ExpectedBasicBoard_8.board = [0, 2, 1, 0, 2, 0, 2, 2, 0]

    FullBoard_Cat_2_ExpectedBasicBoardArray = [FullBoard_Cat_2_ExpectedBasicBoard_0, FullBoard_Cat_2_ExpectedBasicBoard_1, FullBoard_Cat_2_ExpectedBasicBoard_2, FullBoard_Cat_2_ExpectedBasicBoard_3, FullBoard_Cat_2_ExpectedBasicBoard_4, FullBoard_Cat_2_ExpectedBasicBoard_5, FullBoard_Cat_2_ExpectedBasicBoard_6, FullBoard_Cat_2_ExpectedBasicBoard_7, FullBoard_Cat_2_ExpectedBasicBoard_8]

    FullBoard_Cat_2_p1 = [[0,5], [0,4], [0,3], [4,8], [6,4], [4,3], [2,0], [1,4], [2,4], [6,1], [2,8], [8,2], [7,0], [1,7], [5,3], [1,0], [1,6], [5,4], [1,5], [5,2], [6,3], [7,6], [7,3], [5,1], [5,7]]
    FullBoard_Cat_2_p2 = [[5,0], [4,0], [3,0], [8,6], [4,4], [3,2], [3,1], [4,2], [4,6], [1,2], [8,4], [8,7], [8,1], [7,4], [1,1], [1,8], [6,5], [1,3], [5,5], [5,6], [7,2], [6,2], [6,8], [5,8], [-1,-1]]



# ---------------------------------------------------------------------------- #
# ------------------ START p1Win TESTING ------------------------------------- #
# ---------------------------------------------------------------------------- #
    print("-- STARTING FULLBOARD p1Win CONDITION TESTING --")

# ------------------------ Begin Testing p2Win 1 Condition ---------------------- #
    print("\nTesting p1Win 1 Condition...")
    print("----------------------------------------------------------")

     # Run test on p2Win 1 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_p1Win_1_p1, FullBoard_p1Win_1_p2, FullBoard_p1Win_1_ExpectedBasicBoardArray, "P1WIN") == False:
        FullBoard_TestFailCounter_p1Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #

# ------------------------ Begin Testing p2Win 2 Condition ---------------------- #
    print("\nTesting p1Win 2 Condition...")
    print("----------------------------------------------------------")

     # Run test on p2Win 1 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_p1Win_2_p1, FullBoard_p1Win_2_p2, FullBoard_p1Win_2_ExpectedBasicBoardArray, "P1WIN") == False:
        FullBoard_TestFailCounter_p1Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# ------------------ START p2Win TESTING ------------------------------------- #
# ---------------------------------------------------------------------------- #
    print("-- STARTING FULLBOARD p2Win CONDITION TESTING --")

# ------------------------ Begin Testing p2Win 1 Condition ---------------------- #
    print("\nTesting p2Win 1 Condition...")
    print("----------------------------------------------------------")

     # Run test on p2Win 1 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_p2Win_1_p1, FullBoard_p2Win_1_p2, FullBoard_p2Win_1_ExpectedBasicBoardArray, "P2WIN") == False:
        FullBoard_TestFailCounter_p2Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #

# ------------------------ Begin Testing p2Win 2 Condition ---------------------- #
    print("\nTesting p2Win 2 Condition...")
    print("----------------------------------------------------------")

     # Run test on p2Win 2 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_p2Win_2_p1, FullBoard_p2Win_2_p2, FullBoard_p2Win_2_ExpectedBasicBoardArray, "P2WIN") == False:
        FullBoard_TestFailCounter_p2Win += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# ------------------ START CAT 1 TESTING ------------------------------------- #
# ---------------------------------------------------------------------------- #
    print("-- STARTING FULLBOARD CAT CONDITION TESTING --")

# ------------------------ Begin Testing Cat 1 Condition ---------------------- #
    print("\nTesting Cat 1 Condition...")
    print("----------------------------------------------------------")

    # Run test on Cat 1 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_Cat_1_p1, FullBoard_Cat_1_p2, FullBoard_Cat_1_ExpectedBasicBoardArray, "CAT") == False:
        FullBoard_TestFailCounter_Cat += 1

    print("----------------------------------------------------------\n")
# ---------------------------------------------------------------------------- #

# ------------------------ Begin Testing Cat 2 Condition ---------------------- #
    print("\nTesting Cat 2 Condition...")
    print("----------------------------------------------------------")

    # Run test on Cat 2 Condtion
    # If test fails, increment corresponding testFail Counter
    if fullBoardTest(TestFullBoard, FullBoard_Cat_2_p1, FullBoard_Cat_2_p2, FullBoard_Cat_2_ExpectedBasicBoardArray, "CAT") == False:
        FullBoard_TestFailCounter_Cat += 1

    print("----------------------------------------------------------\n")
# ----------------------------------------------------------------------------- #
    FullBoard_TestFailCounter_Total = FullBoard_TestFailCounter_p1Win + FullBoard_TestFailCounter_p2Win + FullBoard_TestFailCounter_Cat

    print("\n\n\n")
    print("FullBoard Testing Results")
    print("Total: " + str(FullBoard_TestCounter_Total - FullBoard_TestFailCounter_Total) + "/" + str(FullBoard_TestCounter_Total) + " test cases passed.")
    print("p1 Win: " + str(FullBoard_TestCounter_p1Win - FullBoard_TestFailCounter_p1Win) + "/" + str(FullBoard_TestCounter_p1Win) + " test cases passed.")
    print("p2 Win: " + str(FullBoard_TestCounter_p2Win - FullBoard_TestFailCounter_p2Win) + "/" + str(FullBoard_TestCounter_p2Win) + " test cases passed.")
    print("cat: " + str(FullBoard_TestCounter_Cat - FullBoard_TestFailCounter_Cat) + "/" + str(FullBoard_TestCounter_Cat) + " test cases passed.")


def main():
    '''
        Executes test sequences

        Arguments:  None

        Returns:    None
    '''
    executeBasicBoardTests()
    if(BACKEND_TEST_SWITCH == 0):
        print(executeBasicBoardTests())
    elif(BACKEND_TEST_SWITCH == 1):
        executeFullBoardTests()
    elif(BACKEND_TEST_SWITCH == 2):
        executeBasicBoardTests()
        executeFullBoardTests()

if __name__ == "__main__":
    main()
