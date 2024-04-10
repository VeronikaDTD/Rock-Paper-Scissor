import random

cpu_win = 0
user_win = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2

    cpu_picked = options[random_number]
    print(f"The CPU picked {cpu_picked}")

    if user_input == "rock" and cpu_picked == "scissors":
        print("User Wins!")
        user_win += 1
        continue
    elif user_input == "scissors" and cpu_picked == "paper":
        print("User Wins!")
        user_win += 1
        continue
    elif user_input == "paper" and cpu_picked == "rock":
        print("User Wins!")
        user_win += 1
        continue
    else:
        print("CPU Wins, You lose!")
        cpu_win += 1

print(f"You won {user_win}, time!")
print(f"The CPU won {cpu_win}, times!")
print("Goodbye!")
