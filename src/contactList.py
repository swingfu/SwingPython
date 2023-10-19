import sys


class Contact:

    def __init__(self, phone, sex, name) -> None:
        self.setPhone(phone)
        self.setSex(sex)
        self.name = name

# check the format of user input for a phone number     
    def setPhone(self, phone) -> None:
            try: 
               intphone = int(phone)
               self.phone = phone
            except ValueError:
                print("Invalid format")

# check the format of user input for sex      
    def setSex(self, sex) -> None: 
        upper = sex.upper()
        if upper == 'F' or upper == 'FEMALE':
            self.sex = 'Female'
        elif upper == 'M' or upper == 'MALE':
            self.sex = 'Male'
        else: print("Invalid format")

    def print(self):
        print(self.phone + " " + self.sex + " " + self.name)

class ContactBook: 

    def __init__(self):
         self.contactList = []
    
# add a new contact into the contact list
    def add_Data(self):
        
        print("Please input phone number,sex and name, separated by colon(;): \n ")

        # to format the user's input 
        txt = input()
        new_phone = txt.split(";")[0]
        new_sex = txt.split(";")[1]
        new_name = txt.split(";")[2]

        c = Contact(new_phone, new_sex, new_name)
        # c.print()
        
        # to check if the phone number alreay exist
        for i in range(len(self.contactList)):
            x = self.contactList[i]
            if new_phone == x.phone:
                print("Phone number already exists.")
                return
        self.contactList.append(c)

        n = str(len(self.contactList))
        print("New contact added. Total count is " + n + ".")



# read a contact from the contact list
    def read_Data(self) -> None:

        print("Please input the phone number to view: \n ")

        check_phone = input()

        for i in range(len(self.contactList)):
            r = self.contactList[i]
            if check_phone == r.phone:
                r.print()
                return
            
        print("Contact not found")



# list all the data from the contact list
    def list_Data(self):
        for i in range(0, len(self.contactList)):
            l = self.contactList[i]
            l.print()
        n = str(len(self.contactList))
        print( n + " contact(s) displayed.")
            

# delete data from the contact list
    def delete_Data(self):
        print("Please input the phone number to delete")

        del_phone = input()

        for i in range(len(self.contactList)):
            d = self.contactList[i]
            if del_phone == d.phone:
                d.print()
                # print(d.phone + " " + d.sex + " "+ d.name)
                self.contactList.remove(d)
                n = str(len(self.contactList))
                print("Contact deleted. Total count is" + n + ".")
                return
        print("Contact not found")

# edit data from the contact list
    def edit_Data(self):
        print("Please input the phone number to update")

        update_phone = input()

        for i in range(len(self.contactList)):
            e = self.contactList[i]
            if update_phone == e.phone:
                print("Update sex: \n ")
                update_sex = input()
                print("Update name")
                update_name = input()
                self.contactList.remove(e)

                e.setPhone(update_phone)
                e.setSex(update_sex)
                e.name = update_name
                self.contactList.insert(i,e)
                print("Contact updated.")
                e.print()
                return
                # print(e.phone + " "+ e.setSex + " " + e.name)

        print("Contact not found")


y = ContactBook()

while True:
    print("Please select your operation. List(L) / Read(R) / Add(A) / Edit(E) / Delete(D) / Quit(Q): \n")
    op = str.upper(input())

    match op:
        case 'A':
            y.add_Data()

        case 'R':
            y.read_Data()

        case 'L':
            y.list_Data()
            
        case 'D':
            y.delete_Data()
            
        case 'E':
            y.edit_Data()
            
        case 'Q':
            print("Goodbye.")
            sys.exit()
        
        case _:
            print("Invalid operation.")

