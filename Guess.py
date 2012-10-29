#Simple Python guessing game
import random


number = random.randrange(100) + 1
guess = int(raw_input("Take a random guess: "))
attempts = 0

while True:
    guess = int(raw_input("Take another guess: "))
    attempts += 1
    if guess > number:
        print "Lower..."
    elif guess < number:
        print "Higher..."
    else:
        print "You guessed it! The number was", number
        print "And it only took you", attempts, "tries!\n"
        break
    if  attempts == 10:
        print "You have made 10 attempts, game over."
        break
raw_input ("\n\nPress the enter key to exit.")