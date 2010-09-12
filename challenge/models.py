from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=256)
    price = models.IntegerField()
    location = models.CharField(max_length=256)
    url = models.CharField(max_length=2048)
    def __unicode__(self):
        return "{'title':'"+self.title+"', 'price':'"+str(self.price)+"', 'location':'"+self.location+"', 'url':'"+self.url+"'}"

class ItemContact(models.Model):
    item = models.ForeignKey(Item)
    email = models.CharField(max_length=256)
    #phone = models.CharField(max_length=16)
    #name = models.CharField(max_length=64)
    #fb_profile = models.CharField(max_length=64)

class ItemDescription(models.Model):
    item = models.ForeignKey(Item)
    description = models.CharField(max_length=32000)

class ItemPicture(models.Model):
    item = models.ForeignKey(Item)
    picture = models.CharField(max_length=256)

class Person(models.Model):
    username = models.CharField(max_length=64)
    location = models.CharField(max_length=255)

class PersonFlags(models.Model):
    person = models.ForeignKey(Person)
    item = models.ForeignKey(Item)
    flag = models.CharField(max_length=64)
