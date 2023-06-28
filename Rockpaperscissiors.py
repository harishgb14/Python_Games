import random

def play():
    user=input("Whats your choise?")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return "Its a tie"
    elif (user=='p' and computer=='r') or (user=='s' and computer=='p') or\
        (user=='r' and computer=='s'):
            return "You won!"
    else:
        return "Computer won!"

print(play())