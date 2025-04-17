# Mario Granados
# In_class assignemtn  9

# image credits 
# url https://media.istockphoto.com/id/636315398/photo/sumppfheuschrecke.jpg?s=612x612&w=0&k=20&c=nuP6jr6Fo_6pQiaVJ3RhUuVadW6GKk2183TsPDLNfx8=
# image from istockphoto.com
# credit to Eileen Krumpf
# date Dec 24 2016

#importss
import tkinter as tk
from PIL import ImageTk, Image

# class animal with attributes name, habitat, desc, and image_path
# getters only, setters not needed for now
class Animal:
    def __init__(self, name, habitat, desc, image_path):
        self.name = name
        self.habitat = habitat
        self.desc = desc
        self.image_path = image_path
    def get_name(self):
        return self.name
    def get_habitat(self):
        return self.habitat
    def get_desc(self):     
        return self.desc
    def get_img(self):
        return self.image_path
    
# simple GUI
root = tk.Tk()
# title and window size
root.title("Museum Catalog")
root.geometry("700x500")

# image path according to my program, change it for testing
image_path = './grasshopper.jpg'

# makes the code look cleaner, could of been a function but I wanted to keep it simple
image = ImageTk.PhotoImage(Image.open(image_path))

# create object
grasshopper = Animal("Grasshopper", "Everglades", "A grasshopper can jump up to 30 inches. "
                                                  "That's roughly 20 times its body length.",
                                                  image)

# creates labels for the gui and adds the image
name_label = tk.Label(root, text=grasshopper.get_name())
name_label.pack()
habitat_label = tk.Label(root, text=grasshopper.get_habitat())
habitat_label.pack(pady=10)
desc_label = tk.Label(root, text=grasshopper.get_desc())
desc_label.pack()
image_label = tk.Label(root, image=grasshopper.get_img())
# adds padding for the image
image_label.pack(padx=10, pady=10)

root.mainloop()