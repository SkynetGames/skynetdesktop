# Imported Files
import utils

# Imported Dependencies


# Method to download and unzip files
def download(url):
    serverLoc = "https://s3.us-east-2.amazonaws.com/skynet-game-files/" + url + ".zip"
    print(serverLoc)