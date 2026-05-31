from tortoise.models import Model
from tortoise.fields import CharField

class Operation(Model):
    label = CharField(primary_key=True, max_length=255)
    command = CharField(max_length=255)