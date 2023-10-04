from random import choice

print ("Let's Play Jokenpo!")

player_wins = 0
computer_wins = 0


def player():
    player_choice = input("Rock, Paper or Scissors? ")
    player_choice.lower()
    if player_choice == "rock":
        return player_choice
    elif player_choice == "paper":
        return player_choice
    elif player_choice == "scissors":
        return player_choice
    else:
        print("Invalid Option! Try Again")
        player()


def computer():
    player_choice = choice(["rock", "paper", "scissors"])
    return player_choice

while True:
    print("-"*70)
    player_choice = player()
    computer_choice = computer()
    print("-"*70)

    if (player_choice == "rock") and (computer_choice == "scissors") \
        or (player_choice == "paper") and (computer_choice == "rock") \
            or (player_choice == "scissors") and (computer_choice == "paper"):
        # Player Wins
        print(f"Player choice is {player_choice} and Computer Choise is {computer_choice} Result: You Won!")
        player_wins +=1
    elif player_choice == computer_choice:
        # Draw
        print(f"Player choice is {player_choice} and Computer Choise is {computer_choice} Result: Draw!")
    else:
        # Computer Wins
        print(f"Player choice is {player_choice} and Computer Choise is {computer_choice} Result: You Lost!")
        computer_wins +=1


    print("-"*70)
    print(f"Player WIns: {player_wins}")
    print(f"Computer Wins: {computer_wins}")
    print("-"*70)

    player_choice = input("Play Again? ")
    if player_choice in ["YES", "Yes",  "yes", "Y", "y"]:
        pass
    elif player_choice in ["NO", "No", "no", "N", "n"]:
        break
    else:
        break
