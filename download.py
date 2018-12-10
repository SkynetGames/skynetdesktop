# Imported Files
import utils

# Imported Dependencies
import threading
import requests
import urllib.request
import json

# Initializer function to be called
target = ""
dest = ""
def download(target, dest):
    print(target)
    print(dest)
    downloadStart = content()

# Content downloading class
class content():
    # Constructor method
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  
        thread.start()  

    # Method that actually updates the program
    def run(self):
        print(target)
        print(dest)