import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint
import os

# Connect to Mongo database
passcode = os.environ.get('Passcode')
uri = "mongodb+srv://swingfsy:" + passcode + "@swingtestcluster0.n5iknl4.mongodb.net/"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

# Create an instance of the Mongo database
db = client.contactList

# Create a collection of the database
contactData = db.contactData

# Main function to CRUD the contact list
def contactBook():
    while True:
        print("Please select your operation. List(L) / Read(R) / Add(A) / Edit(E) / Delete(D) / Quit(Q): \n")
        op = str.upper(input())

        match op:
            case 'A':
                print("Please input phone number,sex and name, separated by colon(;): \n ")

                 # Format the input 
                txt = input()

                if txt.count(';') >= 2:
                    new_phone = txt.split(";")[0]
                    new_sex = txt.split(";")[1]
                    new_name = txt.split(";")[2]
                else:
                    print("Invalid format.")
                    return
                
                add_Data(new_phone, new_sex, new_name)

            case 'R':
                print("Please input the phone number to view: \n ")

                check_phone = input()
                validate_input(check_phone)   
                read_Data(check_phone)

            case 'L':
                list_Data()
            
            case 'D':
                print("Please input the phone number to delete")

                check_phone = input()
                validate_input(check_phone)    
                delete_Data(check_phone)
            
            case 'E':
                print("Please input the phone number to update")

                check_phone = input()
                validate_input(check_phone)
                edit_Data(check_phone)
            
            case 'Q':
                print("Goodbye.")
                sys.exit()
        
            case _:
                print("Invalid operation.")


# Define the class for datastructure
class Contact:

    def __init__(self, phone, sex, name) -> None:
        self.setPhone(phone)
        self.setSex(sex)
        self.name = name

# check the format of user input for a phone number     
    def setPhone(self, phone) -> None:
            try: 
               intphone = int(phone)
               self.phone = phone.strip()
            except ValueError:
                raise ValueError("Invalid format")

# check the format of user input for sex      
    def setSex(self, sex) -> None: 
        upper = sex.upper()
        if upper == 'F' or upper == 'FEMALE':
            self.sex = 'Female'
        elif upper == 'M' or upper == 'MALE':
            self.sex = 'Male'
        else: 
            raise ValueError("Invalid format")


# Define functions for operations       
# Add a new contact item
def add_Data(new_phone, new_sex, new_name) -> None:
    
    # check if the contact item already exists 
    if contactData.find_one({"Phone": new_phone}) != None:
        print("Phone number already exists.")
        return

    c = Contact(new_phone, new_sex, new_name)

    contactItem ={
        "Phone": c.phone,
        "Sex": c.sex,
        "Name": c.name,
    }

    contactData.insert_one(contactItem)
    print("New contact added. Total count is {}.".format(contactData.count_documents({})))


# Read a contact item from the contact List
def read_Data(check_phone) -> None:

    item = contactData.find_one({"Phone": check_phone})
    if item != None:
        pprint.pprint(item)
    else:
        print("Contact not found")
            

# List all the data from the contact list
def list_Data():
    for contactItem in contactData.find():
        pprint.pprint(contactItem)
    print( "{} contact(s) displayed.".format(contactData.count_documents({})))


# Delete data from the contact list
def delete_Data(check_phone):

    result = contactData.delete_one({"Phone": check_phone})

    if result.deleted_count != 0:
        print("Contact deleted. Total count is {}.".format(contactData.count_documents({})))
        return
    else: 
        print("Contact not found")
            

# Edit data from the contact list
def edit_Data(check_phone):
    
    item = contactData.find_one({"Phone": check_phone})
    if item != None:
        print("Update sex: \n ")
        update_sex = input()
        print("Update name: \n ")
        update_name = input()

        x = Contact(check_phone, update_sex, update_name)

        # Update the contact item
        contactData.update_one(
            {"Phone": check_phone},
            {
                 "$set": {
                "Sex": x.sex,
                "Name": x.name
                }
            }
        )
        print("Contact updated.")
            
    else: 
        print("Contact not found")


# Verify if the input phone is validate
def validate_input(check_phone):
    try:
        intphone = int(check_phone)
    except ValueError:
        print("Invalid format.")
        return
