from django.db import models
from rest_framework import serializers

class DwellingManager(models.Manager):

    def calculateRating(self, allRatings):
        return 3.5


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __unicode__(self):
        return u"{0} {1}, {2} {3}, {4}".format(self.number, self.street, self.city, self.state, self.zipcode)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address


class Dwelling(models.Model):
    address = models.ForeignKey('Address')
    desc = models.CharField(max_length = 500, default="Description")
    totalRating = 3.5
    reviewCount = 3

    TOWNHOUSE = 'TH'
    APARTMENT = 'A'
    HOUSE = 'H'

    DWELLING_CHOICES = (
        (TOWNHOUSE, 'Townhouse'),
        (APARTMENT, 'Apartment'),
        (HOUSE, 'House')
    )

    dwelling_type = models.CharField(max_length=2, choices=DWELLING_CHOICES,
                                     blank=True)

    objects = DwellingManager()

    def __unicode__(self):
        return str(self.address)


class DwellingSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Dwelling
