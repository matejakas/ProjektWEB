import re


class Chessboard:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'W'

    def display_board(self):
        print("\n   A B C D E F G H")
        print("  -----------------")
        for i in range(8):
            print(f"{8 - i} |{' '.join(self.board[i])}| {8 - i}")
        print("  -----------------")
        print("   A B C D E F G H\n")

    def get_piece(self, position):
        row = 8 - int(position[1])
        col = ord(position[0].lower()) - ord('a')
        return self.board[row][col]

    def set_piece(self, position, piece):
        row = 8 - int(position[1])
        col = ord(position[0].lower()) - ord('a')
        self.board[row][col] = piece

    def is_valid_move(self, move):
        if not re.match(r'^[a-h][1-8] [a-h][1-8]$', move):
            return False

        from_pos, to_pos = move.split(' ')
        from_piece = self.get_piece(from_pos)
        to_piece = self.get_piece(to_pos)

        if from_piece == ' ' or (from_piece.islower() and self.current_player == 'W'):
            return False

        if to_piece != ' ' and to_piece.isupper() and self.current_player == 'W':
            return False

        return True

    def make_move(self, move):
        from_pos, to_pos = move.split(' ')
        piece = self.get_piece(from_pos)
        self.set_piece(to_pos, piece)
        self.set_piece(from_pos, ' ')

        self.current_player = 'B' if self.current_player == 'W' else 'W'


class ChessGame:
    def __init__(self):
        self.chessboard = Chessboard()

    def start(self):
        print("Welcome to Chess!")
        self.chessboard.display_board()
        self.play()

    def play(self):
        while True:
            move = input(f"{self.chessboard.current_player}'s move: ")

            if move.lower() == 'quit':
                print("Game ended.")
                break

            if move.lower() == 'options':
                self.show_options_menu()
                continue

            if not self.chessboard.is_valid_move(move):
                print("Invalid move! Please try again.")
                continue

            self.chessboard.make_move(move)
            self.chessboard.display_board()

    def show_options_menu(self):
        print("Options Menu")
        print("1. Change player names")
        print("2. Change game rules")
        print("3. Return to game")
        option = input("Select an option: ")

        if option == '1':
            white_player_name = input("Enter white player's name: ")
            black_player_name = input("Enter black player's name: ")
            print("Player names changed.")
        elif option == '2':
            print("Game rules cannot be changed in this version.")
        elif option == '3':
            return
        else:
            print("Invalid option! Please try again.")
            self.show_options_menu()


if __name__ == '__main__':
    game = ChessGame()
    game.start()
