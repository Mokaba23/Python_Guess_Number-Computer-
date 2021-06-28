import random

def computer_guess(x):
    low = 1
    high = x
    message = ''
    while message != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        message = input(f'Is the {guess} too low(L), too high(H) or correct(C)?').lower()
        if message == 'h':
            high -= 1
        elif message == 'l':
            low += 1
    print("Yay,the computer guessed it right")
computer_guess(10)