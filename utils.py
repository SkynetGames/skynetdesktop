# Imported Files
import menu

# Imported Dependencies
import json


# Global vairables
data_files = [ # Local and remote file locations for data files
    ["src/gameData.json", "https://s3.amazonaws.com/skynet-metadata/game_data.json"],
    ["src/softwareData.json", "https://s3.amazonaws.com/skynet-metadata/software.json"],
    #["src/usr_prefs.json", "https://s3.amazonaws.com/skynet-desktop/usr_prefs.json"]
]

# Arrays generated from data files and user prefs
gameData = []
software = []
def loadJSON():
    with open(data_files[0][0]) as g:
        gameData.append(json.load(g))

    with open(data_files[1][0]) as s:
        software.append(json.load(s))


# Convert to data from user_prefs.json
usr_data = [ # Local files that contain games, movies, and other software installed on the machine
    "src/games",
    "src/movies",
    "src/software",
    "src/images"
]

buttons = [ # Data to simplify menu button creation
    ["settings", "Settings", menu.settings],
    ["library", "Library", menu.library],
    ["games", "Games", menu.games],
    ["software", "Software", menu.software]
]

colors = [ # Color palette of skynet
    "#b0bec5", # Light blue
    "#546e7a", # Middle blue
    "#263238"  # Dark blue
]