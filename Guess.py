import random

num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    x = int(guess)
    if x == num:
        print('You guessed right')
        break
    elif x < num:
        print('Try higher')
    elif x > num:
        print('Try lower')
