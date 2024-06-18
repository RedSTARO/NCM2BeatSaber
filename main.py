from ncm import getSongs
from beatsaver import getMap
from tools import *
import json

failCount = 0

data = json.loads(getSongs())


print("Fetch Status:", data['msg'])
print("Playlist Name:", data['data']['name'])
print("Songs Count:", data['data']['songs_count'])
print("Songs List:")
for song in data['data']['songs']:
    song = song.split(" - ")[0]
    print("Fetching " + song + ":")
    mapResult = getMap(song)
    if mapResult == "E1":
        print(f"No map for {song}")
        failCount += 1
    else:
        print("URL:" + mapResult)
print("Songs Count:", data['data']['songs_count'])
print("Failed Count:", failCount)
print("Success Count:", data['data']['songs_count'] - failCount)
