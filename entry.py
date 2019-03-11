# Prompt User For all Data needed for a new Building Object in the DB
# return a dictionary that can be posted to the DB in the main.py file

import file as FileClient
import web as WebClient


b = {}
b['services'] = []
b['entrances'] = []

floorPaths = []

def  fieldPrompt(prompt, dbField):
    ans = input(prompt)
    ans = ans.strip()
    b[str(dbField)] = ans
    print("")

def arrayField(prompt, dbField):
    arr = []
    print("ARRAY FIELD (GIVE COMMA SEPERATED LIST)")
    ans = input(prompt)
    ans = ans.split(",")
    for i in range(0, len(ans)):
        ans[i] = ans[i].strip()
        arr.append(ans[i])
    b[str(dbField)] = arr
    print("")

def hourEntry(dbField, dict):
    print("\nHOUR ENTRY SYSTEM")
    print("System goes over each day of the week\nType enter if the service/building is closed. Otherwise type the time formatted in 12H with a dash")
    print("Ex: '9:00 AM - 5:00 PM'\n")
    hourDict = {}

    hourDict['mon'] = input("Monday: ")
    hourDict['tue'] = input("Tuesday: ")
    hourDict['wed'] = input("Wednesday: ")
    hourDict['thu'] = input("Thursday: ")
    hourDict['fri'] = input("Friday: ")
    hourDict['sat'] = input("Saturday: ")
    hourDict['sun'] = input("Sunday: ")
    print(hourDict)
    dict['hours'] = hourDict

def newEntrance(targetDict, serviceFlag):
    print("ENTRANCE ENTRY")
    print("All fields mandatory press enter to move onto the next one")
    entranceDict = {}
    
    entranceDict['name'] = input("name: ")
    print("Floating Point Numbers Required")
    entranceDict['x'] = float(input("x: "))
    entranceDict['y'] = float(input("y: "))

    if serviceFlag:
        targetDict['entrance'] = entranceDict
    else:
        targetDict['entrances'].append(entranceDict)
    print(targetDict)

def newFloor():
    floorPaths.append(FileClient.selector())

def newFloorPlan(buildingID):
    print("Welcome To the Floor Plan Creation Wizard\n\n")
    print("Select a PNG file of the floorplan start with the lowest floor (i.e basement and go up)\n")
    input("Press Enter to Continue")
    newFloor()
    while True:
        ans = input("Would like to upload another Floor [y/n]")
        if ans != "y":
            break
        newFloor()
    print(floorPaths)
    ans = input("Upload the Files above? [y/n]")
    if ans == "y":
        WebClient.uploadFile(floorPaths, buildingID)
    


def newService():
    print("SERVICE ENTRY")
    print("all fields mandatory press enter to move onto the next one")
    serviceDict = {}
    serviceDict['entrance'] = {}

    serviceDict['name'] = input("name: ")
    serviceDict['room_number'] = input("room number: ")
    serviceDict['faculty'] = input("faculty: ")
    hourEntry("hours", serviceDict)
    serviceDict['description'] = input("description: ")
    
    newEntrance(serviceDict, True)

    b['services'].append(serviceDict)
    print("Service Recorded")
    pass

def newBuilding():
    print("Welcome to Building Entry Wizard")
    print("Press enter to move onto the next property (all fields mandatory)\n")
    
    fieldPrompt("name: ", "name")
    fieldPrompt("address: ", "address")
    fieldPrompt("faculty: ", "faculty")
    hourEntry("hours", b)
    fieldPrompt("history: ", "history")
    arrayField("alias: ", "alias")
    while True:
        newService()
        ans = input("enter another service? [y/n] ")
        if ans != 'y':
            break
    print("")
    print("Building Entrances")
    while True:
        newEntrance(b, False)
        ans = input("enter another entrance? [y/n]")
        if ans != 'y':
            break
    print("Final Document:\n")
    print(b)
    return b