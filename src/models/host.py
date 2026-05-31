from tortoise.models import Model
from tortoise.fields import IntField, CharField

class Host(Model):
    label = CharField(primary_key=True, max_length=255)
    hostname = CharField(max_length=255)
    port = IntField()
    username = CharField(max_length=255)
    password = CharField(max_length=255)