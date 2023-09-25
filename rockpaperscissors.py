#"This is a rock paper scissors game"
import random, time, sys

score_human = 0
score_comp = 0
no = int(input("Enter the number of times you want to play this game: "))
plays = ["rock", "paper", "scissors"]

while no > 0:
    play = random.choice(plays)
    response = input("Enter your choice: ").lower()
    
    if response not in plays:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    print(f"Computer's choice: {play}")
    
    if play == response:
        print("Draw")
    elif (play == "rock" and response == "scissors") or \
         (play == "scissors" and response == "paper") or \
         (play == "paper" and response == "rock"):
        print("Computer wins")
        score_comp += 1
    else:
        print("You win")
        score_human += 1
    
    no -= 1

print(f"Your score: {score_human} Computer score: {score_comp}")
