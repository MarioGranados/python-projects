# Mario Granados
# In class assignmnet 3

import datetime


# class
class Loan:
    # initializer
    def __init__(self, amount, years, annual_rate):
        self.amount = amount
        self.years = years
        self.annual_rate = annual_rate
        self.date_taken = datetime.date.today()

    # getters
    def get_amount(self):
        return self.amount

    def get_years(self):
        return self.years

    def get_annual_rate(self):
        return self.annual_rate

    def get_date_taken(self):
        return self.date_taken

    # formula that was provided on the for monthly payments
    def calculate_monthly_payment(self):
        monthly_rate = (self.annual_rate / 100) / 12
        months = self.years * 12
        monthly_payment = (self.amount * monthly_rate * (1 + monthly_rate)) / (
            months * ((1 + monthly_rate) - 1)
        )
        return monthly_payment

    # formulat for total payments
    def calculate_total_payment(self):
        return self.calculate_monthly_payment() * self.years * 12


def main():
    # Im not going to check if numbers because im going to assume we will put numbers otherwise the program will break
    # I can do a while loop that keeps asking for isdigit() but I keep doing that in assigmnets alot

    # grab user inputs
    # I could of used setters, but im going to assume the proper values are going to be entered
    # Setters would be cool to determine that the user is using ints instead of some other value
    loan_amount = input("Enter a loan amount: ")
    years = input("Enter for how many years: ")
    annual_rate = input("Enter an annual rate: ")
    # date will be initialized whenever we create the object Loan
    print("I will now grab todays date and do some math stuff!\n")

    # assume the user is cool and wont break my program
    loan = Loan(int(loan_amount), int(years), int(annual_rate))

    # format print stuff here
    print(
        f"This is a student loan for ${loan.get_amount():.2f} taken out on {loan.get_date_taken()}."
    )
    print(
        f"This loan will be taken out for {loan.get_years()} at {loan.get_annual_rate()}%."
    )
    print(f"The monthly payments will be ${loan.calculate_monthly_payment():.2f}.")
    print(f"The total payment will be ${loan.calculate_total_payment():.2f}.")


main()
