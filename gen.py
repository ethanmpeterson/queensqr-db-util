import qrcode

def generate(objId):
    url = "https://queensqr.herokuapp.com/" + str(objId)
    return qrcode.make(url)