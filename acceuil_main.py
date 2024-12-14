from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from acceuil_def import accUI


class accMain:
    def __init__(self):

        self.window = Tk()
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")

        self.ui = accUI(self.window)
        self.initialize_ui()

    def initialize_ui(self):

        self.ui.setup_ui()
    def run(self):
            # Lancer la boucle principale de l'application
            self.window.resizable(False, False)
            self.window.mainloop()



if __name__ == "__main__":
    app = accMain()
    app.run()