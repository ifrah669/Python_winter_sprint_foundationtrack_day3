user_move = input("Enter your move (rock/paper/scissors): ").lower()

computer_move = "rock"

print("Your Move       :", user_move)
print("Computer Move   :", computer_move)

if user_move == computer_move:
    print("Result          : It's a Draw")
elif user_move == "paper" and computer_move == "rock":
    print("Result          : You Win")
elif user_move == "rock" and computer_move == "scissors":
    print("Result          : You Win")
elif user_move == "scissors" and computer_move == "paper":
    print("Result          : You Win")
else:
    print("Result          : You Lose")