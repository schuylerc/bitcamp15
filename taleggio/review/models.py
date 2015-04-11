from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

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
