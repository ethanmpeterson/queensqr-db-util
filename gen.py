import qrcode

def generate(objId):
    url = "https://queensqr.herokuapp.com/" + str(objId)
    img = qrcode.make(url)
    img.save(str(objId) + ".png")
    print("Imaged saved as: " + str(objId) + ".png")