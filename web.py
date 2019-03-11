import requests
import json

properties = {}

def uploadFile(paths, buildingID): # Takes a string array of file Path and Uploads them with progress bar
    with open("properties.json") as props:
        properties = json.load(props)
    url = properties['url']
    print(url)
    
    files = {}
    params = {}

    if len(paths) == 1:
        params = {
            "id" : buildingID,
            "number" : 0
        }
        files = {'image' : ('0.png', open(paths[0], 'rb'))}
        r = requests.post(url + "/buildings/upload", files = files, data = params)
        print("File: " + paths[0] + " Completed")
    else:
        files = []
        for i, fPath in enumerate(paths):
            files = {'image' : (str(i) + '.png', open(fPath, 'rb'))}
            params = {
                "id" : buildingID,
                "number" : i
            }
            r = requests.post(url + "/buildings/upload", files = files, data = params)
            print("File: " + fPath + " Completed")

    print(r.status_code)
    pass