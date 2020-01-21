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
        print("\nMAIN MENU:")
        person = input("\nType 'create' to create a new contact \nType 'update' a contact's information \nType 'search' to lookup a contact \nType 'remove' to remove a contact\n\n")
        if person == "create":
            self.create()
        elif person == "update":
            self.update()
        elif person == "search":
            self.search()
        elif person == "remove":
            self.remove()
        else:
            print("Sorry that's not an option. Bye!")
            exit()
            
    def create(self):
        print("\nCreate a New Contact")
        name = input("\nNew contact's full name: ")
        address = input("Contact's address: ")
        phone = input("Contact's phone number: ")
        email = input("Contact's email address: ")
        birthday = input("Contact's birthday (YYYY,MM,DD): ")
        new_person = Contact(name=name, address=address, phone=phone, email=email, birthday=birthday)
        new_person.save()
        print("\nCongrats your information has been saved!")
        contact_book.options()

    def update(self):
        find_name = input("\nSearch for Contact's Information by Fullname to Update: ")
        update = Contact.get(Contact.name == find_name)
        print("")
        print(update.name)
        print(update.address)
        print(update.phone)
        print(update.email)
        print(update.birthday)
        new_name = input("\nUpdate Name to: ")
        new_address = input("Update Address to: ")
        new_phone = input("Update Phone Number to: ")
        new_email = input("Update Email to: ")
        update.name = new_name
        update.address = new_address
        update.phone = new_phone
        update.email = new_email
        update.save()
        print("\nThis contact has been updated!")
        contact_book.options()

    def search(self):
        search_info = input("\nFullname of the contact your searching for: ")
        search = Contact.select().where(Contact.name == search_info)
        # person_info = Contact.get(Contact.name == search_info)
        for person in search:
            print("")
            print(f"Name: {person.name}")
            print(f"Address: {person.address}")
            print(f"Phone: {person.phone}")
            print(f"Email: {person.email}")
            print(f"Birthday: {person.birthday}")
            print("")
        else:
            print("\nSorry that person does not exist.")
            contact_book.options()

    def remove(self):
        remove = input("\nSearch by Name to remove the contact: ")
        remove_person = Contact.get(Contact.name == remove)
        remove_person.delete_instance()
        print("\nContact has been removed.")
        contact_book.options()
   
contact_book = ContactBook()
contact_book.options()