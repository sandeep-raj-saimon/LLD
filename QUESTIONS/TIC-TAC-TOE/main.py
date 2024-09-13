class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol  # Either 'X' or 'O'


class Board:
    def __init__(self):
        # Initialize a 3x3 board with empty cells
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        print("Board:")
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_full(self) -> bool:
        # Check if the board is completely filled
        return all(cell != ' ' for row in self.board for cell in row)

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        # Place the symbol in the specified row and column if the cell is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        else:
            print("Cell is already occupied, try another move.")
            return False

    def check_winner(self, symbol: str) -> bool:
        # Check rows, columns, and diagonals for a winner
        for row in self.board:
            if all([cell == symbol for cell in row]):
                return True

        for col in range(3):
            if all([self.board[row][col] == symbol for row in range(3)]):
                return True

        # Check diagonals
        if all([self.board[i][i] == symbol for i in range(3)]) or all([self.board[i][2 - i] == symbol for i in range(3)]):
            return True

        return False


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0  # Index of the current player in the `players` list

    def play(self):
        # Main game loop
        print("Tic-Tac-Toe Game Started!")
        self.board.display_board()

        while not self.board.is_full():
            current_player = self.players[self.current_turn]
            print(f"{current_player.name}'s turn ({current_player.symbol})")

            # Get move from player
            row, col = self.get_move()

            if self.board.make_move(row, col, current_player.symbol):
                self.board.display_board()

                if self.board.check_winner(current_player.symbol):
                    print(f"Congratulations {current_player.name}! You have won the game.")
                    return

                # Switch turns between players
                self.current_turn = 1 - self.current_turn
            else:
                print("Invalid move, try again.")

        print("It's a draw! The board is full.")

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")


# Example usage:
if __name__ == "__main__":
    player1 = Player("Alice", "X")
    player2 = Player("Bob", "O")
    game = Game(player1, player2)
    game.play()
