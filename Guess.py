#Simple Python guessing game
import random



def game():
    number = random.randint(1,100)
    attempts = 0
    while True:
        guess = int(raw_input("Take a guess: "))
        attempts += 1
        if guess > number:
            print "Your number is too high! Try again."
        elif guess < number:
            print "Your number is too low! Try again."
        else:
            print "You guessed it! The number was", number
            print "And it only took you", attempts, "tries!\n"
            playAgain = raw_input("Play again? Y/N: ").lower()
            if playAgain == "y" or playAgain == "yes":
                game()
            else:
                raise SystemExit ("Thanks for playing!")
            
        if  attempts == 10:
            print "You have made 10 attempts, game over."
            playAgain = raw_input("Play again? Y/N: ").lower()
            if playAgain == "y" or playAgain == "yes":
                game()
            else:
                raise SystemExit ("Thanks for playing!")
            
#Start-up
print "Welcome to the guessing game!"
print "Guess a number between 1 and 100! Let's start!"
game()