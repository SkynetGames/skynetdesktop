# Imported Files
import utils
import menu

# Imported Dependencies
import tkinter as tk
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

    root = tk.Tk()
    root.iconbitmap("./icons/16x16.ico")
    update_gui = update(root)
    root.mainloop()

# Main window
def main():
    class main:        
        # Creates the window
        def __init__(self, master):
            self.master = master
            master.title("Skynet")

            # Setting window to max screen size
            master.state('zoomed')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            menu_height = (screen_height / 17)
            button_width = (screen_width / 8)

         # Creating the background design
            # Creating a full screen canvas with the correct background and no border   
            canvas = tk.Canvas(bg=utils.colors[1], highlightthickness=0)
            # Creates accent border and separator
            canvas.create_rectangle(0, 0, screen_width, (screen_height / 17), fill=utils.colors[0])
            canvas.create_rectangle(0, 0, screen_width, menu_height, fill=utils.colors[2])
            # Creates menu buttons
            library_button = canvas.create_rectangle(0, 0, button_width, menu_height, fill="red", tags="library")
            library_text = canvas.create_text(10, 10, text="Library", font=("Papyrus", 26), fill='blue',tags="library")
            games_button = canvas.create_rectangle((button_width * 2), 0, button_width, menu_height, fill="red", tags="library")
            games_text = canvas.create_text(10, 10, text="Games", font=("Papyrus", 26), fill='blue',tags="library")
            software_button = canvas.create_rectangle((button_width * 3), 0, button_width, menu_height, fill="red", tags="library")
            software_text = canvas.create_text(10, 10, text="Software", font=("Papyrus", 26), fill='blue',tags="library")            
            # Packs buttons
            canvas.tag_bind("libary", "<Button-1>", menu.library)
            # Packs canvas for delivery
            canvas.pack(fill=tk.BOTH, expand=1)          

    root = tk.Tk()
    root.wm_iconbitmap(bitmap = "./icons/16x16.ico")
    main_gui = main(root)
    root.mainloop()