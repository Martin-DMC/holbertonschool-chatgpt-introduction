#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-----------")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return not check_winner(board)
started = "X"

def tic_tac_toe():
    global started
    board = [[" "]*3 for _ in range(3)]
    player = started
    while not check_winner(board) and not check_draw(board):
        print_board(board)
        intentos = 0
        while intentos < 3:
            try:
                row_str = input(f"Enter row (0, 1, or 2) for player {player}: ")
                row = int(row_str)
                if 0 <= row <= 2:
                    break
                else:
                    print("number not valid")
                    intentos += 1
            except ValueError:
                print("Invalid input. please enter a number.")
                intentos += 1
            if intentos == 3:
                print(f"player {player} don't play, BUUHH LOSER!!")
                print_board(board)
                return
            if intentos > 0:
                continue
        while True:
            try:
                col_str = input(f"Enter column (0, 1, or 2) for player {player}: ")
                col = int(col_str)
                if 0 <= col <= 2:
                    break
                else:
                    print("number not valid")
                    intentos += 1
            except ValueError:
                print("Invalid input. please enter a number.")
                intentos += 1
            if intentos >= 3:
                print(f"player {player} don't play, BUUHH LOSER!!")
                print_board(board)
                return
            if intentos > 0 and intentos < 3:
                continue
            elif intentos >= 3:
                break
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if check_winner(board):
            win = "O" if started == player else started
            print(f"Player {win} wins!")
    elif check_draw(board):
        print("It's a draw")
        if started == "X":
            started = "O"
        else:
            started = "X"
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            tic_tac_toe()

tic_tac_toe()
