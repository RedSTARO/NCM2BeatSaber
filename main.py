from ncm import getSongs
from beatsaver import getMap
from tools import *
import json
import os
import re

accurateMode = False

failCount = 0
data = json.loads(getSongs(input("Please paste the link of your song list here"))

print("Please open the installation directory of Beat Saber")
gameDir = os.path.join(selectDir(), "Beat Saber_Data/CustomLevels")

if not os.path.exists(gameDir):
        os.makedirs(gameDir)
        print(f"Directory '{gameDir}' has been created")
else:
    print(f"Directory '{gameDir}' has been found")


print("Fetch Status:", data['msg'])
print("Playlist Name:", data['data']['name'])
print("Songs Count:", data['data']['songs_count'])
print("Songs List:")
for song in data['data']['songs']:
    songName = song.split(" - ")[0]
    if accurateMode == True:
        song = songName
    print("Fetching " + song)
    mapResult = getMap(song)
    if mapResult == "E1":
        print(f"No map for {song}")
        failCount += 1
    else:
        # print("URL:" + mapResult)
        downloadPath = os.path.join(gameDir, re.sub(r'[\\/*?:"<>|]', '', songName), "data.zip")
        downloadResult = downloader(mapResult, downloadPath)
        if downloadResult == "E2":
            print(f"Error when download {gameDir} to {songName}.zip")
            failCount += 1
        else:
            # unzip downloaded stuff
            unzipStatus = unzip(downloadPath)
            print(downloadPath)
            if unzipStatus == "E3":
                print(f"Error when unzip {downloadPath}")
                failCount += 1

print("Songs Count:", data['data']['songs_count'])
print("Failed Count:", failCount)
print("Success Count:", data['data']['songs_count'] - failCount)
