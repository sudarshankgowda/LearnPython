import random

def guess(x):
    print("User will guess the correct number")
    rand_num = random.randint(0, x)
    guess = 0
    while rand_num != guess:
        guess = int(input(f"Guess the element betweeen 0 and {x}:" ))
        if guess > rand_num:
            print("Sorry, Entered element is too High")
        elif guess < rand_num:
            print("Sorry, Entered element is too Low")
    print(f"Hurray, You entered the number {guess} correctly!!!")

def computer_guess(x):
    print("Computer will guess the correct number")
    low = 1
    high = x
    feedback = ""
    guessed_number = 0
    while feedback != 'c':
        if low != high:
            guessed_number = random.randint(low, high)
        else:
            guessed_number = low

        feedback = input(f"Is {guessed_number} is too High('H'), or its too Low('L') or its correct ('c') : ".lower())
        if feedback == 'h':
            high = guessed_number-1
        elif feedback == 'l':
            low = guessed_number+1
    
    print(f"yes, Computer guessed the number {guessed_number} correctly ")


computer_guess(1000)
#guess(100)