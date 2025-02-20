# Mario Granados
# In Class Assignment 4

# I was experimenting with passing objects as an instance and using the __str__ format
# pretty cool stuff


# class chef
class Chef:
    # constructor, passing a class Meal and a string meal_name
    def __init__(self, Meal, meal_name):
        self.Meal = Meal(meal_name)

    # Originally used this but started experimenting with classes
    def make_meal(self, Meal):
        return self.Meal

    # we will get the meal that the chef made instead of getting it from the Meal class because why not?
    def get_meal(self):
        return self.Meal


# class Meal
class Meal:
    # construtor, this consturctor is initialized in the Chef object, once the object is created with a string
    def __init__(self, meal_name):
        self.meal_name = meal_name

    # i thought the __str__ format was cool, it helps prevent getting the object address.
    def __str__(self):
        return f"You ordered {self.meal_name}"

    # wont use this but I kept it since I used it before I was testing stuff out
    def get_meal_name(self):
        return self.meal_name


def main():
    # grab user input
    meal_name = input("please enter a name for your meal: ")
    # create the Chef class called chef and immediatly assign a meal to it.
    chef = Chef(Meal, meal_name)
    # from chef object we grab the Meal object that was initialized with it. then the meal class has a format __str__ so it will call that method
    print(chef.get_meal())


main()
