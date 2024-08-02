def display_tokens(red_tokens, blue_tokens):
    print(f"Red tokens: {red_tokens}, Blue tokens: {blue_tokens}")

def player_turn(player, red_tokens, blue_tokens):
    print(f"Player {player}'s turn")
    color = input("Choose a color (red/blue): ").strip().lower()
    while color not in ["red", "blue"]:
        color = input("Invalid color. Choose a color (red/blue): ").strip().lower()
    count = int(input(f"How many {color} tokens to remove? "))
    if color == "red":
        red_tokens -= count
    else:
        blue_tokens -= count
    return red_tokens, blue_tokens

def check_winner(red_tokens, blue_tokens):
    if red_tokens == 0 and blue_tokens == 0:
        return True
    return False

def red_blue_nim_game():
    red_tokens = int(input("Enter number of red tokens: "))
    blue_tokens = int(input("Enter number of blue tokens: "))
    current_player = 1
    
    while True:
        display_tokens(red_tokens, blue_tokens)
        red_tokens, blue_tokens = player_turn(current_player, red_tokens, blue_tokens)
        
        if check_winner(red_tokens, blue_tokens):
            print(f"Player {current_player} wins!")
            break
        
        current_player = 2 if current_player == 1 else 1

# Run the game
red_blue_nim_game()
