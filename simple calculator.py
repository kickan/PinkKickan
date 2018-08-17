# This is a very simple calculator
calc = input("What kind of calculation do you want to do today? \n(add, subtract, divide or multiply) Type stop to stop the calculations \n")

#create while-loop
while calc != "stop":

# Ask for number 1
    num1 = float(input("Enter the first number: "))

#ask for number 2
    num2 = float(input("Enter the seccond number: "))

# Create if-loop that connects input with calculator
    if calc == "add":
        ans = num1 + num2
    elif calc == "subtract":
        ans = num1 - num2
    elif calc == "divide":
        ans = num1 / num2
    elif calc == "multiply":
        ans = num1*num2
    else:
        print("Sorry, something has gone wrong in the calculation, please try again")

    print("The answer to your calculation is: {}".format(ans))
    print("*************************************************")
    calc = input("What kind of calculation do you want to do next? \n(add, subtract, divide or multiply) Type stop to stop the calculations \n")

print("The calculations has stopped")