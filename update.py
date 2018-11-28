# Imported Files
import gui
import utils

# Imported Dependencies
from tkinter import Tk, Label, Button
import threading
import requests
import urllib.request
import json

# Starts the GUI and updating
def update():
    updateStart = updating()
    gui.update()

# Actual update class
class updating():
    # Constructor method
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  
        thread.start()  

    # Method that actually updates the program
    def run(self):
        for i in range(len(utils.data_files)):
            try:
                soliditems = requests.get(utils.data_files[i][1])
            finally:    
                data = soliditems.json()
                with open(utils.data_files[i][0], "w") as f:
                    json.dump(data, f)  
                print(utils.data_files[i][0])      
        utils.loadJSON()
        for i in range(len(utils.gameData[0])):
            url = "https://s3.us-east-2.amazonaws.com/skynet-game-images/" + utils.gameData[0][i]["name"] + ".jpg"
            target = "src/images/" + utils.gameData[0][i]["name"] + ".jpg"
            print(url)
            urllib.request.urlretrieve(url, target)