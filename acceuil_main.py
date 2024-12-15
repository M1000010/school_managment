from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import acceuil_def


class accMain:
    def __init__(self):

        self.window = Tk()


        self.ui = acceuil_def.accUI(self.window)
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