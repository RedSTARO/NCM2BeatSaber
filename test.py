from ncm import *
import json

songListID = "t.json"
origin = getSongsFromJson(songListID)
data = json.loads(origin)

print(data)
print(data["songs"])
print(len(data["songs"]))