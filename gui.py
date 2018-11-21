# Imported Files
import utils

# Imported Dependencies
from tkinter import Tk, Label, Button, Canvas, Frame, BOTH
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
        def library(self):
            update()
        def games(self):
            print("games")
        def software(self):
            print("software")
        def movies(self):
            print("movies")  
        
        # Creates the window
        def __init__(self, master):
            self.master = master
            master.title("Skynet")

            # Setting window to max screen size
            master.state('zoomed')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()

         # Creating the background design
            # Creating a full screen canvas with the correct background and no border   
            canvas = Canvas(bg=utils.colors[1], highlightthickness=0)
            # Creates accent border and separator
            canvas.create_rectangle(0, 0, screen_width, (screen_height / 17), fill=utils.colors[0])
            canvas.create_rectangle(0, 0, screen_width, (screen_height / 18), fill=utils.colors[2])
            # Packs and designs canvas
            canvas.pack(fill=BOTH, expand=1)          

    root = Tk()
    root.wm_iconbitmap(bitmap = "icons/16x16.bmp")
    main_gui = main(root)
    root.mainloop()