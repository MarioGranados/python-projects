# Mario Granados
# Everglades


class Exhibit:
    def __init__(self, name, temperature, humidity):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity

    # setters
    def set_name(self, name):
        self.name = name

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_humidity(self, humidity):
        self.humidity = humidity

    # getters
    def get_name(self):
        return self.name

    def get_temperature(self):
        return self.temperature

    def humidity(self):
        return self.humidity

    # string representation / formatter
    def __str__(self):
        return f"This is a(n): {self.name}\nThe Temperature is : {self.temperature}\nHumidity is: {self.humidity}%\n"


class Everglades(Exhibit):
    def __init__(self, name="everglades", temperature=80, humidity=90, water_level=0):
        super().__init__(name, temperature, humidity)
        self.water_level = water_level

    # custom method for Everglades
    def set_water_level(self, water_level):
        self.water_level = water_level

    def get_water_level(self):
        return self.water_level
    
    def get_name(self):
        return super().get_name()

    def __str__(self):
        return f"{super().__str__()}The water level is: {self.water_level} inches\n"


def main():
    exhibit = Exhibit("Dessert", 100, 0)
    print(exhibit)

    everglades = Everglades("Everglades", 80, 90, 5)
    print(everglades)

    print(f"changing water lever in {everglades.get_name()}...\n")

    everglades.set_water_level(10)
    print(everglades)
    return


main()
