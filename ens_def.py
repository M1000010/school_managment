from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import Menu
class enseign:
    def __init__(self, window, controller):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\enseign")
        self.window = window
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        # Store references to images
        self.images = {}

        self.setup_ui()

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setup_ui(self):
        # Adding images
        self.add_image("image_1.png", 450.0, 251.0)
        self.add_image("image_2.png", 407.0, 410.0)
        self.add_image("image_3.png", 505.0, 59.0)

        # Adding entries

        self.date_naissanceF = self.add_entry(225.0, 463.0, 134.0, 15.0, "entry_1.png", 292.0, 471.5)
        self.id_moduleF = self.add_entry(572.0, 453.0, 135.0, 16.0, "entry_2.png", 639.5, 462.0)
        self.id_specialiteF = self.add_entry(572.0, 420.0, 135.0, 16.0, "entry_3.png", 639.5, 429.0)
        self.emailF = self.add_entry(572.0, 386.0, 135.0, 16.0, "entry_4.png", 639.5, 395.0)
        self.numeroF = self.add_entry(572.0, 353.0, 135.0, 16.0, "entry_5.png", 639.5, 362.0)
        self.prenomF = self.add_entry(225.0, 434.0, 134.0, 14.0, "entry_6.png", 292.0, 442.0)
        self.nomF = self.add_entry(225.0, 404.0, 134.0, 15.0, "entry_7.png", 292.0, 412.5)
        self.cinF = self.add_entry(225.0, 375.0, 134.0, 14.0, "entry_8.png", 292.0, 383.0)
        self.idF = self.add_entry(225.0, 345.0, 134.0, 15.0, "entry_9.png", 292.0, 353.5)
        self.barre_rechercheF = self.add_entry(109.0, 141.0, 676.0, 22.0, "entry_10.png", 447.0, 153.0)

        # Adding buttons
        self.ajouter = self.add_button(790.0, 346.0, 87.0, 22.0, "button_1.png", "button_1 clicked")
        self.modifier = self.add_button(790.0, 399.0, 87.0, 22.0, "button_2.png", "button_2 clicked")
        self.supprimer = self.add_button(790.0, 452.0, 87.0, 22.0, "button_3.png", "button_3 clicked")
        self.rechercher = self.add_button(790.0, 141.0, 87.0, 23.0, "button_4.png", "button_4 clicked")
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id = self.add_button(12.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.window.resizable(False, False)

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")

    def add_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        self.add_image(image_file, bg_x, bg_y)
        entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)
        return entry
    def add_button(self, x, y, width, height, image_file, command):
        self.add_image(image_file, x + width / 2, y + height / 2)
        button = Button(
            image=self.images[image_file],
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat",
            cursor="hand2"
        )
        button.place(x=x, y=y, width=width, height=height)








