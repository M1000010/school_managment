from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import Menu
class specialiteUI:
    def __init__(self, window, controller):

        self.window = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\ayamo\OneDrive\Bureau\Code\Code\assets\frame_specialite")

        self.window.geometry("900x500+180+100")
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

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setup_ui(self):

        # Adding images
        self.add_image("image_1.png", 505.0, 59.0)
        self.add_image("image_2.png", 738.0, 300.0)
        self.add_image("image_3.png", 299.0, 320.0)

        # Adding entries
        self.barre_rechercheF = self.add_entry(111.0, 141.0, 676.0, 22.0, "entry_1.png", 449.0, 153.0)
        self.nom_specialiteF = self.add_entry(731.0, 306.0, 134.0, 15.0, "entry_2.png", 798.0, 314.5)
        self.id_specialiteF = self.add_entry(731.0, 276.0, 134.0, 15.0, "entry_3.png", 798.0, 284.5)

        # Adding buttons
        self.rechercher = self.add_button(792.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.ajouter= self.add_button(792.0, 375.0, 87.0, 22.0, "button_2.png", "button_2 clicked")
        self.supprimer = self.add_button(694.0, 375.0, 87.0, 22.0, "button_3.png", "button_3 clicked")
        self.modifier = self.add_button(596.0, 375.0, 87.0, 22.0, "button_4.png", "button_4 clicked")
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id= self.add_button(14.0, 141.0, 98.0, 23.0, "button_6.png", "button_6 clicked")
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
















