from ncm import getSongs
from beatsaver import getMap
from tools import *
import json
import os
import re
from tqdm import tqdm

accurateMode = True
DIR = "H:\\Steam\\steamapps\\common\\Beat Saber"

failCount = 0
songListURL = input("Please paste the link of your song list here:")

if songListURL == "":
    songListURL = "https://music.163.com/#/playlist?id=3219642517"

data = json.loads(getSongs(songListURL))

print("Please open the installation directory of Beat Saber")
gameDir = os.path.join(DIR, "Beat Saber_Data/CustomLevels")
# gameDir = os.path.join(selectDir(), "Beat Saber_Data/CustomLevels")

if not os.path.exists(gameDir):
        os.makedirs(gameDir)
        print(f"Directory '{gameDir}' has been created")
else:
    print(f"Directory '{gameDir}' has been found")


print("Playlist fetch Status:", data['msg'])
print("Playlist Name:", data['data']['name'])
print("Songs Count:", data['data']['songs_count'])
print("Songs List:")
for song in tqdm(data['data']['songs'], desc = "Progress", unit = "Songs"):
    songName = song.split(" - ")[0]
    if accurateMode == False:
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

print("Songs Count:", data['data']['songs_count'])
print("Failed Count:", failCount)
print("Success Count:", data['data']['songs_count'] - failCount)
