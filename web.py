import requests
import json

properties = {}

def uploadFile(paths): # Takes a string array of file Path and Uploads them with progress bar
    with open("properties.json") as props:
        properties = json.load(props)
    print(properties)
    print(paths)
    pass