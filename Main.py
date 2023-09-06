import random
import Winner as winner

def get_random_user() -> str:
    # Returns a random user to start the game
    users = ["X", "O"]
    user = random.choice(users)
    return user

def display_board() -> bool:
    # Will add the users spot to a list
    board = []
    for _ in range(3):
        board.extend(["_" for _ in range(3)])
    
    for key, value in game_slots.items():
        slot = key - 1
        if 0 <= slot < len(board) and board[slot] == '_':
            board[slot] = value

    for i in range(0, len(board), 3):
        print('|'.join(board[i:i+3]))

def validate_input(self) -> bool:
    # Validates that the user input meets requirements
    if self < min_spot or self > max_spot or type(self) != int:
        print(error_message)
        return False
    elif self in game_slots:
        print("That slot is already in use!") 
        return False
    else:
        return True
    
def check_for_winner(self: str) -> ():
    # Checks to see if anyone has won or if a draw happens
    global game_over
    global winner_scores
    global rounds_played

    board = [
        [game_slots.get(3 * i + j + 1, "_") for j in range(3)]
        for i in range(3)
    ]

    win_state = winner.is_winner(board, self)
    if win_state:
        print(self, "has won the game!")
        winner_scores[self] += 1
        rounds_played += 1
        game_over = True
        print("Rounds played:", rounds_played)
        for k, v in winner_scores.items():
            print("Wins for", f"'{k}'" + ":", v)
        return

    if len(game_slots) == 9 and not game_over:
        print("The game was a draw!")
        game_over = True
        rounds_played += 1
        print("Rounds played:", rounds_played)
        for k, v in winner_scores.items():
            print("Wins for", f"'{k}'" + ":", v)
    
def get_input(self: str):
    # Gets spot input of current user 
    spot = None
    spot = int(input(f'User "{self}" choose a spot between 1-9: '))

    if not validate_input(spot):
        get_input(self)
    else:
        game_slots[spot] = self
        display_board()
        check_for_winner(self)

def handle_user_state():
    # Handles the inputs of users 
    global current_user
    global game_started

    if not game_started:
        game_started = True
        current_user = get_random_user()
    else:
        if current_user != None:
            if current_user == 'X':
                current_user = 'O'
            else:
                current_user = 'X'
    get_input(current_user)

def handle_end_game_input() -> bool:
    global game_started
    global game_over
    global current_user
    global game_slots
    
    user_input = input("Do you want to play another game? y/n: ").lower()
    if user_input == "n":
        return False
    elif user_input == "y":
        game_started = False
        game_over = False
        current_user = None
        game_slots = {}
    else:
        print(error_message)
        return handle_end_game_input()
    return True

# Integers
min_spot = 1
max_spot = 9
rounds_played = 0

# Booleans
game_started = False

# None Datatypes
current_user = None
game_over = False

# Dictionaries
winner_scores = {'X': 0, 'O': 0}   
game_slots = {}

# Strings
error_message = "Invalid input, try again"

# Continues games until told to stop
while True:
    if game_over:
        if not handle_end_game_input():
            break
            
    handle_user_state()