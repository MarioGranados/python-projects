def main():
    # continue to ask user for number until user enters a number loop
    while True:
        # user enters number
        number = input("Enter a number")
        # if user enters a number we break loop and convert the input (string) into an int
        if number.isdigit():
            number = int(number)
            break
        else:
            # if user enters anything but a number we ask again until number is entered
            print("please enter a number, try again!")

    # if number is divisible by 3 and 5 it is divisible by 15. no modulus remainder
    if number % 3 == 0 and number % 5 == 0:
        print("number is divisible by 15")
    # if number is divisible by 3 print message etc..
    elif number % 3 == 0:
        print("number is divisibile by 3")
    elif number % 5 == 0:
        print("number is divisible by 5")
    else:
        print("number is not divisible by 3 or 5")


main()
