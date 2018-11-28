# Imported Files
import utils
import update

# Imported Dependencies
from pprint import pprint
import tkinter as tk


# Imports info from GUI
def getCanvas(target):
    from gui import main
    canvas = main.canvas
    canvas.delete(target)
    return canvas

# Opens up settings menu
def settings(object):
    canvas = getCanvas("bottom")
    print("settings")

# Creates launching buttons for downloaded library
def library(object):    
    canvas = getCanvas("bottom")
    print("library")

# Creates download buttons for games page
def games(object):
    canvas = getCanvas("bottom")
    t = ""
    for i in range(len(utils.gameData)):
        t = t + utils.gameData[i]["alt"] + "\n"
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack


# Creates download buttons for software page
def software(object):
    canvas = getCanvas("bottom")
    t = ""
    for i in range(len(utils.software)):
        t = t + utils.software[i]["alt"] + "\n"
    label = canvas.create_text(500, 500, text=t, tag="bottom")
    label.pack