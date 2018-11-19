# Imported Files

# Imported Dependencies

# Global vairables
data_files = [ # Local and remote file locations for data files
    ["src/gameData", "https://s3.amazonaws.com/skynet-metadata/games.json"],
    ["src/movieData", "https://s3.amazonaws.com/skynet-metadata/movies.json"],
    ["src/softwareData", "https://s3.amazonaws.com/skynet-metadata/software.json"]
]

usr_data = [ # Local files that contain games, movies, and other software installed on the machine
    "src/games",
    "src/movies",
    "src/software"
]

colors = [ # Color palette of skynet
    "#b0bec5" # Main light background
]