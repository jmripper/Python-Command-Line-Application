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

person = input("Welcome! Type 'create' to create a new contact")

# if person == 'create':
#     name = input("New contact's name:")
#     address = input("Contact's address:")
#     phone = int(input("Contact's phone number:"))
#     email = input("Contact's email address:")
#     birthday = int(input("Contact's birthday (YY/MM/DD):"))
#     new_person = contact(name=name, address=address, phone=phone, email=email, birthday=birthday)
#     new_person.save()
#     print()