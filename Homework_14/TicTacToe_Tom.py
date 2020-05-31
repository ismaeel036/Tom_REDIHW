EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"

WIN_COMBINATION_INDICES = [
    # Complete row
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Complete column
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Complete diagonal
    [0, 4, 8],
    [2, 4, 6]
]


def initialize_board():
    board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
             EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
             EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
    return board


def display_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player, board):
    print(f"{player}, it's your turn.")
    position = input('Enter a position (1-9): ')

    #Player inputs a position (1-9). Ask while the position is not valid (check using valid_position)
    while not valid_position(position, board):
        position = input('Invalid position, enter a position (1-9): ')

    #Writes player's sign in board
    board[int(position) - 1] = player

    return board


def valid_position(position, board):

    # Checks valid position i.e. if the position is a number between 1 and 9 AND if it is empty (EMPTY_SLOT)
    if int(position) in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board[int(position) - 1] == EMPTY_SLOT:
        valid = True
    else:
        valid = False

    return valid


def switch_player(player):
    if player == X_PLAYER:
        player = O_PLAYER

        # print('change player')
    # TODO Switch the player: X --> 0 or 0 --> X
    elif player == O_PLAYER:
        player = X_PLAYER

    return player


def check_for_winner(board):
    winner = None
    filled_slots = 0

    # TODO Check if any of the players got a win combination
    # Hint: loop over WIN_COMBINATION_INDICES to check if one of the combination is X-X-X or O-O-O
    for combination in WIN_COMBINATION_INDICES:

        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[
            combination[0]] != EMPTY_SLOT:

            winner = board[combination[0]]

        elif EMPTY_SLOT not in board:
            winner = TIE

        # else:
        #  winner = None

    # TODO If there is no winner, check if all spots are filled already. This would mean tie (winner = TIE)
    # Hint: count number of filled slots

    return winner


def tic_tac_toe():
    winner = None
    game_still_going = True
    player = X_PLAYER  # X will start. TODO (optional): select who starts randomly --> do this in a separate function
    print('WELCOME TO THE GAME OF TICTACTOE\n')
    # Initialize board
    board = initialize_board()

    # TODO run this while the game is still going
    while game_still_going:

        # Display board
        display_board(board)

        # Ask the player for a valid position and write it on the board
        board = handle_turn(player, board)

        player = switch_player(player)

        # Check if there is a winner already
        winner = check_for_winner(board)
        if winner == None:
            game_still_going = True
        else:
            game_still_going = False

            # TODO stop the game if there is a winner, otherwise switch the player

    print("THE END")
    if winner == TIE:
        print("No winner, the game is a Tie")
    else:
        print(f"Congratulations player {winner}!! You won the game!")
    display_board(board)


# Start game
tic_tac_toe()
