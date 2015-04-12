from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import random

from dwelling.models import Dwelling

# Create your models here.

class ReviewManager(models.Manager):
   def processGuessedRating(self):
      #receive post data from a review and calculate a rating
      pass

   def getOverallRating(self):
      #returns the overall rating attached to a given object(tenant, landlord, dwelling)
      pass

   def createReview(self):
      #creates review
      pass

   def updateReview(self):
      #update the review
      pass

   def deleteReview(self):
      #deletes review
      pass

   def ReviewsOwnedByUser(self):
      #returns all the reviews owned by a specific user
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

   def save(self, *args, **kwargs):
      from metamind.api import ClassificationModel, set_api_key
      set_api_key("JcsbHMxoLMdw70XN9XxSWH03H69yYKA8Ruad6B28lA1kgY0s4t")
      prediction = ClassificationModel(id=88).predict(self.content, input_type="text")

      rint = random.randint(0,1)

      if (prediction[0].get('label') == 'negative'):
            self.rating = .5 + rint
      else:
         if (prediction[0].get('probability') < .4):
            if (rint == 0):
               self.rating = 2.5
            else:
               self.rating = 3.5
         else:
            self.rating = 5 - rint

      super(Review, self).save(*args, **kwargs) # Call the "real" save() method.


class DwellingReview(Review):
   Dwelling = models.ForeignKey(Dwelling)

class TenantReview(Review):
   Tenant = models.ForeignKey(User, related_name="Tenant") #this object may need to be changed later after oauth develops and Landlord/Tenant models are created

class LandlordReview(Review):
   Landlord = models.ForeignKey(User, related_name="Landlord") #this object may need to be changed later after oauth develops and Landlord/Tenant models are created


