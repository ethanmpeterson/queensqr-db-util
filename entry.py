# Prompt User For all Data needed for a new Building Object in the DB
# return a dictionary that can be posted to the DB in the main.py file

b = {}
b['services'] = []
b['entrances'] = []
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

def posEntry():
    posDict = {}
    posDict['x'] = float(input("x: "))
    posDict['y'] = float(input("y: "))
    return posDict

def newEntrance(targetDict):
    print("ENTRANCE ENTRY")
    print("All fields mandatory press enter to move onto the next one")
    entranceDict = {}
    
    entranceDict['name'] = input("name: ")
    print("Floating Point Numbers Required")
    entranceDict['pos'] = posEntry()
    targetDict['entrances'].append(entranceDict)
    

def newService():
    print("SERVICE ENTRY")
    print("all fields mandatory press enter to move onto the next one")
    serviceDict = {}
    serviceDict['name'] = input("name: ")
    serviceDict['room_number'] = input("room number: ")
    serviceDict['faculty'] = input("faculty: ")
    hourEntry("hours", serviceDict)
    serviceDict['description'] = input("description: ")
    b['services'].append(serviceDict)
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
    while True:
        newEntrance(b)
        ans = input("enter another entrance? [y/n]")
        if ans != 'y':
            break
    print("Final Document:\n")
    print(b)
    return b