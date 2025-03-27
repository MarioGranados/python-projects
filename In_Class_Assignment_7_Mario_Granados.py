# Mario Granados
# in class asignment 7


class Crustaceaon:
    def __init__(self, name, number_of_legs, has_claws):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_claws = has_claws

    def set_name(self, name):
        self.name = name

    def set_number_of_legs(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def set_has_claws(self, has_claws):
        self.has_claws = has_claws

    def get_name(self):
        return self.name

    def get_number_of_legs(self):
        return self.number_of_legs

    def get_has_claws(self):
        return self.has_claws
    
    def __str__(self):
        return f"Name: {self.name}, Number of legs: {self.number_of_legs}, Has Claws: {'Yes' if self.has_claws else 'No'}"


class Krill(Crustaceaon):
    def __init__(self, name, number_of_legs, has_claws):
        super().__init__(name, number_of_legs, has_claws)
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_claws = has_claws

    def just_keep_swimmin(self):
        return "Just keep swimming, just keep swimming"


def main():
    krill = Krill("Krill", 10, False)
    print(krill)
    print(krill.just_keep_swimmin())    

    crusty = Crustaceaon("Crusty", 8, True)
    print(crusty)
    print(crusty.just_keep_swimmin())
    return

main()
