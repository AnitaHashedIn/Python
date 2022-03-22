# You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number,
# an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1).
# Split user input using str.split(), and check whether the resulting list is valid:
# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# Try to convert the first and third input to a float (like so: float_value = float(str_value)).
# Catch any ValueError that occurs, and instead raise a FormulaError
# If the second input is not '+' or '-', again raise a FormulaError
# If the input is valid, perform the calculation and print out the result.
# The user is then prompted to provide new input, and so on, until the user enters quit.


class Error(Exception):
    """Base class for other exceptions"""
    pass

class FormulaError(Error):
    ''' raised when + and - not provided'''
    pass

while(True):
    try:
        user_input = list(input("enter the expression:").split(" "))
        print(user_input)
        if(len(user_input)!=3):
            raise FormulaError
        b = user_input[1]
        if(b !='+' and b!='-'):
            print(b)
            raise FormulaError
        a,c = float(user_input[0]), float(user_input[2])

        print(a+c)
        break
    except ValueError as er :
        print(f'input provided is not in correct format, Error:{er}')
    except FormulaError:
        print("input formula is not in correct form")

