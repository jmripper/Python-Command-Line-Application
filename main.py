from peewee import *
from datetime import date

db = PostgresqlDatabase('Contact_book', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
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