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
            button_width = (screen_width / 10)

         # Creating the background design
            # Creating a full screen canvas with the correct background and no border   
            canvas = tk.Canvas(bg=utils.colors[1], highlightthickness=0)
            # Creates accent border and separator
            canvas.create_rectangle(0, 0, screen_width, (screen_height / 16.25), fill=utils.colors[0], outline="")
            canvas.create_rectangle(0, 0, screen_width, menu_height, fill=utils.colors[2], outline="")
            # Creates menu buttons
            for i in range(len(utils.buttons)):
                button_startX = (button_width * i)
                button_endX = (button_width + (button_width * i))
                button = canvas.create_rectangle(button_startX, 0, button_endX, menu_height, fill=utils.colors[2], activefill=utils.colors[0], tags=utils.buttons[i][0], outline="")
                text = canvas.create_text((button_width * (i - 0.5)), (menu_height / 2), text=utils.buttons[i][1], font=("Helvetica", 26), fill="white", tags=utils.buttons[i][0])
                canvas.tag_bind(utils.buttons[i][0], "<Button-1>", utils.buttons[i][2])
            # Packs canvas for delivery
            canvas.pack(fill=tk.BOTH, expand=True)          

    root = tk.Tk()
    root.wm_iconbitmap(bitmap = "./icons/16x16.ico")
    main_gui = main(root)
    root.mainloop()