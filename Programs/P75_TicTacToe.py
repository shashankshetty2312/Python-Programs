# tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |")
        print("\n")

    def make_move(self, position: int) -> bool:
        if position < 0 or position > 8:
            print("❌ Invalid position")
            return False

        if self.board[position] != " ":
            print("❌ Position already taken")
            return False

        self.board[position] = self.current_player
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> bool:
        win_patterns = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True

        return False

    def is_draw(self) -> bool:
        return " " not in self.board

    def play(self):
        print("🎮 Tic-Tac-Toe Game Start")

        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player} (0-8): "))
            except ValueError:
                print("⚠ Enter a number")
                continue

            if not self.make_move(move):
                continue

            if self.check_winner():
                self.print_board()
                print(f"🏆 Player {self.current_player} wins!")
                break

            if self.is_draw():
                self.print_board()
                print("🤝 Game Draw")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
