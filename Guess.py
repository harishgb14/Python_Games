import random
"""
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Enter the number between 1 to {x}:"))
        if guess<random_number:
            print("Wrong ,Tooooooooooooooo low")
        elif guess>random_number:
            print("Wrong, Tooooooooooooooooo high")
    print(f"yessss,You have guessed {random_number} correcty")

guess(10)
"""
def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high[h],too low[l], or correct[c]?".lower())
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Computer guessed the number {guess} correctly !")

computer_guess(100)

