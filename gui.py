# Imported Files
import utils

# Imported Dependencies
from tkinter import Tk, Label, Button
import sys

# GUI update window
def update():
    class update:
        # Creates the window
        def __init__(self, master):
            self.master = master
            master.title("Updating...")
            master.configure(background=utils.colors[0])
            master.geometry("300x150") # x, y
            master.resizable(0, 0)

    root = Tk()
    root.iconbitmap("icons\16x16.bmp")
    update_gui = update(root)
    root.mainloop()

# Main window
def main():
    class main:
        # Creates the window
        def __init__(self, master):
            self.master = master
            master.title("Skynet")
            master.configure(background=utils.colors[0])
            # Setting window to max screen size
            master.state('zoomed')

    root = Tk()
    root.wm_iconbitmap(bitmap = "icons/16x16.bmp")
    main_gui = main(root)
    root.mainloop()