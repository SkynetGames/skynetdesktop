# Imported Files
import utils
from download import download

# Imported Dependencies
from pprint import pprint
import tkinter as tk
from tkinter import *
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
    t = utils.userData[0][0]
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack

# Creates launching buttons for downloaded library
def library(object):    
    canvas = getCanvas("bottom")
    t = "You don't have anything downloaded :("
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack

# Creates download buttons for games page
def games(object):    
    canvas = getCanvas("bottom")
    t = ""
    for i in range(len(utils.gameData[0])):
        img = ImageTk.PhotoImage(Image.open("src/images/" + utils.gameData[0][i]["name"] + ".jpg"))
        panel = tk.Label(canvas, image = img)
        #The Pack geometry manager packs widgets in rows or columns.
        panel.pack(fill="none")

# Creates download buttons for software page
def software(object):
    canvas = getCanvas("bottom")
    t = ""
    for i in range(len(utils.software[0])):
        t = t + utils.software[0][i]["alt"] + "\n"
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack