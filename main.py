# Python Script that lets APSC100 Group Members enter building data into our instance of MongoDB
# Uses a general building schema

# Print Welcome

# Imports
import qrcode
import getpass
import login as LoginClient
#from pymongo import MongoClient

print("Welcome to the QueensQR Data Entry Utility")
print("Please Login")

# Login database user
usr = input("username: ")
try:
    pwd = getpass.getpass("password: ")
    mongo = LoginClient.auth(usr, pwd)
except Exception as err:
    print("Login Error", err)
else:
    pass

print(mongo)
print("Logged in DB USER")

exit()