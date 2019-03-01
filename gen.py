import qrcode
import json

def generate(objId, idx):
    data = {
        "id": str(objId),
        "entranceIdx" : str(idx)
    }
    data = json.dumps(data)
    img = qrcode.make(data)
    img.save(str(objId) + ".png")
    print("Imaged saved as: " + str(objId) + ".png")