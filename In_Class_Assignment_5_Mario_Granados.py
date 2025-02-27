#Mario Granados
#In Class Assignment 5

# class Mean with meal parameter and __str__ formatter
class Meal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# class ToGoBox that grabs object Meal and a string customer name
class ToGoBox:
    def __init__(self, meal, customer_name):
        self.Meal = meal
        self.customer_name = customer_name
#getter for Meal in the ToGoBox
    def get_meal(self):
        return self.Meal
#getter for customer in the TogoBox
    def get_customer_name(self):
        return self.customer_name

#class Cheff that takes in a meal and customer name, it also returns the ToGoBox object
class Chef:
    def make_to_go_order(self, meal_name, customer_name):
        meal = Meal(meal_name)
        return ToGoBox(meal, customer_name)

# main
def main():
    # grab the meal name
    meal_name = input("Please enter the name of your meal: ")
    # grab customer name
    customer_name = input("And please enter who this meal is for: ")

    # create Chef object
    chef = Chef()
    # make_to_go_order method is executed. This creates meal = Meal() object and passes meal_name
    # then we return and create a ToGoBox() object with the meal object we made and pass a customer name
    # we store this into the to_go_order method which gets us the ToGoBox Object
    to_go_order = chef.make_to_go_order(meal_name, customer_name)
    # the ToGoBox object has getters so we use those here for formatting
    print(f"{to_go_order.get_customer_name()} ordered {to_go_order.get_meal()}.")

main()