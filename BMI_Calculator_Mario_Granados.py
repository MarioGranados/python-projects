# Mario Granados
# BMI Calculator
import datetime


# class Member with initializer
class Member:
    def __init__(self, name, birth_year, weight_pounds, height_inches):
        self.name = name
        self.birth_year = birth_year
        self.weight_pounds = weight_pounds
        self.height_inches = height_inches

    # Calculate the age of the individual by grabing the year and subtracting it from the birth year
    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year

    # setter for weight
    def update_weight(self, weight_pounds):
        self.weight_pounds = weight_pounds

    # calculate bmi by converting weight in kilograms, and height in meters
    def calculate_bmi(self):
        # math formula
        weight_kg = self.weight_pounds * 0.45359237
        height_m = self.height_inches * 0.0254
        bmi = weight_kg / (height_m**2)
        return bmi

    # determine if the person is overweight, underweight, normal etc..
    def bmi_interpretation(self):
        # for readablility
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    # for formatting purposes
    def __str__(self):
        return f"The BMI for {self.name} ({self.get_age()}) is {self.calculate_bmi():.2f} - {self.bmi_interpretation()}"


# Testing class
class Test:
    def __init__(self):
        # create some member objects and assign values
        self.member1 = Member("John Wick", 1990, 180, 70)
        self.member2 = Member("Steven Strange", 1985, 150, 64)
        self.member3 = Member("Peter Parker", 1979, 180, 65)

    def run_test(self):
        print(self.member1)
        print(self.member2)
        print(self.member3)


# Running the test
def main():
    test = Test()
    test.run_test()


main()
