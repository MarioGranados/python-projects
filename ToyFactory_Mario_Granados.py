# Mario Granados
# Toy Factory


# Toy Class
class Toy:
    # initializer with toy name
    def __init__(self, toy_name):
        self.toy_name = toy_name

    # grabs the toy name
    def get_toy_name(self):
        return self.toy_name

    # formats the toy name
    def __str__(self):
        return f"Say hello to {self.toy_name}, your new toy"


# Toy Factory Class
class ToyFactory:
    # Originally I set default values but since we are running tests, the default values are in the Test Class
    def __init__(self, heads, bodies, legs, arms, workers):
        self.heads = heads
        self.bodies = bodies
        self.arms = arms
        self.legs = legs
        self.workers = workers

    # for visual purpose
    def __str__(self):
        return f"head and bodies remaining: {self.heads} Legs and arms: {self.legs} workers: {self.workers}"

    # grabs the parts so we subtract it from the inventory
    def fetch_parts(self):
        # if there is no more parts we return the out_of_stock method that prints 'out of stock'
        if self.heads <= 0 or self.bodies <= 0 or self.arms <= 0 or self.legs <= 0:
            return self.out_of_stock()
        # If parts are available then we subtract form inventory
        else:
            self.heads -= 1
            self.arms -= 2
            self.legs -= 2
            self.bodies -= 1
            # return true for validation on creating a toy, we cant promise a new toy if we dont have parts
            return True

    # if we have enough workers then we will assemble the parts
    def assemble_parts(self):
        # check for workers
        if self.workers <= 0:
            # if we are out of workers then we print we are out of workers
            return self.out_of_workers()
        else:
            # if we have workers they get assigned to the assembly of the toy
            self.workers -= 1
            # return true for validation creating a toy
            return True

    # if we have parts, and workers we create a toy, otherwise we dont create nothing
    def make_toy(self, toy_name):
        if self.fetch_parts() and self.assemble_parts():
            return Toy(toy_name)
        else:
            return None

    # print we are out of stock and return false
    def out_of_stock(self):
        print("\nWe ran out of parts!\n")
        return False

    # same as previous method but for workers
    def out_of_workers(self):
        print("\nWe ran out of workers!\n")
        return False


# test class
class Test:
    # we have default values, but they can be changed for different tests
    def __init__(self, heads=100, bodies=100, legs=200, arms=200, workers=5):
        self.factory = ToyFactory(heads, bodies, legs, arms, workers)

    # run the test until we dont get a toy
    def run(self):
        while True:
            # get toy name
            toy_name = input("Enter the name of your toy: ")
            # create a toy, if we dont have parts this will return none
            toy = self.factory.make_toy(toy_name)
            # if there is a toy, print the toy __str__ and factory __str__
            if toy:
                print(toy)
                print(self.factory)
            else:
                print("Could not create toy. Factory is out of stock or workers.")
                # if there is no toys, we stop loop
                break

        print("Toy creation process finished.")


# different test cases, for different inventory
def main():
    test = Test()
    test.run()

    test1 = Test(5, 5, 10, 10, 20)
    test1.run()

    test2 = Test(20, 20, 20, 20, 20)
    test2.run()

    test3 = Test(10, 10, 10, 10, 0)
    test3.run()


main()
