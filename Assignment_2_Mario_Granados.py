# Mario Granados
# Assignment II

# imports
import datetime


# member classs with initialization of name, year of birth, weight(in lbs), and height(in inches)
class Member:
    def __init__(self, name, year_of_birth, weight_in_pounds, height_in_inches):
        self.name = name
        self.year_of_birth = year_of_birth  
        self.weight_in_pounds = weight_in_pounds
        self.height_in_inches = height_in_inches

    # getter for name
    def get_name(self):
        return self.name

    # getter for age
    def get_age(self):
        return datetime.date.today().year - self.year_of_birth

    # update weight
    def set_weight(self, updated_weight):
        self.weight_in_pounds = updated_weight

    # updates weight to kilograms
    def weight_in_kilograms(self):
        return self.weight_in_pounds * 0.45359237

    # updates weight to meters
    def height_in_meters(self):
        return self.height_in_inches * 0.0254

    # bmi formula
    def calculate_bmi(self):
        return self.weight_in_kilograms() / (self.height_in_meters() ** 2)

    # bmi interpretation from prev asignment
    def bmi_interpretation(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    # formatter
    def __str__(self):
        return f"The BMI for {self.get_name()} ({self.get_age()}) is {self.calculate_bmi():.2f} – {self.bmi_interpretation()}"


def main():

    # date = datetime.date.today()
    # date = datetime.date(1997, 2, 19)
    # print(date.year)
    # print(datetime.date.today().year - date.year)

    # members
    member1 = Member("John Doe", 1997, 180, 70)
    member2 = Member("Jane Smith", 1995, 150, 65)
    # format print
    print(member1)
    print(member2)
    # test set weight method
    member1.set_weight(170)
    print("\nAfter weight change:")
    print(member1)


main()
