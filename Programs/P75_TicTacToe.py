# Author: OMKAR PATHAK (Annotated Version)

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")


def check_winner(board):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c]:
            return True
    return False


def main():
    # ❌ VIOLATION: Original used global variables (choices, winner, etc.)
    board = [str(i) for i in range(9)]
    current_player = "X"

    for turn in range(9):
        print_board(board)

        try:
            move = int(input(f"Player {current_player}: "))
            
            # ❌ VIOLATION: No bounds check in original
            if move < 0 or move > 8:
                print("Out of range")
                continue

            if board[move] in ["X", "O"]:
                print("Invalid move")
                continue

        except:
            # ❌ VIOLATION: Bare except (bad practice)
            print("Enter valid number")
            continue

        board[move] = current_player

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print("Game Draw")


if __name__ == "__main__":
    main()
