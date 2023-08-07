import random
# -----------------------------------------------
print("Welcome to the Rock-Paper-Scissors Game!")
# -----------------------------------------------------
user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print("""
Winning Rules:
1. Rock crushes Scissors
2. Scissors cut Paper
3. Paper covers Rock
""")

print("Choices are:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

while True:
    choice = int(input("Enter your choice from 1 to 3: "))
    print()

    if choice > 3 or choice < 1:
        print("Invalid input. Please enter a valid choice (1-3).")
        continue
    else:
        break

if choice == 1:
    user_choice = "Rock"
elif choice == 2:
    user_choice = "Paper"
else:
    user_choice = "Scissors"

print("Your choice is", user_choice)
print("Now it's the Computer's turn")

computer = random.randint(1, 3)
if computer == 1:
    comp_choice = "Rock"
elif computer == 2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissors"

print("Computer's choice is", comp_choice)

if ((user_choice == "Rock" and comp_choice == "Scissors") or
    (user_choice == "Scissors" and comp_choice == "Paper") or
    (user_choice == "Paper" and comp_choice == "Rock")):
    print("Congratulations! You win!")
    result = "Win"
    user_score += 1
elif user_choice == comp_choice:
    print("It's a tie! Both you and the computer chose", user_choice)
    result = "Tie"
    ties += 1
else:
    print("Sorry, you lose. The computer wins!")
    result = "Loss"
    comp_score += 1

print("\nScores:")
print(name + "'s score is", user_score)
print("Computer's score is", comp_score)
print("Ties are", ties)


# ---------------------------------------
