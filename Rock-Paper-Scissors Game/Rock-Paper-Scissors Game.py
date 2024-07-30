import random
print("All the best!")
options = ("rock", "paper", "scissors")
running = True

while running:
    You = None
    computer = random.choice(options)

    while You not in options:
        You = input("Enter a choice to win this game (rock, paper, scissors): ")

    print(f"You: {You}")
    print(f"Computer: {computer}")

    if You == computer:
        print("It's a tie!")
    elif You == "rock" and computer == "scissors":
        print("You win!")
    elif You == "paper" and computer == "rock":
        print("You win!")
    elif You == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")