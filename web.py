import requests
import json

properties = {}

def uploadFile(paths, buildingID): # Takes a string array of file Path and Uploads them with progress bar
    with open("properties.json") as props:
        properties = json.load(props)
    url = properties['url']
    print(url)
    files = {'image' : ('0.png', open(paths[0], 'rb'))}
    params = {
        "id" : buildingID,
        "number" : 0
    }
    # for i, fPath in enumerate(paths):
    #     files.append({'file' : (str(i) + '.png', open(fPath, 'rb'))})
    r = requests.post(url + "/buildings/upload", files = files, data = params)
    print(r.status_code)
    pass