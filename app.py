import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called played (I think this supposed to say player?) starting at position 3,2
player = player.Player(3,2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    if selection =="w": 
        player.moveUp()
        board.checkMove(player.rowPosition, player.columnPosition) 
        # checkMove needs to check row and column position in order to move forward
    elif selection =="s":
        player.moveDown()
        board.checkMove(player.rowPosition, player.columnPosition)
    elif selection =="a":
        player.moveLeft()
        board.checkMove(player.rowPosition, player.columnPosition)
    elif selection == "d":
        player.moveRight()
        board.checkMove(player.rowPosition, player.columnPosition)
    else:
        print ("Invalid selection, try again")
    # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(player.rowPosition, player.columnPosition):
        print ("Congratulations! You've won the game!!")
        break
    # broke the loop if the winning condition was met