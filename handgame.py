# Initialize hand values and game_end flag
p1h1, p1h2, p2h1, p2h2 = 1, 1, 1, 1
game_end = False

# Function to check if a player has lost
def check_loss(hand1, hand2):
    if hand1 == 0 and hand2 == 0:
        return True
    else:
        return False

# Function to update a player's hand value after an attack
def update_hand(player_hand, opponent_hand):
    player_hand += opponent_hand
    if player_hand >= 5:
        player_hand -= 5
    return player_hand

print("The point of this game is to disable the other player's hand by making the number of fingers they're holding up equal to 5.")
print("When you attack, you add the number of fingers on the attacking hand to the attacked hand.")
# Main game loop
while not game_end:
    # Display hand values
    print(f" {p2h1}        {p2h2} \n\n\n\n {p1h1}        {p1h2} \n\n")
    
    # Player 1's turn
    which_hand_attacks = input("Player 1, do you want to attack with your left or right hand? (l/r): ")
    which_hand_attacked = input("Player 1, do you want to attack the left or right hand? (l/r): ")
    if which_hand_attacks == "l":
        if which_hand_attacked == "l":
            p2h1 = update_hand(p2h1, p1h1)
        elif which_hand_attacked == "r":
            p2h2 = update_hand(p2h2, p1h1)
    elif which_hand_attacks == "r":
        if which_hand_attacked == "l":
            p2h1 = update_hand(p2h1, p1h2)
        elif which_hand_attacked == "r":
            p2h2 = update_hand(p2h2, p1h2)
    if check_loss(p2h1, p2h2):
        game_end = True
        break
        
    # Display hand values
    print(f" {p1h1}        {p1h2} \n\n\n\n {p2h1}        {p2h2} \n\n")
    
    # Player 2's turn
    which_hand_attacks = input("Player 2, do you want to attack with your left or right hand? (l/r): ")
    which_hand_attacked = input("Player 2, do you want to attack the left or right hand? (l/r): ")
    if which_hand_attacks == "l":
        if which_hand_attacked == "l":
            p1h1 = update_hand(p1h1, p2h1)
        elif which_hand_attacked == "r":
            p1h2 = update_hand(p1h2, p2h1)
    elif which_hand_attacks == "r":
        if which_hand_attacked == "l":
            p1h1 = update_hand(p1h1, p2h2)
        elif which_hand_attacked == "r":
            p1h2 = update_hand(p1h2, p2h2)
    if check_loss(p1h1, p1h2):
        game_end = True
print("Game over!")
