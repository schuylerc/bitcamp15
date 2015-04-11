from django.db import models
#from django.contrib.gis.db import models
#from django.contrib.localflavor.us.models import USStateField

class DwellingManager(models.Manager):
   pass


# Create your models here.
class Address(models.Model):
   number = models.IntegerField()
   street = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   state = models.CharField(max_length=2)
   zipcode = models.IntegerField()

   objects = DwellingManager()

class Dwelling(models.Model):
   name = models.CharField(max_length=30)
   address = models.ForeignKey('Address')

   TOWNHOUSE = 'TH'
   APARTMENT = 'A'
   HOUSE = 'H'

   DWELLING_CHOICES = (
      (TOWNHOUSE, 'Townhouse'),
      (APARTMENT, 'Apartment'),
      (HOUSE, 'House')
   )

   dwellingType = models.CharField(max_length=2, choices=DWELLING_CHOICES)

   def __str__(self):
      return ""


