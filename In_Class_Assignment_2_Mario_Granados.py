# Mario Granados
#In-Class Assignment 2

def main():
    # create list of grades and have it empty
    grades = []

    # continue to loop until '-1' is entered
    while True:
        # asks for grade
        user_input = input("Enter a grade: ")

        # if user's input is a number we convert input to string and append it to user input
        if user_input.isdigit():
            grades.append(int(user_input))
        # if user input is '-1' we exit the loop
        elif user_input == '-1':
            break
        # if user puts anything else we display that input is invalid
        else:
            print('Not a valid input')

    # if grades list has any input we do math stuff, if not we say nothing was entered
    if grades:
        # get sum of all grades
        total = sum(grades) 
        # average formula total / number of grades
        average = total / len(grades)

        print(f'The grades are: {grades}')
        print(f'The average grade is: {average:.2f}')
    else:
        print('No grades were entered.')

main()