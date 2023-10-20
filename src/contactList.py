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
               self.phone = phone.strip()
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
    
    def search_Phone(self,check_phone) -> int:
        for i in range(len(self.contactList)):
            r = self.contactList[i]
            if check_phone == r.phone:
                return i
        return -1

# add a new contact into the contact list
    def add_Data(self):
        
        print("Please input phone number,sex and name, separated by colon(;): \n ")

        # to format the user's input 
        txt = input()
        # print(txt.count(';'))

        if txt.count(';') >= 2:
            new_phone = txt.split(";")[0]
            new_sex = txt.split(";")[1]
            new_name = txt.split(";")[2]
        else:
            print("Invalid format.")
            return
        
        i = self.search_Phone(new_phone)

        if i >= 0 :
            print("Phone number already exists.")
            return

        c = Contact(new_phone, new_sex, new_name)
        
        self.contactList.append(c)

        print("New contact added. Total count is {}.".format(len(self.contactList)))



# read a contact from the contact list
    def read_Data(self) -> None:

        print("Please input the phone number to view: \n ")

        check_phone = input()
        try: 
            intphone = int(check_phone)
        except ValueError:
            print("Invalid format")
            return

        i = self.search_Phone(check_phone)
        if (i < 0):
            print("Contact not found")
        else:
            self.contactList[i].print()
        

# list all the data from the contact list
    def list_Data(self):
        for x in self.contactList:
            x.print()
        print( "{} contact(s) displayed.".format(len(self.contactList)))
            

# delete data from the contact list
    def delete_Data(self):
        print("Please input the phone number to delete")

        del_phone = input()
        try: 
            intphone = int(del_phone)
        except ValueError:
            print("Invalid format")
            return
        
        i = self.search_Phone(del_phone)
        e = self.contactList[i]
        e.print()

        self.contactList.pop(i)
        print("Contact deleted. Total count is {}.".format(len(self.contactList)))
        return
    
# edit data from the contact list
    def edit_Data(self):
        print("Please input the phone number to update")

        update_phone = input()
        try: 
            intphone = int(update_phone)
        except ValueError:
            print("Invalid format")
            return
        
        i = self.search_Phone(update_phone)
        if (i < 0):
            print("Contact not found")
            return

        e = self.contactList[i]

        print("Update sex: \n ")
        update_sex = input()
        print("Update name")
        update_name = input()
        #self.contactList.remove(e)
        e.setPhone(update_phone)
        e.setSex(update_sex)
        e.name = update_name
        #self.contactList.insert(i,e)
        print("Contact updated.")
        e.print()


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

