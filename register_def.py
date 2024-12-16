from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, END, messagebox
from tkinter.ttk import Combobox

import authentication_main
from registre import userC


class registerUI :
    def __init__(self, window, controller):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\register")

        self.window = window
        self.controller = controller

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

        self.add_image("image_1.png", 248.0, 158.0)
        self.add_image("image_2.png", 435.0, 63.0)
        self.add_image("image_3.png", 248.0, 253.0)
        self.add_image("image_4.png", 689.0, 259.0)
        self.add_image("image_5.png", 248.0, 345.0)

        self.choix = ["Etudiant", "Enseignant", "Admin"]

        # Adding entries

        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(248.0, 172.0, image=entry_image_1)
        self.usernameF = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 16)
        )

        self.usernameF.place(x=95.0, y=159.0, width=306.0, height=24.0)

        #self.user_nameF = self.add_entry(95.0, 159.0, 306.0, 24.0, "entry_1.png", 248.0, 172.0)
        #self.passwordF = self.add_entry(92.0, 257.0, 306.0, 24.0, "entry_2.png", 245.0, 270.0)
        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(245.0, 270.0, image=entry_image_2)
        self.passwordF = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show='●',
            font=("Helvetica", 16)
        )
        self.passwordF.place(x=92.0, y=257.0, width=306.0, height=24.0)
        self.RoleF = self.add_combobox(145.0, 352.0, 210.0, 30.0, "entry_3.png", 250.0, 362.0,self.choix)





        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.open_menu,
            relief="flat"
        )
        self.button_1.place(
            x=165.0,
            y=408.0,
            width=166.9046630859375,
            height=46.999755859375
        )

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")



    def add_combobox(self, x, y, width, height, image_file, bg_x, bg_y, values):

        style = ttk.Style()
        style.configure("Custom.TCombobox",
                        fieldbackground="white",
                        borderwidth=0,
                        highlightthickness=0,
                        font=("Helvetica", 16))
        """
        Ajoute un champ déroulant (Combobox) à la fenêtre.

        Args:
            x (float): Position x du Combobox.
            y (float): Position y du Combobox.
            width (float): Largeur du Combobox.
            height (float): Hauteur du Combobox.
            values (list): Liste des options à afficher dans le Combobox.
            default_index (int): Index de l'option par défaut sélectionnée.

        Returns:
            Combobox: L'instance de Combobox créée.
        """
        self.add_image(image_file, bg_x, bg_y)
        combobox = Combobox(
            self.window,
            values=values,
            style="Custom.TCombobox"
        )
        combobox.place(x=x, y=y, width=width, height=height)
        # combobox.current(default_index)  # Définit la sélection par défaut
        return combobox

    def open_menu(self):
        self.addUser()
        self.window.destroy()
        menu_window = authentication_main.authMain()
        menu_window.root.mainloop()

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addUser(self):
        username = self.usernameF.get()
        password = self.passwordF.get()
        role = self.RoleF.get()

        if not username or not password:
            messagebox.showwarning("Erreur d'entrée", "Veuillez remplir les champs de nom d'utilisateur et mot de passe !")
            return

        if self.controller.addUser(username, password, role):
            messagebox.showinfo("Succès", "Utilisateur enregistré avec succès !")
            self.clearForm()
        else:
            messagebox.showerror("Échec de l'enregistrement", "Une erreur s'est produite lors de l'enregistrement de l'utilisateur.")

    def clearForm(self):
        self.usernameF.delete(0, 'end')
        self.passwordF.delete(0, 'end')
        self.RoleF.set('')

    def clearForm(self):
        widgets = [self.usernameF, self.passwordF, self.RoleF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets






