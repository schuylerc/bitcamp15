from django.db import models


class DwellingManager(models.Manager):
    def createDwelling(self):
        pass

    def updateDwelling(self):
        pass

    def deleteDwelling(self):
        pass


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __str__(self):
        return "{0} {1}, {2}".format(self.number, self.street, self.state)

    def __unicode__(self):
        return u"{0} {1}, {2}".format(self.number, self.street, self.state)


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

    dwelling_type = models.CharField(max_length=2, choices=DWELLING_CHOICES)

    objects = DwellingManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
