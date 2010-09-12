from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField
    price = models.DecimalField
    location = models.CharField

class ItemContact(models.Model):
    item = models.ForeignKey(Item)
    email = models.CharField
    phone = models.CharField
    name = models.CharField
    fb_profile = models.CharField

class ItemDescription(models.Model):
    item = models.ForeignKey(Item)
    description = models.CharField

class ItemPicture(models.Model):
    item = models.ForeignKey(Item)
    picture = models.CharField

class Person(models.Model):
    username = models.CharField
    location = models.CharField

class PersonFlags(models.Model):
    person = models.ForeignKey(Person)
    item = models.ForeignKey(Item)
    flag = models.CharField
