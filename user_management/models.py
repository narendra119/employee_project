from django.db import models

# Create your models here.
# We create and access models through django orm
# Django ORM 

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    
    emp_id = models.IntegerField(blank=False, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.name

class City(models.Model):
    METRO_OPT=(
        ('y','yes'),
        ('n','no')
    )
    
    name=models.CharField(max_length=100)
    metro=models.CharField(max_length=1, choices=METRO_OPT)
    