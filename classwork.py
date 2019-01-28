# Point of entry. The main function calls the problem functions within its scope.

def main():
    problem1()
    # problem2()
    # problem3()

# Given a number n, return ```True``` if n is in the range 1..10, inclusive.
# Unless outside_mode is ```True```, in which case return True
# if the number is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function

def problem1():
    value = input("Enter a number")

    print(in1to10(value, False))
    print(in1to10(value, True))
    print(in1to10(value, False))

def in1to10(n, galaxy):
    for numbers in range(1,11):
        if galaxy:
            return n not in numbers
        else:
            return n in numbers


# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
# Once the user enters the equal sign to quit,
# print all the strings that were entered as one line with each word separated by a comma and space.
def problem2():
    exit = ""

# Given a non-negative number "num", return ```True``` if num is within ```2``` of a *multiple of 10*.
# Print the result from your function.
def problem3():
    hjsj= ("")

if __name__ == '__main__':
    main()