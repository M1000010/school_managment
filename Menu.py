
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

#import student_main
from all import *
class Menu:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\menu")
        self.window = Tk()
        self.window.resizable(False, False)
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
        self.add_image("image_1.png", 450.0, 95.0)
        self.add_image("image_2.png", 775.0, 330.0)

        # Adding buttons

        self.specialite = self.add_button(548.0, 401.0, 105.0, 75.0, "button_1.png", self.open_specialite)
        self.bloc = self.add_button(416.0, 401.0, 104.0, 75.0, "button_2.png", self.open_bloc)
        self.salle = self.add_button(284.0, 401.0, 105.0, 75.0, "button_3.png", self.open_salle)
        self.evaluation = self.add_button(152.0, 401.0, 105.0, 75.0, "button_4.png", self.open_eval)
        self.paiement = self.add_button(20.0, 401.0, 105.0, 75.0, "button_5.png", self.open_paiement)
        self.abs_enseign = self.add_button(547.0, 289.0, 108.0, 75.0, "button_6.png", self.open_abs_ens)
        self.seance = self.add_button(416.0, 289.0, 105.0, 75.0, "button_7.png", self.open_seance)
        self.resultat = self.add_button(284.0, 289.0, 105.0, 75.0, "button_8.png", "button_8 clicked")
        self.module = self.add_button(152.0, 289.0, 105.0, 75.0, "button_9.png", self.open_module)
        self.enseignant = self.add_button(20.0, 289.0, 105.0, 75.0, "button_10.png", self.open_ens)
        self.abs_etudiant = self.add_button(548.0, 177.0, 104.0, 75.0, "button_11.png", self.open_abs_etd)
        self.groupe = self.add_button(416.0, 177.0, 105.0, 75.0, "button_12.png", "button_12 clicked")
        self.filiere = self.add_button(284.0, 177.0, 105.0, 75.0, "button_13.png", self.open_filiere)
        self.niveau = self.add_button(152.0, 177.0, 105.0, 75.0, "button_14.png", self.open_niveau)
        self.etudiant = self.add_button(20.0, 177.0, 105.0, 75.0, "button_15.png", self.open_stud)

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")

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

    def run(self):
        self.window.mainloop()

    def open_filiere(self):
        self.window.destroy()
        filiere_window = Filiere.Filiere()
        filiere_window.window.mainloop()


    def open_paiement(self):
        self.window.destroy()
        paiement_window = paiement.paiement()
        paiement_window.window.mainloop()


    def open_niveau(self):
        self.window.destroy()
        niveau_window = niveau.niveau()
        niveau_window.window.mainloop()

    def open_abs_ens(self):
        self.window.destroy()
        appl_window = abs_enseign.abs_ens()
        appl_window.window.mainloop()

    def open_abs_etd(self):
        self.window.destroy()
        niveau_window = absence_etd.abs_etd()
        niveau_window.window.mainloop()

    def open_bloc(self):
        self.window.destroy()
        bloc_window = bloc.bloc()
        bloc_window.window.mainloop()

    def open_ens(self):
        self.window.destroy()
        ens_window = enseignant.enseign()
        ens_window.window.mainloop()

    def open_eval(self):
        self.window.destroy()
        eval_window = evaluation.evaluation()
        eval_window.window.mainloop()

    def open_module(self):
        self.window.destroy()
        module_window = module.module()
        module_window.window.mainloop()

    def open_salle(self):
        self.window.destroy()
        salle_window = salle.salle()
        salle_window.window.mainloop()

    def open_seance(self):
        self.window.destroy()
        seance_window = seance.seance()
        seance_window.window.mainloop()

    def open_specialite(self):
        self.window.destroy()
        specialite_window = specialite.specialite()
        specialite_window.window.mainloop()

    def open_stud(self):
        self.window.destroy()
        app_window = student_main.StudentMain
        app_window.run()





if __name__ == "__main__":
    app = Menu()
    app.run()


