# Mario Granados
# Assignment 1
# First Grader Math Tool

# import
import random


# function that randomly adds or subtracts
def calculate_answer(x, y, operator):
    # Perform addition or subtraction based on the operator.
    return x + y if operator == 0 else x - y


# this function is just used
def get_operator_symbol(operator):
    # Return the operator symbol based on the operator value.
    return "+" if operator == 0 else "-"


# main function
def main():
    print("Welcome to my Math Game!\n")
    print('Type "quit" at any time to stop playing.\n')
    # this loop will continue until the words 'quit' are entered by the user
    while True:
        # Generate two random numbers
        x, y = random.randint(0, 100), random.randint(0, 100)

        # due to our function doing x - y, we need to ensure that X > Y to avoid negative numbers
        # this if statement just swaps the variables to avoid negative numbers
        if y > x:
            x, y = y, x

        # Randomly select an operation: 0 for '+', 1 for '-'
        operator = random.randint(0, 1)
        # used for formatting only
        symbol = get_operator_symbol(operator)

        print(f"What is {x} {symbol} {y}?")
        user_input = input("Your answer: ")
        # if user enters 'quit' or any form of 'QUIT' we stop playing
        if user_input.lower() == "quit":
            print("Thanks for playing! Have a nice day!")
            break
        # if user enters a number we can begin checking if they are correct
        if user_input.isdigit():
            user_answer = int(user_input)
            correct_answer = calculate_answer(x, y, operator)

            if user_answer == correct_answer:
                print(f"Good job! The answer is {correct_answer}.\n")
            else:
                print(
                    f"Not quite. The correct answer is {correct_answer}, you entered {user_answer}.\n"
                )
        # if user does not enter number or does not enter 'quit' then we remind user of correct inputs
        else:
            print('Invalid input. Please enter a number or type "quit" to exit.\n')


main()
