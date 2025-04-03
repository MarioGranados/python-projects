# Mario Granados
# Penguin Assignment

from abc import ABC, abstractmethod


# abstract class Bird
class Bird(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Bird: {self.name}"

    # abstract methods, these are required on the child class, i didn't include swim since I wasnt sure if all birds swim.

    @abstractmethod
    def set_name(self, name):
        self.name = name

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def fly(self):
        pass


# class penguin inherits from Bird the abstract class, if i dont include the abstrac methods, vs code will get mad at me.
class Penguin(Bird):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"This is a Penguin, his name is {self.name}"

    # mandatory methods here
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return super().get_name()

    def eat(self):
        return f"{self.name} eats krill, squid, and small fishes."

    def fly(self):
        return f"{self.name} cannot fly."

    def swim(self):
        return f"{self.name} swims around 4 to 7 miles per hour."


# main program
def main():
    # create penguin object
    penguin = Penguin("Pingu")
    print(penguin)
    print(penguin.fly())
    print(penguin.eat())
    print(penguin.swim())
    # create a list of birds
    # I can't create a Bird object since it is an abstract class, meaning it is like the skeleton or blueprint of the class Penguin.
    # absctract classes are more like instructions for the child class to follow.


main()
