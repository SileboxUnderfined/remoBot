from tortoise.models import Model
from tortoise.fields import IntField, CharField

class Host(Model):
    id = IntField(primary_key=True)
    hostname = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_length=255)