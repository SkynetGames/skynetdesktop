# Imported Files
import utils
import download

# Imported Dependencies
from pprint import pprint
import tkinter as tk
from tkinter import Button
from PIL import ImageTk, Image


# Imports info from GUI
def getCanvas(target):
    from gui import main
    canvas = main.canvas
    canvas.delete(target)
    return canvas

# Opens up settings menu
def settings(object):
    canvas = getCanvas("bottom")

# Creates launching buttons for downloaded library
def library(object):    
    canvas = getCanvas("bottom")
    print("library")

# Creates download buttons for games page
def games(object):
    canvas = getCanvas("bottom")
    x = 500
    for i in range(len(utils.gameData[0])):
        path = "src/images/" + utils.gameData[0][i]["name"] + ".jpg"
        img = ImageTk.PhotoImage(Image.open(path), tag="bottom")
        panel = tk.Label(canvas, image = img)
        panel.pack()


# Creates download buttons for software page
def software(object):
    canvas = getCanvas("bottom")
    t = ""
    for i in range(len(utils.software[0])):
        t = t + utils.software[0][i]["alt"] + "\n"
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack