import requests
import json

def getMap(songName):
    # Define the API endpoint
    url = f"https://beatsaver.com/api/search/text/0?sortOrder=Relevance&q={songName}"

    # Perform the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Access specific elements (example)
        try:
            return data["docs"][0]["versions"][0]["downloadURL"]
        except IndexError:
            return "E1"


