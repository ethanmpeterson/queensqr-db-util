# Python Script that lets APSC100 Group Members enter building data into our instance of MongoDB
# Uses a general building schema

# Print Welcome

# Imports
import getpass
import login as LoginClient
import entry as EntryClient
import gen as QRClient
import selector as SelectionTool
import file as FileClient


print("Welcome to the QueensQR Data Entry Utility")
print("Please Login")

# Login database user
usr = input("username: ")
try:
    pwd = getpass.getpass("password: ")
    print("\n")
    mongo = LoginClient.auth(usr, pwd)
except Exception as err:
    print("Login Error", err)
else:
    pass

print(mongo)
print("\n")
print("Logged in")

# Get DB object and collection of buildings

db = mongo.apscm3

collection = db.buildings

print(db)
print(collection)

print("\nData Retreived")

# Prompt User

print("Please Select an Action (Enter the number corresponding to the action)\n")
print("(1) List all buildings\n")
print("(2) Enter data for a new building\n")
print("(3) Generate a QR Code image for a certain building\n")

ans = input("answer: ")

# collect all building objects in array
buildings = list(collection.find({}))

if ans == "1":
    for i, b in enumerate(buildings):
        print("\n-------------------------\n")
        print("index = " + str(i) + "\n")
        print(b)
        print("\n-------------------------\n")
elif ans == "2":
    try:
        objectId = collection.insert_one(EntryClient.newBuilding()).inserted_id
        print("Object Placed in DB under ID: " + str(objectId))
    except Exception as err:
        print("Failed to insert object into DB", err)
    else:
        pass
    # Prompt if user would like to generate QR code using that object id
    ans = int(input("entrance index: "))
    QRClient.generate(objectId, ans)
    exit()
elif ans == "3":
    selection = SelectionTool.selectFrom(buildings)
    print("You Have Selected " + selection['name'] + "\nGenerate a QR Code?")
    ans = input("answer [y/n] ")
    if (ans == 'y'):
        ans = int(input("entrance index: "))
        QRClient.generate(selection['_id'], ans)
    elif (ans == 'n'):
        exit()
    else:
        print("Enter a valid input")
        exit()



exit()