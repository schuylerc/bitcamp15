from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from dwelling.models import Dwelling

# Create your models here.

class ReviewManager(models.Manager):
   def processGuessedRating(self):
      #receive post data from a review and calculate a rating
      pass

   def getOverallRating(self):
      #returns the overall rating attached to a given object(tenant, landlord, dwelling)
      pass

class Review(models.Model):
   rating = models.IntegerField(
      default=1,
      validators=[
         MaxValueValidator(5),
         MinValueValidator(1)
      ]
   )

   timeCreated = models.DateTimeField()
   userCreated = models.ForeignKey(User)
   content = models.CharField(max_length=500)

   objects = ReviewManager()

   def __str__(self):
      return self.userCreated.__str__() + " - " + self.content[:10]

class DwellingReview(Review):
   Dwelling = models.ForeignKey(Dwelling)

class TenantReview(Review):
   Tenant = models.ForeignKey(User, related_name="Tenant") #this object may need to be changed later after oauth develops and Landlord/Tenant models are created

class LandlordReview(Review):
   Landlord = models.ForeignKey(User, related_name="Landlord") #this object may need to be changed later after oauth develops and Landlord/Tenant models are created


