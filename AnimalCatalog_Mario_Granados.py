# Mario Granados
# In_class assignemnt 9
# animal catalog

# image credits 
# penguin - https://en.wikipedia.org/wiki/Penguin#/media/File:Aptenodytes_forsteri_-Snow_Hill_Island,_Antarctica_-adults_and_juvenile-8.jpg - Ian Duffy from UK - Animal Portraits Uploaded by Snowmanradio
# lion - https://en.wikipedia.org/wiki/Lion#/media/File:020_The_lion_king_Snyggve_in_the_Serengeti_National_Park_Photo_by_Giles_Laurent.jpg - Giles Laurent - Own work
# elephant - https://en.wikipedia.org/wiki/Elephant#/media/File:Elephant_in_the_Serengeti_National_Park.jpg - Taken by Muhammad Mahdi Karim - Own work

#importss from prev code and python libraries
from animal_catalog_interface import Animal
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

# catalog class that creats a list of animals, also gets the animals whithin the list and adds additional animals
class Catalog:
    def __init__(self):
        self.animals = []

    
    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        return self.animals
    
# gui class from the docs
class Gui(tk.Tk):
    def __init__(self, catalog):
        super().__init__()
        self.animals = catalog.get_animals()
        self.geometry("1200x1500")
        self.title('Animal Catalog')
        self.image_label = None

        # initialize data
        self.animal_names = [animal.get_name() for animal in self.animals]

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()


    def create_wigets(self):
        paddings = {'padx': 5, 'pady': 5}

        label = ttk.Label(self, text='Select an animal:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.animal_names[0],
            *self.animal_names,
            command=self.option_changed)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, columnspan=2, sticky=tk.W, **paddings)

    # when the optino menu is selected this function is called, sometimes the images reset, sometimes they dont. I have no idea why...
    def option_changed(self, *args):
            # Find the selected animal based on the option menu
            selected_animal = next(animal for animal in self.animals if animal.get_name() == self.option_var.get())

            # Label for animal name
            name_label = tk.Label(self, text=selected_animal.get_name())
            name_label.grid(column=0, row=2, sticky=tk.W)

            # Label for animal habitat
            habitat_label = tk.Label(self, text=selected_animal.get_habitat())
            habitat_label.grid(column=0, row=3, sticky=tk.W)

            # Label for animal desc
            desc_label = tk.Label(self, text=selected_animal.get_desc())
            desc_label.grid(column=0, row=4, sticky=tk.W)

            # If there is an existing image label, remove it
            if self.image_label:
                self.image_label.grid_forget()

            # Image for the animal
            image_path = selected_animal.get_img()
            image = ImageTk.PhotoImage(Image.open(image_path))
            self.image_label = tk.Label(self, image=image)
            self.image_label.image = image
            self.image_label.grid(column=0, row=5, sticky=tk.W)


            # from docs
            self.output_label['text'] = f'You selected: {self.option_var.get()}'


# main
def main():

    # 3 animals objects
    penguin = Animal('Penguin', "Antartica", "A penguin is a flightless bird that lives in the coldest region of the world", './penguin.jpg')
    lion = Animal('Lion', "Africa", "A lion is a large cat of the species Panthera leo", './lion.jpg')
    elephant = Animal('Elephant', "Africa", "An elephant is the largest land animal on Earth", './elephant.jpg')
    # catalog
    catalog = Catalog()
    # add animals to catalog
    catalog.add_animal(penguin)
    catalog.add_animal(lion)
    catalog.add_animal(elephant)
    # start gui with catalog
    gui = Gui(catalog)
    gui.mainloop()
    # testing
    print(f"Animal Catalog: {catalog.get_animals()}")
    
main()