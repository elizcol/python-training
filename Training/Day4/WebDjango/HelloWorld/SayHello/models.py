from django.db import models
from mongoengine.document import Document
from mongoengine.fields import StringField

# Create your models here.
class Contact(models.Model):
    firstName = StringField
    lastName = StringField
    email = StringField