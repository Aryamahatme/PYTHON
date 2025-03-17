import random

def game(comp, you):
    if comp == you:
        return None  # Tie
    elif (comp == "S" and you == "W") or (comp == "W" and you == "G") or (comp == "G" and you == "S"):
        return False  # You lose
    else:
        return True  # You win

print("Computer's turn: Snake(S) Water(W) Gun(G)?")
randnum = random.randint(1, 3)
comp = "S" if randnum == 1 else "W" if randnum == 2 else "G"  # Assign computer's choice

you = input("Player's turn: Snake(S) Water(W) Gun(G)? ").strip().upper()

# Validate user input
if you not in ["S", "W", "G"]:
    print("Invalid input! Please choose 'S' for Snake, 'W' for Water, or 'G' for Gun.")
else:
    # Determine the game result
    result = game(comp, you)

    # Print choices
    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    # Print game result
    if result is None:
        print("The game is a tie!")
    elif result:
        print("You Win!")
    else:
        print("You Lose!")
