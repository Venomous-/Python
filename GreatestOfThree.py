#Ask for three numbers, declare the greatest
global num1, num2, num3
num1 = 0
num2 = 0
num3 = 0

def input1():
    global num1
    try:
        number1 = int(raw_input("Enter your first number: "))
        num1 = number1
        input2()
    except ValueError:
        print "Numbers only please!"
        input1()
def input2():
    global num2
    try:
        number2 = int(raw_input("Enter your second number: "))
        num2 = number2
        input3()
    except ValueError:
        print "Numbers only, please!"
        input2()
def input3():
    global num3
    try:
        number3 = int(raw_input("Enter your third number: "))
        num3 = number3
    except ValueError:
        print "Numbers only, please!"
        input3()

input1()
greatest = max(num1, num2, num3)
print "The greatest of the three numbers is {0}!".format(greatest)