from TicTacToe_player import drawBoard, check_turn, check_for_win
import os

spots = { 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7',
         8 : '8', 9 : '9'}


playing = True
turn = 0
complete = False
prev_num = -1

while playing:  
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    resets the screen
    """

    drawBoard(spots)
    if prev_num == turn:

        """
        If a invalid turn occured let the player know
        """

        print("Invalid spot selected, please pick another.")
    prev_num = turn
    print("Player " + str((turn % 2) + 1) +"'s turn: Pick your spot or press q to quit")
    choice = input()

    """
    Get Input
    from User
    """

    if choice == 'q':
        playing = False

    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "0"}:

            """
            Valid input update the board
            """

            turn += 1
        spots[int(choice)] = check_turn(turn)
        """
        Check if the game has ended
        """

        if check_for_win(spots): playing, complete = False, True
        if turn > 8: playing = False
        """
        Checks if there's a tie
        """

os.system('cls' if os.name == 'nt' else 'clear')
"""Out of the loop, print the results"""

drawBoard(spots)
"""Draw the board one last time"""

if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!")
    else: print("Player 2 Wins!")
    """If there was a winner, say who won"""
else:
    print("No Winner!")
""" It's a Tie Game"""

print("Thanks for playing!")