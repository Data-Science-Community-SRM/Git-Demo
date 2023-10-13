import random

def uc():
    u = input("Enter Rock, Paper, or Scissors: ")
    while u not in ["rock", "paper", "scissors"]:
        u = input("Invalid choice. Enter Rock, Paper, or Scissors: ")
    return u

def cc():
    return random.choice(["rock", "paper", "scissors"])

def win(u, c):
    if u == c:
        return "Tie"
    elif (
        (u == "rock" and c == "scissors")
        or (u == "paper" and c == "rock")
        or (u == "scissors" and c == "paper")
    ):
        return "You won"
    else:
        return "You lost"

def main():
    while True:
        u = uc()
        c = cc()
        print(f"The computer chose {c}.")
        result = win(u, c)
        print(result)

main()
