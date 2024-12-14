import tkinter as tk

from acceuil_main import accMain
from Authentication_main import authMain


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Switch Between Interfaces")

        self.accMain = accMain(self.root, self.show_authMain)
        self.authMain = authMain(self.root, self.show_accMain)

        self.show_authMain()

    def show_accMain(self):
        self.authMain.pack_forget()
        self.accMain.pack()

    def show_interface2(self):
        self.accMain.pack_forget()
        self.authMain.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
