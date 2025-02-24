from ncm import *
from beatsaver import getMap
from tools import *
import json
import os
import re
from tqdm import tqdm

accurateMode = False
DIR = "D:\SteamLibrary\steamapps\common\Beat Saber"

failCount = 0
songListID = input("Please PASTE the id of your song from NCM list here:")

if songListID == "":
    songListID = "3219642517"

data = json.loads(getSongsFromNCM(songListID))
# data = json.loads(getSongsFromJson("t.json"))
status = data['code']
songCount = len(data["songs"])
songList = data["songs"]

print("Please open the installation directory of Beat Saber")
gameDir = os.path.join(DIR, "Beat Saber_Data/CustomLevels")
# gameDir = os.path.join(selectDir(), "Beat Saber_Data/CustomLevels")

if not os.path.exists(gameDir):
        os.makedirs(gameDir)
        print(f"Directory '{gameDir}' has been created")
else:
    print(f"Directory '{gameDir}' has been found")


print("Playlist fetch Status:", status)
# print("Playlist Name:", data['data']['name'])
print("Songs Count:", songCount)
print("Songs List:")
for song in tqdm(songList, desc = "Progress", unit = "Songs"):
    songName = song["name"]
    if accurateMode:
        song = songName + " " + song["al"]["name"]
    else:
        song = songName

    tqdm.write("Fetching " + song)
    mapResult = getMap(song)
    if mapResult == "E1":
        tqdm.write(f"No map for {song}")
        failCount += 1
    else:
        # print("URL:" + mapResult)
        downloadPath = os.path.join(gameDir, re.sub(r'[\\/*?:."<>|～!]', '', songName), "data.zip")
        downloadResult = downloader(mapResult, os.path.normpath(downloadPath))
        if downloadResult == "E2":
            tqdm.write(f"Error when download {gameDir} to {songName}.zip")
            failCount += 1
        else:
            # unzip downloaded stuff
            unzipStatus = unzip(downloadPath)
            tqdm.write("Unziping " + downloadPath)
            if unzipStatus == "E3":
                tqdm.write(f"Error when unzip {downloadPath}")
                failCount += 1

print("Songs Count:", songCount)
print("Failed Count:", failCount)
print("Success Count:", songCount - failCount)
