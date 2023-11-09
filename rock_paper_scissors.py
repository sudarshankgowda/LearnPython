import random

def play():
    user = input("r : Rock, p : Paper, s: Scissors :")
    #r > p, p > s, s > r

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Tie"

    if is_win(user, computer):
        return "You won"

    return "You lost"

def is_win(user, computer):
    if ((user == 'r' and computer == 'p') or (user == 'p' and computer == 's') or (user == 's' and computer == 'r')):
        return True

print(play())