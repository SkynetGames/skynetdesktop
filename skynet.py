# Imported Files
import update
import gui
import utils

# Imported Dependencies
import os
import shutil
import time

# Global vairables


# TODO\\ get init() working

# Initializes the files
def init():
    # Creates, or clears /cache
    if (os.path.isdir("cache")):
        shutil.rmtree("cache")
        os.mkdir("cache")
    else: 
        os.mkdir("cache")
    # If it doesn't exist create /src
    if (os.path.isdir("src")):
        # Updates data files
        lifespan = 86400
        path = utils.data_files[0][0]
        file_exists = os.path.exists(path)
        file_up_to_date = False
        if file_exists:
            file_up_to_date = os.path.getmtime(path) - time.time() < lifespan
        if not file_exists or not file_up_to_date:
            update.update()
    else:
        os.mkdir("src")
        init()


# Main function
def main():
    init()
    gui.main()

# Calls the main function to start everything
main()