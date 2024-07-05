class TicTacToe:
    def __init__(self):
        self.board = {
            'top-a': ' ', 'top-b': ' ', 'top-c': ' ',
            'mid-a': ' ', 'mid-b': ' ', 'mid-c': ' ',
            'bot-a': ' ', 'bot-b': ' ', 'bot-c': ' '
        }
        self.current_player = 'X'

    # Print the current state of the board
    def print_board(self):
        print(f" {self.board['top-a']} | {self.board['top-b']} | {self.board['top-c']} ")  # Top row
        print("---+---+---")
        print(f" {self.board['mid-a']} | {self.board['mid-b']} | {self.board['mid-c']} ")  # Middle row
        print("---+---+---")
        print(f" {self.board['bot-a']} | {self.board['bot-b']} | {self.board['bot-c']} ")  # Bottom row
        print()

    # Print the board with labels
    def print_initial_board(self):
        print("Initial Board Layout:")
        print(" top-a | top-b | top-c ")
        print("-------+-------+-------")
        print(" mid-a | mid-b | mid-c ")
        print("-------+-------+-------")
        print(" bot-a | bot-b | bot-c ")
        print()

    # Define all possible winning conditions
    def check_winner(self):
        win_conditions = [
            ['top-a', 'top-b', 'top-c'], ['mid-a', 'mid-b', 'mid-c'], ['bot-a', 'bot-b', 'bot-c'],  # Horizontal
            ['top-a', 'mid-a', 'bot-a'], ['top-b', 'mid-b', 'bot-b'], ['top-c', 'mid-c', 'bot-c'],  # Vertical
            ['top-a', 'mid-b', 'bot-c'], ['top-c', 'mid-b', 'bot-a']  # Diagonal
        ]

        # Check if the current player meets any winning condition
        for condition in win_conditions:
            if all(self.board[pos] == self.current_player for pos in condition):
                return True
        return False

    # Check if all positions are filled, indicating a tie
    def check_tie(self):
        return all(value != ' ' for value in self.board.values())

    # Prompt the player to make a move and validate the input
    def player_move(self):
        valid_moves = "top-a, top-b, top-c, mid-a, mid-b, mid-c, bot-a, bot-b, bot-c"
        while True:
            move = input(f"Turn to Player {self.current_player}, Move to which space? ({valid_moves}): ")
            if move in self.board:
                if self.board[move] == ' ':
                    self.board[move] = self.current_player
                    break
                else:
                    print("The position is already occupied. Try again.")
            else:
                print("Invalid move. Try again.")
            print()

    # Switch the current player from X to O or O to X
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    # Reset the game
    def reset_game(self):
        self.board = {
            'top-a': ' ', 'top-b': ' ', 'top-c': ' ',
            'mid-a': ' ', 'mid-b': ' ', 'mid-c': ' ',
            'bot-a': ' ', 'bot-b': ' ', 'bot-c': ' '
        }
        self.current_player = 'X'

    # Main game loop
    def play(self):
        self.print_initial_board()  # Print the initial board layout
        while True:
            self.print_board()
            self.player_move()
            if self.check_winner():
                self.print_board()
                print(f"Congratulations, Player {self.current_player} wins!")
                break
            if self.check_tie():
                self.print_board()
                print("Draw!")
                break
            self.switch_player()
        while True:
            restart = input("Would you like to play again? (type 'r' to restart, 'q' to quit): ")
            if restart.lower() == 'r':
                self.reset_game()
                self.play()
                break
            elif restart.lower() == 'q':
                print("Thank you for playing!")
                break
            else:
                print("Invalid input. Please type 'r' or 'q'.")
