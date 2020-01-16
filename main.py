from peewee import *
from datetime import date

db = PostgresqlDatabase('contact_book', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:\
        database = db

# create base model class of Contact


class Contact(BaseModel):
    name = CharField()
    address = CharField()
    phone = CharField()
    email = CharField()
    birthday = DateField()

# Create tables
db.create_tables([Contact])

print("Welcome to Your Contact Book!")

class ContactBook:
    def options(self):
        print("\nMENU")
        person = input("\nType 'create' to create a new contact \nType'update' a contact's information \nType 'search' to lookup a contact \nType 'remove' to remove a contact\n")
        if person == "create":
            self.create()
        elif person == "update":
            self.update()
        elif person == "search":
            self.search()
        elif person == "remove":
            self.remove()
        else:
            print("\nSorry that's not an option. Bye!")
            exit()
            
    def create(self):
        print("\nCreate a New Contact")
        name = input("New contact's full name: ")
        address = input("Contact's address: ")
        phone = int(input("Contact's phone number: "))
        email = input("Contact's email address: ")
        birthday = input("Contact's birthday (YYYY,MM,DD): ")
        new_person = Contact(name=name, address=address, phone=phone, email=email, birthday=birthday)
        new_person.save()
        print("")
        print("Congrats your information has been saved!")
        print("")
        print(f"Name: {new_person.name}")
        print(f"Address: {new_person.address}")
        print(f"Phone Number: {new_person.phone}")
        print(f"Email: {new_person.email}")
        print(f"Birthday: {new_person.birthday}")

def update():
    if person == 'update':
        find_name = input("Search for Contact's Name to Update: ")
        update = Contact.get(Contact.name == find_name)
        print("")
        print(update.name)
        print(update.address)
        print(update.phone)
        print(update.email)
        print(update.birthday)
        print("")
        name = input("Update Name to: ")
        update.name = name
        address = input("Update Address to: ")
        update.address = address
        phone = input("Update Phone Number to: ")
        update.phone = phone
        email = input("Update Email to: ")
        update.email = email
        # update_info = (Contact.update(name=name, address=address, phone=phone, email=email).where(update.name == find_name))
        # info = update_info.excute()
        print("Here is your updated information!")
        print(f"Updated Info: {update.name}")

def search():
    if person == 'search':
        search_info = input("Name of the contact your searching for: ")
        person_info = Contact.get(Contact.name == search_info)
        print("")
        print(f"Name: {person_info.name}")
        print(f"Address: {person_info.address}")
        print(f"Phone: {person_info.phone}")
        print(f"Email: {person_info.email}")
        print(f"Birthday: {person_info.birthday}")
        print("")

def remove():
    if person == 'remove':
        remove = input("Search by Name to remove the contact: ")
        remove_person = Contact.get(Contact.name == remove)
        remove_person.delete_instance()
        print("Contact has been removed.")

    
contact_book = ContactBook()
contact_book.options()

