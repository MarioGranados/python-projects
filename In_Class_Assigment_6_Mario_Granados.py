# Mario Granados
# In class assigment 6


# class Bug with name: string, number of legs: int, and number of wings: int
class Bug:
    def __init__(self, name: str, legs: int, wings: int):
        self.name = name
        self.legs = legs
        self.wings = wings

    # getters
    def get_name(self):
        return self.name

    # setters
    def set_name(self, name: str):
        self.name = name

    def get_legs(self):
        return self.legs

    def set_legs(self, legs: int):
        self.legs = legs

    def get_wings(self):
        return self.wings

    def set_wings(self, wings: int):
        self.wings = wings

    # str formatter
    def __str__(self):
        return f"Bug: {self.name}, Legs: {self.legs}, Wings: {self.wings}"


# inheritance of bug, grasshopper
class Grasshopper(Bug):
    # initialize with inheritance, defaults are 6 legs, and 4 wings
    def __init__(self, name: str):
        super().__init__(name, legs=6, wings=4)

    # make grasshopper hope or jump
    def jump(self):
        return f"{self.name} Jump!"

    # make grasshopper sound chirp
    def sound(self):
        return f"{self.name} chirp chirp"

    # dont need __str__ due to parent class already having the formatter.


# main function
def main():
    # create bug object and initialize values
    bug = Bug("Random Bug", 8, 2)
    print(bug)
    # create grasshopper object based on bug class
    grasshopper = Grasshopper("Green Hopper")
    print(grasshopper)
    print(grasshopper.jump())
    print(grasshopper.sound())

    # testing super(), by using setters from the parent class
    grasshopper.set_name("Monster Grasshopper")
    grasshopper.set_legs(8)
    grasshopper.set_wings(8)
    print(grasshopper)
    print(grasshopper.jump())
    print(grasshopper.sound())

    # prints false since objects are not the same
    ##print(bug == grasshopper)


main()
