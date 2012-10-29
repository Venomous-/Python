loop = 0

while loop == 0:
    exp = raw_input("Enter Equation: ")
    print(eval(exp))
    loop = 1
    while loop == 1:
        again = raw_input("Another Question (Y/N): ").lower()
        if again == "y" or again == "yes":
            loop = 0
        elif again == "n" or again == "no":
            raise SystemExit("Good Bye")
        else:
            print "Not a valid option; try again."
            loop = 1