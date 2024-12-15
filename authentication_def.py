from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import Menu

from authentication_base import authController


class logUI:
    def __init__(self, root, controller):

        self.controller = controller

        self.root = root

        self.root.geometry("888x500+180+100")
        self.root.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=500,
            width=888,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.ASSETS_PATH = Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\authentication")


    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setup_ui(self):
        # Images
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(689.0, 250.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(244.0, 222.0, image=image_image_2)

        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.canvas.create_image(244.0, 317.0, image=image_image_3)

        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas.create_image(244.0, 85.0, image=image_image_4)

        # Entries
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(244.0, 236.0, image=entry_image_1)
        self.usernameF = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 16)
        )
        self.usernameF.place(x=91.0, y=221.0, width=306.0, height=24.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(241.0, 334.0, image=entry_image_2)
        self.passwordF = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='●',
            font=("Helvetica", 16)
        )
        self.passwordF.place(x=88.0, y=319.0, width=306.0, height=24.0)

        # Button
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.button_1.place(x=155.0, y=404.0, width=200.0, height=40.0)

        # Store references to images to prevent garbage collection
        self.images = [image_image_1, image_image_2, image_image_3, image_image_4, entry_image_1, entry_image_2, button_image_1]
    def login(self):
        username = self.usernameF.get()
        password = self.passwordF.get()

        if self.controller.authenticate(username, password):
            messagebox.showinfo("Succès", "Authentification réussie!")
            self.root.after(100, self.open_menu)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
    def on_button_click(self):
        print("Button clicked")

    def salam(self):
        self.username = 'cristiano'
        self.password = 'miakhalifa'
        self.controller.register(self.username, self.password)

    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()