from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class MenuItem(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.IntegerField(
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0),
        ]
    )

   def __str__(self):
      return f'{self.title} : {str(self.price)}'
   
   
class Booking(models.Model):
   name = models.CharField(max_length=255) 
   no_of_guests = models.IntegerField(
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(0),
        ]
    )
   booking_date = models.DateTimeField() 

   def __str__(self):
      return self.name

